CAPSULE_V1 ADMISSION-CORE EXTERNAL REPRODUCTION

1. Verify the detached tar.gz SHA256 declaration.
2. Extract only into a newly created empty directory; reject absolute paths, '..', links, devices, and duplicate members.
3. Verify every MANIFEST.json record by relative path, SHA256, and byte count.
4. Run: python3 -I -S capsule_runner.py verify
5. Return CAPSULE_RECEIPT.json without promoting it to truth or mutating any live system.

The runner invokes only admission_core.py. It does not test or reproduce genotype, body, dialogue, autonomous loops, services, network access, or trading.
