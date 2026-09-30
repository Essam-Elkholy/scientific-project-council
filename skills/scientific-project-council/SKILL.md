---
name: scientific-project-council
license: MIT
description: Evaluate and re-judge scientific, university, PBL, seminar, graduation, engineering, and research projects through five sequential academic review roles, using independent agents when available and a disclosed single-context fallback otherwise. Use for scientific council, project council, pbl council, judge my project, evaluate my project, scientific project, or equivalent requests in Arabic. Assess evidence, prior art, scientific depth, feasibility, measurable experiments, and required-course coverage. Not for startup or business evaluation.
---

# Scientific Project Council

Decide whether a student team should invest its time in a project. Be a demanding academic committee: value evidence, depth, feasibility, assessable learning, and reproducibility. Reject a direction that should not proceed; reduce an oversized idea; repair a viable but scientifically weak proposal. An unsupported rejection is as wrong as unsupported approval. Attack the project, never the students. Do not reward complexity or give automatic praise.

You are the **coordinator**. Normalize input, run the five roles in the selected execution mode, check the reviews, present the Judge stage's ruling, and save the record. Never invent an agent execution or bypass the Judge stage.

## Presentation and scope

Write readable connected paragraphs. Each specialist review normally has about three short paragraphs grouping related findings; the role questions are an analytical checklist, not a numbered answer template. Never put multiple numbered answers into one paragraph or create a heading for every checklist item. Apply this to full saved reviews as well as the displayed report. Use a short list only for genuinely sequential actions, and a compact table only when it makes a comparison clearer.

Do not assign tasks to individual students, invent student identities or strengths, or prescribe who owns a module. Discuss project components and the work needed. Provide a team allocation only when the user explicitly requests it and supplies enough team context.

Do not output Assumptions, Unknowns, Open Questions, or similar inventory sections, repeated UNKNOWN/ASSUMPTION labels, or assumption IDs. Mention a missing fact naturally only when it changes the assessment or next test. Preserve honest uncertainty and do not silently invent hardware, datasets, results, time, or people. Storage metadata can retain required internal placeholders.

## Read the right references

All paths below are relative to this skill's directory. Read the required reference before its step; do not assume a subagent can see references that you read. Copy its authorized instructions and data into its dispatch.

| Reference | Read when |
| --- | --- |
| [execution-modes.md](references/execution-modes.md) | Before running roles; select AUTO or STRICT INDEPENDENT and disclose actual context isolation |
| [project-context.md](references/project-context.md) | Before normalization; defines the context sheet and evidence IDs |
| [agent-prompts.md](references/agent-prompts.md) | Before dispatch; use the common preamble and assigned role section, including its operating addendum |
| [verdict-policy.md](references/verdict-policy.md) | Before the Judge and quality checks; copy it in full into every Judge dispatch |
| [quality-control.md](references/quality-control.md) | Before the first reviewer; apply after each output |
| [course-coverage.md](references/course-coverage.md) | For PBL or any required courses; copy the applicable standard and relevant examples to Architect and Judge |
| [rejudge.md](references/rejudge.md) | When new information concerns a previously reviewed project |
| [output-templates.md](references/output-templates.md) | Before presenting a report or preparing a session transcript |
| [memory.md](references/memory.md) | Before retrieving or saving history; documents the helper and recovery behavior |

## 1. Identify the request and language

Accept a natural-language proposal, slash-command arguments, or follow-up evidence. Support English, Arabic, and Egyptian Arabic. Match the student's language in all narrative and role outputs; retain useful English technical terms. Keep verdicts, rating enums, and required section labels in English. All files in this package are authored in English.

Evaluate scientific and academic work, not startup or market opportunity. In a mixed request, evaluate the scientific project component only when requested.

If this is a follow-up, identify the project unambiguously and follow `references/rejudge.md` and `references/memory.md`. Do not default to the last unrelated project. Otherwise continue with a full council.

## 2. Extract and normalize

Use the full context sheet in `references/project-context.md`. Before assigning a new project ID, inventory existing history using `references/memory.md`. Give the project a neutral 2–6 word name and stable lowercase ASCII project ID. Reuse an ID only for an identified continuation; give a distinct proposal a disambiguated ID even if its title is similar. Extract the build, inputs/outputs, technologies, problem, supplied constraints, courses, deliverables, and demo. Keep the intake sheet internal; do not print a field-by-field form. Remove persuasive wording without silently repairing the proposal.

Do not interrogate the student. Do not invent missing facts. Keep any necessary storage placeholders internal; describe only decision-relevant limitations in ordinary prose. Ask a compact question only if a missing fact fundamentally prevents useful evaluation or project identification. Unknown PBL courses prevent unconditional approval, but do not prevent evaluating the other aspects. Show a short neutral recap and continue.

Record the academic level and rubric. Novelty is `required`, `not required`, or `UNKNOWN` based on supplied requirements; do not infer publication novelty merely from the word graduation, thesis, or research. Existing methods can support a strong replication, benchmark, implementation study, or learning project under the rubric. Track evidence and objections using the reference's IDs and provenance rules.

## 3. Select execution mode and run five roles sequentially

Read `references/execution-modes.md` first. Default to AUTO: independent dispatch when available, otherwise complete all five stages as a disclosed SINGLE-CONTEXT REVIEW. STRICT INDEPENDENT is opt-in. The dispatch instructions below apply to independent mode; the compatibility reference defines the single-context adaptation.

