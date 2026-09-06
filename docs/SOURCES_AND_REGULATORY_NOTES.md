# Sources, prior art, and regulatory context

Checked on 2026-09-06. These sources motivate a research question; they do not certify NF-SCI or validate the broader Dr.Nimad/ASI Trader system. This note replaces unverified promotional claims for the purposes of this public package.

## Prior art and the actual gap

| Primary source | Relevant precedent | Relationship to V1 |
|---|---|---|
| [in-toto](https://in-toto.io/) | Metadata describing software-supply-chain steps and integrity relationships | V1 is not an in-toto implementation or verified interoperability result. |
| [SLSA provenance](https://slsa.dev/provenance) | Verifiable information about how software artifacts were produced | V1 records fixed decision comparisons; it does not establish a SLSA level or authenticated build provenance. |
| [Reproducible Builds definition](https://reproducible-builds.org/docs/definition/) | Defined inputs, environment, and instructions can reproduce identical artifacts | V1 demonstrates deterministic decision replay, not the reproducibility of an entire AI stack. |
| [CoSAI: Signing ML Artifacts](https://github.com/cosai-oasis/ws1-supply-chain/blob/main/signing-ml-artifacts.md) | Signed claims tied to artifact and claimant identities, with consumer trust policies | AI provenance and auditability are already active fields. V1 has no signature-verification layer; a universal novelty or exclusivity claim would be unsupported. |

The proposed direction is to connect a small, inspectable decision record to existing authorization and evidence mechanisms. Whether that offers useful additional protection or lower integration cost must be measured. A fixed fixture validator, by itself, does not demonstrate that advantage.

## EU AI Act: corrections to the launch narrative

[The current consolidated AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727) must be read by applicable system category and provision:

- Article 12 concerns automatic records and traceability for high-risk systems. Paragraph 3 already specifies minimum records for a particular biometric-identification category; it is incorrect to say the law leaves all logging content blank.
- Articles 13 and 14 address information/transparency and human oversight. A six-case decision receipt does not establish fulfillment of those requirements.
- Article 43 includes internal-control conformity-assessment routes. Compliance is not exclusively something an outside certifier may declare. Conversely, a vendor's unsupported declaration does not establish conformity.
- Article 113 contains differentiated application dates. Do not advertise every high-risk obligation as applying universally today.

None of these provisions requires this product, SHA-256, or this capsule schema. This bundle makes no conformity finding.

## Standards status is not a blank slate

[CEN-CENELEC's July 2026 update](https://www.cencenelec.eu/news-events/news/2026/newsletter/ots-75-anec/) reports approval of EN 18286, an AI quality-management standard, while describing Official Journal citation as a further step. That does not establish this capsule's conformity or the status of every logging standard.

The [European Commission's standardisation page](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) distinguishes voluntary standards and the legal effect of cited harmonised standards. Do not equate a proposal, an approved standard, and an Official Journal citation.

## Korea

[AI Basic Act Article 34](https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810839) addresses specified responsibilities for high-impact AI, including risk management, explanation, user protection, human oversight, and preparation/retention of supporting documents. Applicability and implementing requirements require their own assessment. This capsule is not evidence that all of those responsibilities have been met.

## Public wording that matches the evidence

“We are publishing a small research capsule for reproducible admission-policy decisions. It exposes a frozen test set, ordered errors, byte identities, and reproduction receipts for inspection. We are investigating how such records could complement established provenance and authorization mechanisms.”

Changing “compliant” to “designed for compliance” or “대응” is not sufficient if the supporting implementation and applicability assessment are missing. Describe the implemented behavior first.

Avoid claims that all AI needs NF-SCI, that the project is the first or only solution, that an AI cannot start without authentic evidence, that three physical machines have been independently certified, or that big-tech adoption follows automatically from publication. None is established by this package.

## Positioning

An interoperable specification and an optional implementation/service business are a possible strategy. Adoption, licensing, governance, compatibility, and measured user value still have to be earned. Calling a private design a “law” does not give it legislative force or recognized certification authority.

No third-party article, system card, company logo, or institution name in these references implies endorsement. Unverified market sizes, incident counts, operating-duration claims, and trading-performance claims have been omitted.
