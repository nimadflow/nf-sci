# Claim card

Version: public review of the unchanged V1 capsule, 2026-09-06.

**Supported public description:** “A reproducible six-case admission-policy capsule with frozen inputs, ordered decisions, file hashes, and comparison receipts.”

| Claim | Evidence and ceiling |
|---|---|
| The original tarball is 6,549 bytes | Direct byte count; its SHA is in `artifacts/` and `PACKAGE_MANIFEST.json`. This is not the size of the video/document ZIP. |
| The fixed cases reproduce | Original submitted receipts match the baseline. Packaging QA also produced matching case-output bytes. See `EVIDENCE.md`. |
| Receipt copies are identical | Direct byte comparison; duplicate receipt contents do not prove distinct machines or independent people. |
| The capsule performs no requested actuation | Source inspection and six-case output flags. It writes its own local result files. |
| SHA-bound bytes are comparable | Capsule identities are verified; most evidence references inside requests receive only format checks. |
| Whole-body AI integration, refusal propagation, recovery, and continuous self-improvement | Not demonstrated by this capsule. |
| Three independently attested physical machines | Not established. Environment descriptions are submitted reports, not hardware attestations. |
| A trusted caller, signed authority, authentic/fresh evidence, or immutable logs | Not established by request strings or plain SHA-256. |
| EU/Korean legal compliance, certification, adoption as a standard | Not established. Regulatory context is research motivation only. |
| First in the world, necessary for all AI, impossible to bypass, or superior to frontier models | Not established. |
| Trading readiness, positive expected value, or authorization to use capital | Not evaluated or granted. |

## Threat-model boundary

The bundled Python interpreter, runner, source files, fixed oracle, host, and initial archive digest are part of the trust base. A party able to replace both artifacts and their expected hashes can replace the comparison basis. SHA-256 alone does not identify the issuer, validate evidence semantics, or establish that the host ran the code shown.

The runner checks its declared files and preserves ordered results. This is not a proof that all adversarial inputs are safely handled, nor an OS sandbox. Source `timeout_ms` and permission-shaped fields are not independently enforced authority.

## Stronger evidence to pursue

Use an already authorized, existing nonmonetary tool path. Show the same entrypoint accepting a valid case and consuming a rejection before the first protected effect; retain actual pre/post target identities and raw outputs. Then test a stale or substituted evidence reference, not just a missing or malformed field. Compare the incremental value with an existing policy/provenance workflow.

Success metrics for that future work: external reproductions with traceable inputs, confirmed counterexamples resolved, measured integration cost, and observed effect-boundary behavior. Stars, model praise, a video, and policy declarations are not substitutes.

No new runtime, execution harness, model, or production integration was authored for this public package.
