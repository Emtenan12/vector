"""
Query-side spell correction against a DOMAIN vocabulary.

Why query-side: the retrieval eval showed typo variants failing at 45%
(dense) and 40% (sparse) against 80%/85% on the primary phrasing -- i.e.
the dense side degrades nearly as much as the sparse side, so this is not
a BM25 tokenization problem. Confirmed cause is subword shattering in the
embedder's WordPiece tokenizer: "dynamics" is one token, "dynmaics" is
d+##yn+##ma+##ics. No index-side change can repair that, because both
indexes are already built from correctly-spelled text. The query is the
only place the damage can be undone.

Why a domain vocabulary rather than a general English dictionary: the
corrections have to land on doctrine terms. A generic dictionary has no
reason to prefer "maneuver" over "manoeuvre"/"manure" for "manuever", and
worse, it will happily "correct" doctrine acronyms (MDMP, IPOE, COA, TLP)
into ordinary words. Building the frequency dictionary from the corpus
itself makes in-domain corrections the default by construction.

The guards below exist because a spell corrector that fires too eagerly
hurts the categories it was not meant to touch -- casual queries contain
"plz", "gimme", "whats", "em", and rewriting those into doctrine terms
would inject content words the user never asked for. Each guard is
therefore a bias toward LEAVING TOKENS ALONE.
"""
import json
import re
from collections import Counter
from pathlib import Path

_WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")

# The BM25 stopword list the index was built with. Imported by value rather
# than referenced so this module stays usable without the index loaded.
from pipeline.embed_index import _STOPWORDS as _RETRIEVAL_STOPWORDS  # noqa: E402

# Conversational filler that appears in the suite's casual variants. These
# are not doctrine terms, are not misspellings, and must never be "fixed"
# into one -- "plz" sits within edit distance 2 of several real corpus
# words.
_CHAT_STOPLIST = {
    "plz", "pls", "gimme", "whats", "wat", "wanna", "gonna", "em", "n",
    "r", "u", "ur", "thx", "ok", "okay", "yeah", "hey", "quick", "real",
    "lemme", "kinda", "sorta", "info", "stuff",
}


