# Validation report: data\atp_sample\stage3_chunks\ATP_sample_Cleaned.jsonl

Total chunks: 11444  |  Documents: 27

## 1. Content-preservation ratio (per document)
  [PASS] ATP_1-06x3: 102.07% (threshold >= 99%)
  [PASS] ATP_1-0.1-001: 102.71% (threshold >= 99%)
  [PASS] ATP_1-05.04-001: 102.48% (threshold >= 99%)
  [PASS] ATP_2-01.3-003: 103.93% (threshold >= 99%)
  [PASS] ATP_2-22.7-000: 102.85% (threshold >= 99%)
  [PASS] ATP_2-33.4-001: 101.42% (threshold >= 99%)
  [PASS] ATP_3-04.13-000: 114.79% (threshold >= 99%)
  [PASS] ATP_3-11.74-000: 103.89% (threshold >= 99%)
  [PASS] ATP_3-21.8-001: 101.29% (threshold >= 99%)
  [PASS] ATP_3-34.45-000: 103.12% (threshold >= 99%)
  [PASS] ATP_3-35-000: 102.73% (threshold >= 99%)
  [PASS] ATP_4-02.4-000: 101.37% (threshold >= 99%)
  [PASS] ATP_4-02.82-000: 118.66% (threshold >= 99%)
  [PASS] ATP_4-32.3-001: 108.28% (threshold >= 99%)
  [PASS] ATP_4-90.5-000: 102.24% (threshold >= 99%)
  [PASS] ATP_4-93-000: 102.52% (threshold >= 99%)
  [PASS] ATP_5-0.1-001: 102.33% (threshold >= 99%)
  [PASS] ATP_5-0.2-1-000: 104.10% (threshold >= 99%)
  [PASS] ATP_5-0x3: 107.72% (threshold >= 99%)
  [PASS] ATP_5-19-000: 102.25% (threshold >= 99%)
  [PASS] ATP_6-02.53-000: 105.01% (threshold >= 99%)
  [PASS] ATP_6-02.70-000: 105.42% (threshold >= 99%)
  [PASS] ATP_6-02x75: 104.53% (threshold >= 99%)
  [PASS] ATP_7-100.1-001: 101.19% (threshold >= 99%)
  [PASS] ATP_7-100.3-001: 101.42% (threshold >= 99%)
  [PASS] ATP_7-22.01-002: 103.94% (threshold >= 99%)
  [PASS] ATP_7-22.02-001: 110.50% (threshold >= 99%)

## 2. Leaked-artifact scan
  [PASS] 0 leaked-prompt hits, 0 chunks with (cid:) artifacts

## 3. doc_id format consistency
  [PASS] all doc_ids match ADP_X-Y / ATP_X-Y

## 3b. Font-encoding corruption (per document)
  [PASS] all 27 documents under 2% replacement chars

## 3c. Zero-chunk documents
  [PASS] every document produced at least one chunk

## 4. Known-enumeration regression tests
  [SKIP] regression: ADP 5-0 MDMP 7-step list: SKIPPED -- no chunks found for doc_id prefix 'ADP_5-0' (source PDF not yet processed in this run)
  [SKIP] regression: ADP 6-0 mission command 7 principles: SKIPPED -- no chunks found for doc_id prefix 'ADP_6-0' (source PDF not yet processed in this run)

## 5. Chunk token-count distribution
  [INFO] n=11444 min=8 median=169.0 max=8155 | 537 chunks (4.7%) exceed max_seq_length=512 (will be silently truncated by the dense embedder at query/index time -- flagged, not a failure by itself, since these are logged last-resort overflow units from unsplittable lists/tables)

## 6. Documented exclusions (manual -- not caught by an automated gate)

Same treatment as ADP-7-0 in the ADP build: a real, known gap that must stay
visible in the report rather than silently vanish from a count.

- **`ATP_4-02.82-000` is not usable content.** It passed every automated
  gate above (3 chunks, 118.66% preservation, no leaks, no encoding
  corruption) because gate 3c only fails on *zero* chunks. Inspecting the
  3 chunks directly shows all of it is an Army Publishing Directorate
  redirect notice ("This electronic document is located on another
  website... https://doctrine.navy.mil/"), not the actual ATP 4-02.82
  publication text. Needs a replacement source file, same as ADP-7-0.
  `pipeline/validate.py`'s zero-chunk gate does not generalize to this
  failure mode (nonzero-but-non-content); worth a follow-up check if this
  pattern recurs at full-corpus scale.
- **One ATP-3 series document is absent from the source download**
  entirely (89 of 90 expected ATP-3 series files present locally; see
  D:\Downloads\ATP-20260802T095321Z-1-001\ATP\ATP-3\). Filename not
  identified -- out of scope to chase down per current instructions. Not
  in this sample and not counted anywhere above; noted here so the gap
  stays visible rather than being invisible-by-omission from a report that
  only describes documents actually present.

Effective sample-content count: 26 of 27 documents usable, not 27 of 27.

## Summary: 32 passed, 0 failed, 2 skipped