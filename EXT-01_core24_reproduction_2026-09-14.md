# External Reproduction Record — EXT-01

Record ID: EXT-01
Bundle: core24-reproduce.zip
Date of run: 2026-09-14, between 21:01 and 21:10 KST (UTC+9), from screen timestamps; exact minute in the reproducer's report form
Record drafted: 2026-09-15

## Identity of the artifact

1. ZIP SHA-256: 0dff2c4430801030bb6de006975208a48f5033776d7a770ba48651b3b89b3864
2. Manifest SHA-256 passed to the verifier: 3c5c9cf893d88eeae292095334408c953e555c10f09f9974440770d3d067030f
3. Expected SHA-256 of the newly generated execution-01/CONTENT_RECEIPT.json, as declared inside the ZIP's README_REPRODUCE.md: 687c6ea8ac2e073ea93101e3a88647b4d49125beb11905ca9af2e0dc1ec7757e

## Reproducer and environment

1. Reproducer: external-01. A collaborator known to the maintainer. Identity withheld by mutual agreement.
2. Machine: the reproducer's own Windows PC. Not the maintainer's machine. No remote access by the maintainer at any point.
3. OS: Windows. The exact version string was not collected during the run and is not recorded here.
4. Python: 3.12.10 (tags/v3.12.10:0cc8128, Apr 8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32. Python was not present on the machine before this run and was installed for it. This is an environment change and is disclosed here.
5. Shell: Windows PowerShell, non-elevated.
6. Extraction: Expand-Archive into C:\core24test\run1. Top level after extraction: candidate/, reference/, FILES.sha256.json (7945 bytes), README_REPRODUCE.md (2376 bytes). Both files carry the fixed timestamp 1980-01-01 00:00 from the deterministic build.
7. Network: the verifier is documented as needing no network and is invoked with python -I -S -B. Network isolation was not independently measured on the reproducer's machine.

## Command and result

1. Command run, from C:\core24test\run1\candidate: python -I -S -B capsule_verify.py verify --manifest-sha256 3c5c9cf893d88eeae292095334408c953e555c10f09f9974440770d3d067030f
2. Final line printed: {"first_false": null, "measured_n": 24, "status": "PASS_REPRODUCED_PUBLIC_CORE24_ONLY", "unexecuted_n": 0}
3. Exit code ($LASTEXITCODE): 0
4. Get-FileHash of ..\execution-01\CONTENT_RECEIPT.json (SHA256): 687C6EA8AC2E073EA93101E3A88647B4D49125BEB11905CA9AF2E0DC1EC7757E
5. Comparison: all 64 hex characters match the expected value. The only difference is letter case, which is PowerShell's output format.
6. The generated receipt is therefore byte-identical to reference/CONTENT_RECEIPT.json shipped in the ZIP.
7. Successful executions: 1. The single-run rule of the guide was respected; execution-01 was created once and not re-run.

## Anomalies, recorded rather than removed

1. Python was absent before the run and was installed (3.12.10). See environment item 4.
2. The command line as it reached the reproducer contained capsule\_verify.py — a backslash before the underscore. Python failed twice with: can't open file 'C:\\core24test\\run1\\candidate\\capsule\\_verify.py': [Errno 2] No such file or directory. Once with python, once with py -3. Neither attempt opened the verifier, so neither created execution-01 or consumed the single-run claim.
3. The reproducer then listed the candidate directory (public, BUILD_INPUTS.json, capsule_verify.py, README_BUILD.md) and printed README_REPRODUCE.md from inside the ZIP, which states the command with capsule_verify.py. Running that exact line succeeded on the first try.
4. Classification: a distribution-path defect in the instruction text delivered outside the ZIP (a markdown-escaped underscore survived into plain text). Not a defect in the bundle, the verifier, or the README inside the ZIP. The maintainer's out-of-band instruction document is being corrected.

## What this record shows, and what it does not

1. Shows: the public core24 bundle, run on a second physical machine by a person other than the maintainer, produced a CONTENT_RECEIPT.json byte-identical to the shipped reference. Reported measured_n is 24 with unexecuted_n 0 and first_false null.
2. Does not show: independent reproduction by a stranger using only public materials. The reproducer received the ZIP and a written guide from the maintainer and could message the maintainer during the run. That stronger form of reproduction has not yet occurred and is not claimed.
3. Does not show: full32 qualification. Eight motor cases are withheld from the public bundle; the status string says PUBLIC_CORE24_ONLY.
4. Does not show: anything about NF-SCI as a whole, about trading, or about commercial fitness.
5. The 12 baseline matches and 12 mismatches recorded inside the receipt are the reproduction target — the shipped reference already contains them. They are not a newly measured detector score, and reproducing a mismatch is not baseline acceptance.
6. measured_n 24 is a count of observations in one bundle, not 24 independent samples.

## Evidence retained and not published

1. Retained on the reproducer's machine, untouched: C:\core24test\run1\ including execution-01\. That directory contains RESULT.json with local paths and timestamps.
2. Retained by the maintainer: six screenshots of the PowerShell session, including both failed launches; the reproducer's completed report form.
3. Not published: RESULT.json, stdout/stderr captures, the screenshots (they contain local paths and a messaging-app identity), the reproducer's name.

## Attestation basis

1. The maintainer reviewed the screenshots and the report form.
2. An AI reviewer (Claude, in an auditor role) read the same screenshots and drafted this record. That reading is not an execution and is not counted as an independent verification.
3. No party other than the reproducer ran the verifier for this record.

## Relation to other reproduction records

1. AI_SANDBOX_1 — 2026-09-12T22:24:46Z, an AI sandbox environment, byte-identical, exit code 0. A different execution environment class; counted separately, not merged with EXT-01.
2. A reproduction by the same collaborator on 2026-09-05 was of a different bundle (admission capsule v1, six fixed cases). It is a separate record for a separate artifact and is not merged into the core24 count.
3. Count after this record, for core24 only: local reproduction 1, AI sandbox 1, second human machine 1, stranger with public materials only 0.
