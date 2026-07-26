# Validation report: data/stage3_chunks/ADP_Cleaned.jsonl

Total chunks: 4032  |  Documents: 15

## 1. Content-preservation ratio (per document)
  [PASS] ADP_6-22: 100.88% (threshold >= 99%)
  [FAIL] ADP_7-0: 0.00% (threshold >= 99%)
  [PASS] ADP_1-01: 103.21% (threshold >= 99%)
  [PASS] ADP_1: 101.02% (threshold >= 99%)
  [PASS] ADP_2-0: 101.29% (threshold >= 99%)
  [PASS] ADP_3-0: 101.80% (threshold >= 99%)
  [PASS] ADP_3-05: 100.92% (threshold >= 99%)
  [PASS] ADP_3-07: 100.86% (threshold >= 99%)
  [PASS] ADP_3-13: 101.24% (threshold >= 99%)
  [PASS] ADP_3-19: 100.49% (threshold >= 99%)
  [PASS] ADP_3-28: 100.96% (threshold >= 99%)
  [PASS] ADP_3-37: 101.76% (threshold >= 99%)
  [PASS] ADP_3-90: 104.60% (threshold >= 99%)
  [PASS] ADP_4-0: 101.65% (threshold >= 99%)
  [PASS] ADP_5-0: 102.60% (threshold >= 99%)
  [PASS] ADP_6-0: 101.28% (threshold >= 99%)

## 2. Leaked-artifact scan
  [PASS] 0 leaked-prompt hits, 0 chunks with (cid:) artifacts

## 3. doc_id format consistency
  [PASS] all doc_ids match ADP_X-Y / ATP_X-Y

## 3b. Font-encoding corruption (per document)
  [PASS] all 15 documents under 2% replacement chars

## 3c. Zero-chunk documents
  [FAIL] 1 document(s) produced ZERO chunks: ['ADP_7-0'] -- no extractable text layer (needs OCR or a replacement source file)

## 4. Known-enumeration regression tests
  [PASS] regression: ADP 5-0 MDMP 7-step list: best chunk 'ADP_5-0__000125' matched 7/7 items (need >= 7)
  [PASS] regression: ADP 6-0 mission command 7 principles: best chunk 'ADP_6-0__000022' matched 7/7 items (need >= 7)

## 5. Chunk token-count distribution
  [INFO] n=4032 min=4 median=154.5 max=2141 | 99 chunks (2.5%) exceed max_seq_length=512 (will be silently truncated by the dense embedder at query/index time -- flagged, not a failure by itself, since these are logged last-resort overflow units from unsplittable lists/tables)

## Summary: 21 passed, 2 failed, 0 skipped