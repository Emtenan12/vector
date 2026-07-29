"""Prove query-side and passage-side embeddings share one model/vector space."""
import json, numpy as np, chromadb
from sentence_transformers import SentenceTransformer
from pipeline.embed_index import COLLECTION_NAME

BGE_QUERY_PREFIX = 'Represent this sentence for searching relevant passages: '
EMBED_MODEL = 'models/bge-small-en-v1.5'          # the patched value

m = SentenceTransformer(EMBED_MODEL, device='cpu')
print('loaded          :', EMBED_MODEL)
print('dim             :', m.get_sentence_embedding_dimension())
print('max_seq_length  :', m.max_seq_length, '  (512=bge-small, 256=all-MiniLM-L6-v2)')
print()

col = chromadb.PersistentClient(path='data/indexes/chroma_db').get_collection(COLLECTION_NAME)

# TEST 1: re-embed stored passages and compare to the vectors actually in the index.
# If the index were built by a different model, this cosine would be far from 1.
got = col.get(limit=5, include=['documents', 'embeddings'])
print('TEST 1 — re-embed stored passages, compare to indexed vectors')
sims = []
for cid, doc, stored in zip(got['ids'], got['documents'], got['embeddings']):
    fresh = m.encode([doc])[0]
    s = np.array(stored, dtype=np.float64); f = np.array(fresh, dtype=np.float64)
    cos = float(s @ f / (np.linalg.norm(s) * np.linalg.norm(f)))
    sims.append(cos)
    print(f'   {cid:<22} cosine(stored, re-embedded) = {cos:.6f}')
print(f'   min={min(sims):.6f}  -> {"MATCH (same model)" if min(sims) > 0.999 else "MISMATCH"}')
print()

# TEST 2: end-to-end retrieval through the patched query path.
print('TEST 2 — query path with BGE_QUERY_PREFIX against the same index')
for q, want in [('What are the seven steps of the military decision-making process?','ADP_5-0'),
                ('What are the principles of mission command?','ADP_6-0'),
                ('What are the characteristics of the defense?','ADP_3-90')]:
    emb = m.encode(BGE_QUERY_PREFIX + q).tolist()
    r = col.query(query_embeddings=[emb], n_results=3)
    top, dist = r['ids'][0][0], r['distances'][0][0]
    ok = 'OK ' if top.startswith(want) else 'BAD'
    print(f'   [{ok}] {q[:52]:<52} -> {top:<20} d={dist:.4f}')