class DomainSpellCorrector:
    """Correct out-of-vocabulary query tokens toward corpus terms.

    backend="symspell" uses SymSpell's precomputed-delete index (fast,
    O(1)-ish lookup, extra dependency + memory). backend="rapidfuzz" scans
    the vocabulary with a C-backed Levenshtein (no index to build, scales
    with vocabulary size). Both are evaluated rather than assumed; see
    eval/typo_correction_eval.md.
    """

    def __init__(self, vocab: Counter, backend: str = "symspell",
                 min_freq: int = 3, max_edit: int = 2, min_len: int = 5,
                 min_candidate_freq: int = 5, guard_english: bool = True):
        self.backend = backend
        self.min_freq = min_freq
        self.max_edit = max_edit
        self.min_len = min_len
        self.min_candidate_freq = min_candidate_freq
        self.vocab = vocab
        self.known = {w for w, n in vocab.items() if n >= min_freq}
        # Ordinary English words that simply aren't doctrine terms must be
        # left alone. Without this guard the corpus vocabulary treats them
        # as out-of-vocabulary and "corrects" them into doctrine terms:
        # observed corpus->corps, intel->into, aren't->agent, each of which
        # destroys the query it appears in.
        self.english = _load_english_words() if guard_english else set()

        if backend == "symspell":
            from symspellpy import SymSpell, Verbosity

            self._Verbosity = Verbosity
            self.sym = SymSpell(max_dictionary_edit_distance=max_edit, prefix_length=7)
            for w, n in vocab.items():
                if n >= min_freq:
                    self.sym.create_dictionary_entry(w, n)
        elif backend == "rapidfuzz":
            self.candidates = [w for w, n in vocab.items()
                               if n >= min_candidate_freq and len(w) >= min_len]
        else:
            raise ValueError(f"unknown backend {backend!r}")

    # -- guards ---------------------------------------------------------
    def _skip(self, tok: str) -> bool:
        low = tok.lower()
        if low in _CHAT_STOPLIST:
            return True
        if len(low) < self.min_len:
            return True          # short tokens are too close to everything
        if low in self.known:
            return True          # already a corpus term
        if low in self.english:
            return True          # real English, just not doctrine vocabulary
        if "'" in low:
            return True          # contractions ("aren't") are not typos
        if tok.isupper():
            return True          # acronym as typed (MDMP, IPOE, COA, TLP)
        if any(ch.isdigit() for ch in tok):
            return True
        return False

    def _best(self, low: str) -> str | None:
        if self.backend == "symspell":
            sugg = self.sym.lookup(low, self._Verbosity.CLOSEST,
                                   max_edit_distance=self.max_edit,
                                   include_unknown=False)
            sugg = [s for s in sugg
                    if s.term != low and s.count >= self.min_candidate_freq]
            if not sugg:
                return None
            # Tie-breaking matters more than candidate generation here;
            # several typos have two candidates at the same edit distance.
            #   1. edit distance
            #   2. first character preserved -- typists rarely miss the
            #      opening letter, and without this "mision" resolves to
            #      "vision" rather than "mission".
            #   3. not a retrieval stopword -- correcting a content token
            #      into a function word deletes it from the BM25 stream
            #      entirely; this is what turns "froms" into "from"
            #      instead of "forms".
            #   4. corpus frequency, last. Leading with frequency picks the
            #      common function word every time; leading with length
            #      preservation picks "principle" over "principles".
            sugg.sort(key=lambda s: (
                s.distance,
                s.term[:1] != low[:1],
                s.term in _RETRIEVAL_STOPWORDS,
                -s.count,
            ))
            return sugg[0].term

        from rapidfuzz import process, fuzz

        hit = process.extractOne(low, self.candidates,
                                 scorer=fuzz.WRatio, score_cutoff=88)
        if not hit:
            return None
        term = hit[0]
        if term == low:
            return None
        # WRatio is not an edit distance; enforce the distance bound too so
        # a high similarity score on a short token cannot sneak through.
        from rapidfuzz.distance import Levenshtein

        if Levenshtein.distance(low, term) > self.max_edit:
            return None
        return term

    # -- public ---------------------------------------------------------
    def correct(self, query: str) -> tuple[str, list[tuple[str, str]]]:
        """Return (corrected_query, [(original, replacement), ...])."""
        edits: list[tuple[str, str]] = []

        def repl(m: re.Match) -> str:
            tok = m.group(0)
            if self._skip(tok):
                return tok
            best = self._best(tok.lower())
            if not best:
                return tok
            edits.append((tok, best))
            # Preserve leading capitalization so nothing downstream that
            # keys on case is surprised by the rewrite.
            return best.capitalize() if tok[:1].isupper() else best

        return _WORD_RE.sub(repl, query), edits


def _load_english_words() -> set[str]:
    """General-English word set, taken from the frequency dictionary that
    ships with symspellpy so no network fetch is needed (this environment
    has no egress to word-list hosts)."""
    try:
        import symspellpy
    except Exception:
        return set()
    path = Path(symspellpy.__file__).parent / "frequency_dictionary_en_82_765.txt"
    if not path.exists():
        return set()
    out = set()
    with path.open(encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            if parts:
                out.add(parts[0].lower())
    return out


def build_vocab(chunks: list[dict]) -> Counter:
    vocab: Counter = Counter()
    for c in chunks:
        vocab.update(w.lower() for w in _WORD_RE.findall(c["text"]))
    return vocab


def load_corpus_vocab(jsonl_path: Path) -> Counter:
    chunks = [json.loads(l) for l in jsonl_path.open(encoding="utf-8") if l.strip()]
    return build_vocab(chunks)
