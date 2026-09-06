# NF-SCI — Reproducible Admission Decisions

A small Python research capsule for reviewing **six fixed admission-policy cases** through byte-identical JSON decisions and reproduction receipts.

V1 evaluates one accepted request and five rejected requests. It is a concrete, inspectable starting point for discussing how a policy decision should be recorded outside a language model. It contains no model weights, inference calls, trading system, or production actuator.

**Current result:** the supplied receipts agree with the frozen baseline. An additional assisted packaging run on 6 September 2026 reproduced all six cases, with exit code 0, empty stderr, and unchanged source files. That run's actual case outputs are included. See [evidence and provenance](EVIDENCE.md).

## Try the existing capsule

Inspect the [source](capsule/admission_core.py), [runner](capsule/capsule_runner.py), and [reproduction instructions](REPRODUCING.md). Use a fresh copy of `capsule/`. From that directory:

```sh
python3 -I -S capsule_runner.py verify
```

Successful verification prints `RESULT=True` and `RC=0`, and creates `CAPSULE_RECEIPT.json` plus six `case_outputs/*.json` files. Rejection is a decision inside a successful test; it is not identified by process exit status alone.

The original compressed capsule is **6,549 bytes**. Its exact tarball, detached checksum, and all twelve original files are included. The much larger public ZIP also carries documentation, evidence, and a short video.

## What the result means

| Demonstrated in this capsule | Outside the demonstrated scope |
|---|---|
| Fixed request-shape and policy checks | Authenticating a caller or authority issuer |
| Six deterministic decisions and ordered errors | Verifying the truth, signature, or freshness of referenced evidence |
| Hash comparison of capsule files and case outputs | Blocking an actual AI/tool action before its first effect |
| Reproduction against a frozen baseline | Whole-system security, legal conformity, autonomy, or model superiority |

Most request SHA fields are checked for **format**, not against referenced evidence files. One verb digest is compared with a built-in constant. Every decision, including the admitted case, reports `actuation_performed=false`. A hash identifies bytes; it does not establish that a claim is true.

## Review map

- [Five-clause descriptive specification](SPEC.md)
- [Claim card and limitations](CLAIMS.md)
- [Receipt comparison and attribution](EVIDENCE.md)
- [Prior art and regulatory context](docs/SOURCES_AND_REGULATORY_NOTES.md)
- [Video: evidence-review walkthrough](media/evidence-review-walkthrough.mp4) — edited, silent document walkthrough; see [editing notes](media/VIDEO_NOTES.md)
- [한국어 업로드 순서·배포 전략](START_HERE_KO.md)
- [License status](LICENSE_STATUS.md)

## Useful feedback

Can you reproduce the same six decision hashes in your environment? Which claimed property is narrower than the evidence provided? What concrete integration would make this useful alongside existing signing, provenance, and authorization systems?

The next stronger experiment would connect independently verified evidence to an existing tool's real effect boundary, including a denied path that leaves the protected target unchanged. That is a proposed next experiment, **not a V1 result**.

Packaging and explanatory documents were prepared with AI assistance. Original capsule and receipt bytes are preserved. This public-review bundle is not an adopted standard or a certification product; see the license status before downstream reuse.
