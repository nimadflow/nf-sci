# V1 descriptive specification — five clauses

Scope: `ADMISSION_CORE_EXTERNAL_REPRODUCTION_V1`. This describes the shipped capsule; it does not define a general AI safety standard. The exact source and `MUST_MATCH.json` govern the six-case replay. Untested input combinations are not promoted to validated behavior by this document.

## 1. Request surface

The core accepts JSON through its existing command-line interface. The request schema label is `DRNIMAD_ACTUATION_REQUEST_V1`. Its fifteen required top-level keys are:

`schema`, `request_id`, `requester_uid`, `mission_ir_sha`, `body_selected_receipt_sha`, `route_proof_sha`, `verb_id`, `qualified_verb_sha`, `operand`, `expected_prestate_sha`, `effect_class`, `authority_class`, `exact_env_manifest_sha`, `timeout_ms`, `rollback_contract_sha`.

The operand has exactly `kind`, `locator`, `identity_sha256`, and `parent_identity_sha256`. Top-level forbidden, missing, and extra keys generate ordered errors before later validation. Exact conditions and error names are in `admission_core.py`.

## 2. Implemented policy checks

The core compares requester UID with a caller-supplied allowed value; the runner supplies `995`. This is value matching, not OS-credential authentication. Accepted authority text is `BLUE_NONMONETARY`. The two known verbs permit `APPEND_STATE`; monetary effect labels are rejected. `B3_PROBE_APPEND_V1` additionally requires the built-in verb digest. The timeout field must be an integer, excluding booleans, from 1 to 5,000. The locator is checked for absolute-path form and `..` segments, without opening its target.

Seven request SHA fields and two operand identity fields require lowercase 64-hex strings. Except for the pinned verb comparison, these checks do not resolve evidence, verify signatures, establish lineage, or prove freshness. The timeout field is a request constraint; it does not implement an actuator deadline.

## 3. Decision and effect boundary

The result schema is `DRNIMAD_ACTUATION_ADMISSION_RESULT_V1`, with `state`, `part_state`, `request_sha256`, `errors`, `actuation_performed`, and `monetary_authority_present`. An empty error list yields `ADMITTED`; otherwise `REJECTED`. The part state is `ADMISSION_ONLY__NO_ACTUATION`, and the final two flags are false.

The core writes a decision file, not the requested operation. Its successful exit can accompany either decision. No downstream caller consumes the decision to perform a protected operation in this capsule.

## 4. Byte-level identity

JSON encoding uses sorted keys, compact separators, UTF-8, and one trailing newline. Error order is significant. Request and decision hashes refer to these defined bytes. Output files are created exclusively; existing outputs are not overwritten by the runner. These properties provide a comparison basis, not identity authentication or tamper-proof storage against a privileged attacker.

## 5. Frozen replay

`capsule_runner.py verify` checks the manifest and runs PC plus NC1–NC5, then compares source, fixture, manifest, request, and decision identities with `MUST_MATCH.json`. The runner gives each core subprocess a 10-second timeout. Verification emits its receipt and six decision files.

The fixed `CORE_EXTERNAL_REPRODUCTION_N=0` field is retained for baseline equality. It is not a live count of worldwide reproductions. Passing the six cases establishes this fixed replay only; it does not validate arbitrary inputs, enforcement, rollback, or an entire system.
