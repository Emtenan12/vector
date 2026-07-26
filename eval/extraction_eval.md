# Extraction tool evaluation

Tested against 3 real ADP PDFs pulled from the Google Drive `DatasetPdf/ADP` folder — chosen to be
structurally diverse, with the difference **confirmed via PDF metadata**, not assumed:

| File | Size | Pages | Producer / Creator | Provenance |
|---|---|---|---|---|
| `ADP_1-01.pdf` | 2.9 MB | 44 | *(no Producer/Creator field)* | Pristine native — CreationDate `2019-07-17` matches the real ADP 1-01 publication date; no producer metadata is typical of the official DoD PDF publishing toolchain. |
| `ADP_3-0.pdf` | 1.5 MB | 56 | Producer: macOS Quartz PDFContext · Creator: **Microsoft Word for Microsoft 365** · Author: `Schrankel, Catherine J CIV USARMY MCCOE (USA)` | Retyped/reformatted in Word by a named Army civilian, printed to PDF on `2026-01-01`. Not the original publication pipeline. |
| `ADP_6-0.pdf`* | 3.1 MB | 82 | Producer: macOS Quartz PDFContext · Creator: **Safari** · `/Title` retains the original download URL (`irp.fas.org/...adp6_0.pdf?utm_source=chatgpt.com`) | Browser "print to PDF" of a web-hosted copy, `2025-12-22`. |

\* The canonical `ADP-6-0.pdf` (8.58 MB) and `ADP_5-0.pdf` (6.99 MB) could not be downloaded — see
**Environment constraint** below. A smaller duplicate of ADP 6-0's content already present in Drive
was substituted; its content was verified complete (301K extracted chars, 82 real pages via `pypdf`,
matches the expected ~140-page-equivalent doctrine text). No substitute existed for ADP 5-0.

Both `pypdf` parses of the two regenerated PDFs throw `Ignoring wrong pointing object` xref warnings —
a real, confirmed corpus-quality signal: this Drive folder is a mix of native official PDFs and
informally regenerated copies with corrupted cross-reference tables, independent of which extraction
tool is used downstream.

## Environment constraint (flagged, not routed around)

`mcp__Google_Drive__download_file_content` fails consistently ("session expired") on files roughly
≥4-7MB — confirmed via 18+ attempts across multiple fresh sessions on `ADP_5-0.pdf` (6.99MB, 0/18
succeeded) and `ADP-6-0.pdf` (8.58MB, failed until a smaller duplicate was found), while every file
≤3.7MB tested downloaded successfully first or second try. `read_file_content` (Drive's own text
extraction) succeeds on the same large files, so this is specific to the raw-binary-download code
path, not a general Drive outage. This still blocks `ADP_5-0.pdf` specifically, which is required for
the MDMP 7-step list regression test — **flagging back to the user**; will keep retrying opportunistically
and this needs to be resolved (or the file supplied another way) before the full 16-doc ADP run.

## Tools tested

1. **MarkItDown** (`markitdown[pdf]` 0.1.6, default config and `enable_plugins=False`) — no difference
   between the two configs; MarkItDown exposes no PDF-specific layout/heading options.
2. **pymupdf4llm** 1.28.0
3. **docling** 2.115.0 — **could not be run at all**, see below.

## Results

| File | Tool | Headings (`^#`) | `(cid:` artifacts | Other artifacts | Time |
|---|---|---:|---:|---|---:|
| ADP_1-01 | MarkItDown | **0** | 190 | — | 5.4s |
| ADP_1-01 | pymupdf4llm | **140** | 0 | — | 10.6s |
| ADP_3-0 | MarkItDown | **0** | 265 | — | 9.7s |
| ADP_3-0 | pymupdf4llm | **193** | 0 | 265× `�` replacement chars (isolated to a repeated header-date field, 0 in body text) | 11.5s |
| ADP_6-0 | MarkItDown | **0** | 0 | Private-Use-Area bullet glyphs (`\xef\x81\xac` etc.) instead of `-`/`•`, list marker glued to preceding text (`principles ofM-bM-^@M-^T`) | 10.8s |
| ADP_6-0 | pymupdf4llm | **168** | 0 | — | 18.1s |
| all | docling | N/A — see below | N/A | N/A | N/A |

Zero occurrences of either known leaked-prompt-fragment wording in any output from either tool.

### MarkItDown: reproduces the prior-session finding exactly, on 3/3 real documents

`grep -c "^#"` → 0 on every file, every config. Section titles land as bare text with no markdown
heading markup at all — confirmed this is not an artifact of one bad file, it's this tool's default
PDF path in general. Example (`ADP_6-0__markitdown_default.md`):

```
COMPETENCE
1-27. Tactically and technically competent commanders, subordinates, and teams are the basis...
```

vs. the same content in pymupdf4llm:

```
### **COMPETENCE**

1-27. Tactically and technically competent commanders, subordinates, and teams are the basis...
```

