# Release v1.0.0-public-review — 2026-09-06

Scope: a fixed six-case admission-policy capsule (one admitted, five rejected) with byte-identical
JSON decisions and reproduction receipts. This is a research capsule, not the whole NF-SCI system,
not a model, not a production actuator. See CLAIMS.md for the claim ceiling.

Artifacts
- CAPSULE_V1_ADMISSION_CORE_EXTERNAL_REPRODUCTION_V1.tar.gz — 6549 bytes —
  SHA-256 6913e7858ec3eec01baafd4eff4f840fa7da19ef2f15538027c1620c6de99cea
- Public review ZIP (as originally packaged) — 11707265 bytes —
  SHA-256 f880192272f4eab98bfc8e098f1a91e960644e262c9e6f2220fa59eb13e6d275
- CAPSULE_RECEIPT.json (identical bytes from three environments: submitter, second reviewer, packaging QA) —
  4683 bytes — SHA-256 60d2f1cadd9ac7c2252f548539713e4a8033ed5e236440b39db8831946f78ab3

Reproduce: from a fresh copy of capsule/, run `python3 -I -S capsule_runner.py verify`.
Expected: RESULT=True, RC=0, empty stderr, CAPSULE_RECEIPT.json with the SHA above.

Licensing: code Apache-2.0 (LICENSE); documentation CC BY 4.0 (LICENSE-DOCS.md); trademarks not licensed (NOTICE).

Feedback wanted: reproductions with your environment string and receipt SHA; counterexamples where a
claimed property is narrower than the evidence; integration ideas alongside existing signing/provenance systems.
