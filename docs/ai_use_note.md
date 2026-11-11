# AI use note (draft)

Status: **draft written from the repository history; attribution wording confirmed by the Product Owner on 12 Nov 2026 on behalf of the Ethics and Privacy Officer (Dương Minh Chính), who may still amend it.** Anything marked "confirm" needs the person named to check it against what they actually did.

## Tools

Claude (Anthropic) was used as a coding and writing assistant by members of the team. The BRFSS data are public CDC data; no personal data were involved. The Product Owner confirms that nothing private (passwords, tokens, personal information) was pasted into the tool in his own use; each other member confirms the same for their own use.

## What AI assistance was used for

| Area | Use | Checked by |
|---|---|---|
| Scripts and dictionary (`scripts/`, `docs/variable_dictionary.*`) | Drafting the verification and build scripts and the variable dictionary | Results compared with the CDC codebook and run locally; output in `docs/source_verification.json` (Bảo, confirm) |
| D2 notebook (`notebooks/02_...`) | Drafting code and wording for profiling, cleaning log and the five data manipulations | Numbers re-checked against the CSV outputs in `docs/d2_outputs/` and the clean dataset (Dũng, confirm) |
| D3 notebook (`notebooks/03_...`) | Drafting helper functions for survey-weighted estimates and the candidate table | Outputs reviewed against `docs/d3_outputs/`; **no independent cross-check against a survey package is recorded** (Phương, confirm) |
| Repository documentation (`README.md`, `data/README.md`) | Drafting and tightening text, consistency checks across files | Figures taken from the CSV outputs; reviewed by the product owner (Dũng) |

## What AI assistance was not used for

* Choosing the decision question, the risk-factor definitions or the priority-group thresholds: these belong to the team; the thresholds are the product owner's decision.
* Interpreting results as causal. All findings are descriptive.
* Handling personal data: the public BRFSS file has no direct identifiers, and no attempt was made to identify respondents.

## Responsibility

Team members are responsible for every number and sentence they submit. AI-generated code or text was run, read and checked before use, and errors found were corrected by the team. The final report must repeat this statement in its own wording.

## To complete before D4

* Each member adds or corrects the rows above for their own part.
* The Ethics and Privacy Officer reviews the attribution wording in `data/README.md`, section 4, and signs off this note (the Product Owner confirmed the wording on 12 Nov 2026 in the meantime).