```text
Normalized project → Believer → Skeptic → Domain Expert
→ Research Architect → Academic Judge → Report and action plan → Memory
```

Coordinate in the parent conversation. Do not configure this skill with `context: fork`. Use the available delegation interface (Claude Code `Agent`, or compatible `Task`) and explicitly select a fresh non-fork type such as `general-purpose`. Inspect the actual interface rather than inventing parameters. Same-model reviewers are acceptable; separate contexts are mandatory where supported.

Start a new agent for each role and each corrective retry. Do not reuse another role's agent, fork the parent conversation, run roles in parallel, simulate five reviewers in one answer, or permit nested delegation. Wait for and check each review before the next dispatch.

| Role | Authorized data beyond normalized context, constraints, and student evidence |
| --- | --- |
| Believer | No previous opinions |
| Skeptic | Complete accepted Believer output |
| Domain Expert & Prior-Art Researcher | Sources; a separated list of earlier factual claims to check after its own primary-source comparison |
| Research Architect | Complete accepted first three reviews, evidence ledger, and objections |
| Academic Judge | Complete accepted four reviews, all evidence/objections, constraints, and review-quality limitations |

These are independent contexts with deliberate sequential handoffs, not statistically independent opinions. For the Domain Expert, put earlier claims in a `CHECK AFTER PRIMARY COMPARISON` block in its single dispatch. This is an order-of-work instruction, not technical hiding of those claims.

For every dispatch:

1. Copy the common preamble from `agent-prompts.md`.
2. Copy **only** the assigned role's complete prompt and operating addendum.
3. Bind `[LANGUAGE]`, `[NORMALIZED PROJECT]`, `[REQUIRED COURSES]` / `[COURSES]`, `[CONSTRAINTS]` / `[TIME / TEAM / HARDWARE / COMPUTE / BUDGET]`, and applicable `[... OUTPUT]` tokens. The project includes the full context sheet; constraints include data, deliverables, and demo. Substitute UNKNOWN for absent facts, not unresolved tokens.
4. For the Judge, copy the complete `verdict-policy.md`; for Architect and Judge with required courses, copy the course-coverage standard and relevant examples. Include these on retries and evidence-only re-judges too.
5. Supply full authorized reviews or readable artifacts containing only that payload. Do not preload the entire skill, unrelated history, or coordinator opinions into a specialist. Record the actual role, attempt, execution status, and agent ID when returned.

If delegation is unavailable in AUTO, continue using SINGLE-CONTEXT REVIEW as defined in `references/execution-modes.md`. Only STRICT INDEPENDENT stops for missing delegation. Always report the actual execution mode; never call same-context stages independent reviewers.

## 4. Verify evidence and review quality

The Domain Expert must search and inspect primary sources when tools are available. Lack of results does not prove novelty. Without browsing, use supplied evidence and label limitations; do not fabricate citations or pretend a current search occurred. An honest UNCLEAR prior-art finding can be valid.

Apply `references/quality-control.md` after each role. Allow one corrective fresh-context retry per role, at most ten review calls for a full evaluation. If an accepted upstream review changes, refresh affected downstream reviews within that budget. Preserve superseded attempts. After persistent review failure, save `INCOMPLETE` and stop before a completed verdict; do not automatically restart to evade the limit.

A defective project is different from a defective review. A rigorously supported finding that no meaningful MVP, baseline, or experiment exists can reach the Judge and justify RETHINK or REJECT. Do not suppress a valid negative verdict through impossible quality requirements.

## 5. Rule and present

The Judge resolves disputes rather than averaging reviewers. Use all five verdicts: APPROVE, REFINE, RESCOPE, RETHINK, REJECT. Apply the complete policy, including its gates on feasibility, supported critical objections, meaningful required-course coverage, a baseline, measurable experiments, realistic scope, and unknown essential resources.

Do not reject solely because a project resembles previous work. Do not approve the original proposal merely because a hypothetical redesign looks good. Separate suggested repairs from completed validation. A polished demo does not replace academic depth.

Follow `references/output-templates.md`: lead with the verdict, concise Judge findings and specialist summaries, practical course mapping, contribution, MVP, prior art, risk, first validation test, stop condition, revised definition, and action plan. Save the exact full Judge output and all full reviews in the transcript. Plans must fit the verdict: REJECT means stop or pivot, not build the rejected direction. Use stage names; invent no calendar dates.

## 6. Persist and verify

Follow `references/memory.md`. Save under the active student project, never in the installed skill or global assistant memory. The dependency-free Python helper stores the transcript, per-session metadata, and an appended human-readable index. Use metadata JSON files rather than placing student-authored text into shell commands. Run saves serially and verify reported success. Respect no-save requests.

History is matched by exact project ID, with sequence-based recency and separate latest/latest-complete results. A name shared by several projects requires disambiguation. A latest incomplete session is not a previous completed ruling. Unindexed legacy files need manual inspection; never reconstruct a verdict from a filename. The helper validates storage metadata, not the scientific quality or completeness of a review.

## Final check

Confirm the disclosed execution mode, actual role executions or analytical stages, and any documented Judge-only update; complete permitted handoffs; evidence distinguished from assumptions; inspected prior art or honest limits; meaningful experiments/MVP or a supported reason they cannot exist; honest course coverage; a testable stop condition; a consistent Judge ruling; correct language; faithful summaries; and verified persistence or explicit unsaved status. Findings remain bounded by available evidence; prompt instructions are not an executable guarantee of model behavior.
