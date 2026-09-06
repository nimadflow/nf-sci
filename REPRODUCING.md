# Reproduce the unchanged capsule

This is a local, fixed-fixture replay using Python's standard library. Inspect the code before running it. Packaging QA observed Python 3.12.13 on Linux; the supplied environment reports describe additional Python versions. They are not a portability guarantee for every interpreter or OS.

## 1. Verify the package you received

Compare the outer ZIP's SHA-256 with the value published by the distributor through a channel you trust. After extraction, compare files with root `SHA256SUMS`. A checksum from the same untrusted download establishes consistency, not publisher authenticity.

The original compressed capsule is retained in `artifacts/`:

```text
CAPSULE_V1_ADMISSION_CORE_EXTERNAL_REPRODUCTION_V1.tar.gz
bytes: 6549
SHA256: 6913e7858ec3eec01baafd4eff4f840fa7da19ef2f15538027c1620c6de99cea
```

`capsule/` contains the twelve byte-identical extracted files. `capsule/MANIFEST.json` binds ten payload files; its own hash and the other comparison identities are in `capsule/MUST_MATCH.json`. The outer package manifest includes all original file hashes.

## 2. Use a fresh directory

Make a fresh working copy of `capsule/` and open a terminal in it. Keep the downloaded copy intact. Do not run from the repository root, and do not place extra executable/source files inside the capsule directory.

The only invocation needed is the existing verifier:

```sh
python3 -I -S capsule_runner.py verify
```

It creates `case_outputs/` and `CAPSULE_RECEIPT.json`. The runner intentionally refuses pre-existing outputs. For a later independent run, use another fresh copy; do not modify `MUST_MATCH.json` or use `record` to turn a mismatch into a pass.

Python `-I -S` is not an OS sandbox. This verifier does not establish network isolation or protection from a malicious host. No network or model call is needed by the inspected V1 code.

## 3. Read the result at the right level

Successful verifier stdout:

```text
RESULT=True
RC=0
```

Check the process return code, stderr, receipt, and actual output hashes together. PC should be admitted. NC1–NC5 should be rejected with the exact ordered errors in `MUST_MATCH.json`. Both decisions are admission-only and perform no requested action.

Expected receipt SHA-256 for the fixed verification output:

```text
60d2f1cadd9ac7c2252f548539713e4a8033ed5e236440b39db8831946f78ab3
```

This hash is a reproducibility target, not a unique run identifier.

## 4. A useful reproduction report

Preserve the exact capsule digest, unmodified receipt, all six raw decision files, stdout, stderr, exit status, command, Python/OS versions, and a run timestamp in a separate evidence directory. State which environment details were observed and which were merely reported. Remove unnecessary personal paths before publishing an environment summary and label any derivative.

Do not label a mismatch as a pass. Report the first differing file/property and its actual bytes/hash. An independent report should be attributable to its real submitter; it must not be presented as a vendor endorsement.

No external run is required merely to download or inspect this package. Running the capsule grants no deployment, trading, or production authority.
