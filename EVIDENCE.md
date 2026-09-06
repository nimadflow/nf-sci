# Evidence and provenance

Scope: the fixed V1 admission core. This document was prepared with AI assistance on 2026-09-06. It distinguishes inspected bytes, submitted environment reports, and the new packaging run.

## Evidence sources

| Source | What was inspected | What it establishes |
|---|---|---|
| Original capsule distribution | 7,117-byte source ZIP; 6,549-byte tarball; all twelve tar members; ten payload manifest records | Identity of the frozen program, fixtures, and baseline. The baseline is not itself an independent execution. |
| Seonghyeok result submission | Original 10,994-byte result ZIP, its receipt and collection logs | Submitted receipt agrees with the baseline. Its environment is reported in source logs, not remotely attested. |
| Attached run1 / run2 receipts | Two byte-identical 4,683-byte receipt files | Their identical content does not establish two distinct devices. |
| Mythos report | Original 4,056-byte report and its six case comparisons | Reports two runs in a vendor sandbox. Network and physical-environment claims were not independently measured here. |
| Assisted packaging QA | One invocation of the existing verifier in a fresh local copy; actual six output files retained | This packaging environment reproduced the six outputs. It is not an independent user reproduction or vendor certification. |

The original Seonghyeok result contains 25 regular files. Its ten `.stderr` files are empty, and `run.stdout` contains 17 bytes. Its collection summary says `REVIEW_REQUIRED`; that historical value has not been edited. The public bundle includes five selected, byte-identical evidence items and a labeled environment excerpt. The complete source result ZIP, raw user/host paths, and redundant presentation logs are not redistributed here.

The original Seonghyeok ZIP does **not** include individual `case_outputs/*.json`. Those original outputs cannot be independently byte-checked from that submission. The outputs in `evidence/packaging_qa/case_outputs/` are from the new packaging run; they are not replacements represented as Seonghyeok's files.

## Reported environments and observed packaging environment

| Record | Environment | Attribution |
|---|---|---|
| Seonghyeok source logs | Ubuntu 26.04 LTS; Python 3.14.4; WSL2 kernel 6.18.33.2; collection starts 2026-09-05T11:57:34Z | Reported by submitted logs. The launcher explicitly did not enforce OS containment. |
| Mythos receipt | Ubuntu 24.04.4; Python 3.12.3; vendor-sandbox kernel 6.18.44-fc-v24; reports two runs at 2026-09-05T17:58:07Z and disabled network | Statements in the supplied receipt; not independent hardware/network attestation. |
| Packaging QA | Linux x86_64; Python 3.12.13; kernel 6.18.35; one run on 2026-09-06 | Measured by the packaging process; detailed timestamps in `evidence/packaging_qa/QA_RECORD.json`. |

Mythos's historical report says the raw Seonghyeok ZIP was not supplied to that reviewer. This packaging review did obtain it and compared its receipt directly. The original report remains unchanged. Its suggested future inclusion of output hashes should not imply that V1 lacks decision hashes: V1 already records them. Retaining the raw case outputs and environment provenance is a distinct improvement.

## Exact six-case comparison

| Case | State | Ordered errors | Decision SHA-256 |
|---|---|---|---|
| PC | ADMITTED | none | `9f1755f80f4ef6ceab20a760aa7cdd4f956b5b101faf0b7993ed31492970f3ef` |
| NC1 | REJECTED | FORBIDDEN_KEYS:shell; EXTRA_KEYS:shell | `ff01e3a9c11a5d7a359bf103bf884f1fa59922900bbdd5c42900e5cf0d987852` |
| NC2 | REJECTED | REQUESTER_UID | `7efe823c4efaba46762366f5b71a9892b3f1113c01ae41d67271fa5205670d76` |
| NC3 | REJECTED | MONETARY_EFFECT_FORBIDDEN; VERB_EFFECT_MISMATCH | `47323b6dea689506ad01be3924ee7b75e0ea657ae1b3d735e75e7d574a80bc05` |
| NC4 | REJECTED | QUALIFIED_VERB_SHA | `e7ea896e449719e16830e4d57fdce4cc786af5156f40b98c544d8680e3bab12e` |
| NC5 | REJECTED | MISSING_KEYS:rollback_contract_sha | `6ace1b4f5f8dc93871b4a38ae06507b3e599ce502374eeab2f46fc9a4ce0028f` |

Every packaging-QA output hash matches the corresponding frozen value. Original submitted receipts report the same values. All six outputs state admission-only, no actuation, and no monetary authority.

## Identity anchors

| Artifact | SHA-256 |
|---|---|
| Original distribution ZIP, retained as an input outside this bundle | `fb81963c53d43dbf3975d076997458b9120d85f5a906f09163e635a8523c086b` |
| Original capsule tarball, included | `6913e7858ec3eec01baafd4eff4f840fa7da19ef2f15538027c1620c6de99cea` |
| Original Seonghyeok result ZIP, selectively excerpted | `d0a2d0ceb86c66cb38f107fb4609cf6f0251bf02ffe6fd9b740b20f25909359b` |
| run1, run2, Seonghyeok receipt, packaging-QA receipt | `60d2f1cadd9ac7c2252f548539713e4a8033ed5e236440b39db8831946f78ab3` |
| Original Mythos report | `99395c9d102a598fc432543226612c7ae2c2dae577ca9db7c0250f2cca78abe3` |

Identical receipts deliberately omit many environment-dependent details. Counting their filenames is not a method for counting independent executions, people, or physical machines. No worldwide reproduction total is asserted.

## Packaging verification

Existing command: `python3 -I -S capsule_runner.py verify`. Invocation count: one. Return code: 0. Stdout: 17 bytes. Stderr: 0 bytes. All twelve original files remained unchanged. All ten payload manifest records matched. No new runner, runtime, or harness was written.

The run used a separate local working directory. OS containment and network isolation were not established by this invocation. No production system was connected or acted upon. This checks the contents being distributed; it does not grant production authority or repair a runtime outside the capsule.