`(cid:`-style font-encoding failures appear on 2 of 3 files (190, 265 instances) — on the 3rd
(the Safari-regenerated copy) MarkItDown produces 0 `cid` artifacts but instead corrupts list markup:
bullets come through as raw Private-Use-Area glyph bytes from a dingbat font
(`M-oM-^AM-,` in `cat -A`, i.e. `\xef\x81\xac`) rather than a real `-`/`•`, and the list lead-in text
runs directly into the em-dash with no line break (`enabled by the principles ofM-bM-^@M-^T`). A
`MarkdownHeaderTextSplitter` pass has nothing to split on for any of the 3 files.

### pymupdf4llm: real headings, clean lists, one new (contained) artifact

`grep -c "^#"` → 140-193 per document. Headings map onto the real chapter/section structure
(`### Chapter 1`, `## PRINCIPLES OF MISSION COMMAND`, `### COMPETENCE`, ...), and heading levels are
consistent with document hierarchy, not flat. The mission-command 7-principles list (ADP 6-0) survives
completely intact, in the correct order, attached to its lead-in paragraph:

```
### **PRINCIPLES OF MISSION COMMAND**
...
Successful mission command is enabled by the principles of—

- Competence.
- Mutual trust.
- Shared understanding.
- Commander's intent.
- Mission orders.
- Disciplined initiative.
- Risk acceptance.

### **COMPETENCE**
```

Zero `(cid:` artifacts on all 3 files. One new artifact found on the Word-regenerated `ADP_3-0.pdf`:
265 Unicode replacement characters (`�`), but **all 265 are confined to one repeated running-header
date field** (`**2� M���� 2025**`, appearing once per page) — verified with a script checking every
line containing `�`; zero occurrences in body paragraphs. This field gets removed anyway by the
page-break noise-stripping required for finding #1, so it doesn't reach the chunker.

### Mid-sentence page-break corruption (finding #1) — reproduced, evidence captured

Both tools exhibit the exact bug described in the task's confirmed findings, on the same real
sentence in `ADP_6-0.pdf`. pymupdf4llm:

```
...This minimizes the number of decisions a

**1-6**

**ADP 6-0**

**31 July 2019**

**Introduction to Mission Command**

single commander makes and allows subordinates...
```

MarkItDown, same location:

```
...This minimizes the number of decisions a
1-6 ADP 6-0 31 July 2019

Introduction to Mission Command
single commander makes and allows subordinates...
```

The word group "a single commander" is split by 4 lines of page-footer/header noise (page number,
publication ID, date, running section title) in both tools, and the text before the break does not end
in terminal punctuation — exactly the trigger condition specified in finding #1. This pattern (page
number + pub-name + date + running chapter/section title, each its own bolded short line in
pymupdf4llm output) recurs ~1x per page (82 times in `ADP_6-0.pdf` alone) and is what
`pipeline/clean.py`'s noise detector is built against.

### docling: cannot run in this environment (policy-blocked), independent of quality

`docling.document_converter.DocumentConverter` requires downloading a layout-analysis model from
`huggingface.co` at first use — even with `do_ocr=False` and `do_table_structure=False` explicitly set
on `PdfPipelineOptions`. Every attempt failed with `httpx.ProxyError: 403 Forbidden`, consistent with
this sandbox's egress policy, which was independently confirmed to block direct `huggingface.co`
connections (`curl` to `huggingface.co` also returns a 403 CONNECT rejection at the proxy level, logged
in `recentRelayFailures`). Per this environment's own proxy guidance, a 403 policy denial is to be
reported, not routed around — so docling was not force-installed with a manually-staged model cache.

This is a real disqualifying finding independent of extraction quality: docling's core value
proposition (layout-aware parsing) is architecturally tied to a model that this environment cannot
fetch through any sanctioned path. Separately, `pip install docling` pulled **5.7GB** of dependencies,
2.7GB of which is pure NVIDIA/CUDA libraries — dead weight for a CPU-only ARM edge target regardless of
whether the network issue is ever resolved elsewhere.

## Decision: pymupdf4llm

- Only tool of the 3 that emits real markdown headings on real ADP PDFs (0 for MarkItDown on 3/3
  files, confirming and extending the prior session's single-file finding; docling never got to run).
- Zero `(cid:` artifacts on any of the 3 files (vs. 190/265 for MarkItDown on 2/3).
- Clean, correctly-ordered markdown lists with lead-in paragraphs attached — verified against the
  mission-command 7-principles enumeration, one of the two required regression tests.
- Lightweight: pulls in only `pymupdf`/`pypdfium2`-class dependencies, no torch/CUDA stack, runs in
  10-18s per ~50-80 page document on CPU with no model download.
- Real headings being present is what justifies using a narrow `MarkdownHeaderTextSplitter` pass in
  `pipeline/chunk.py` (see chunking module) — this precondition is now evidence-backed, not assumed.
- Its one new artifact (replacement-char corruption in a repeated header field on one Word-regenerated
  PDF) is fully contained within the noise-line pattern `clean.py` already has to strip for finding #1,
  so it does not require separate handling.
