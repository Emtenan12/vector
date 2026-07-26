# Validation report: data/stage3_chunks/ADP_Cleaned_sample.jsonl

Total chunks: 885  |  Documents: 3

## 1. Content-preservation ratio (per document)
  [PASS] ADP_1-01: 103.17% (threshold >= 99%)
  [PASS] ADP_3-0: 101.71% (threshold >= 99%)
  [PASS] ADP_6-0: 101.19% (threshold >= 99%)

## 2. Leaked-artifact scan
  [PASS] 0 leaked-prompt hits, 0 chunks with (cid:) artifacts

## 3. doc_id format consistency
  [PASS] all doc_ids match ADP_X-Y / ATP_X-Y

## 4. Known-enumeration regression tests
  [SKIP] regression: ADP 5-0 MDMP 7-step list: SKIPPED -- no chunks found for doc_id prefix 'ADP_5-0' (source PDF not yet processed in this run)
  [PASS] regression: ADP 6-0 mission command 7 principles: best chunk 'ADP_6-0__000034' matched 7/7 items (need >= 7)

## 5. Chunk token-count distribution
  [INFO] n=885 min=8 median=120 max=1418 | 34 chunks (3.8%) exceed max_seq_length=256 (will be silently truncated by the dense embedder at query/index time -- flagged, not a failure by itself, since these are logged last-resort overflow units from unsplittable lists/tables)

## Summary: 7 passed, 0 failed, 1 skipped