# Re-Judging

Apply [execution-modes.md](execution-modes.md) to context isolation, stage execution, and completeness. SINGLE-CONTEXT REVIEW can finish with an advisory verdict when all stages pass; it must remain explicitly labeled in reports and history. STRICT INDEPENDENT retains its delegation requirement.

Recognize follow-ups such as “what changed?”, “we got 82% accuracy”, “we changed the hardware”, “we removed the robot arm”, “we found a dataset”, “the professor changed the courses”, or “we built the first prototype”. Match the project using its explicit ID/name or unambiguous current context. Read its latest session, previous ruling, specialist reviews, and objection history. Do not use another project's history. If history is missing, say so and run a full council on the available proposal; do not invent a previous verdict.

Check session completeness before selecting Judge-only mode. If the latest session is INCOMPLETE, use the latest COMPLETE session only if its design is still applicable and all four accepted reviews and its ruling are available; also disclose and carry forward relevant evidence or unresolved defects from the incomplete attempt. Otherwise start a new full council with a fresh recorded attempt budget, linking the incomplete session. Do not automatically restart within the same invocation to evade retry limits. Without a completed earlier ruling, show no verdict transition and never invent a previous verdict.

Classify before dispatch:

- **EVIDENCE UPDATE:** new observations, measurements, access confirmation, or prototype results test the same design and objectives. An equivalent verified component substitution can fit here if it changes no scientific premise, interfaces, course requirements, or decisive constraints.
- **PROJECT PIVOT:** changes to objectives, architecture, methods, required courses, core hardware capability, dataset task/distribution, scope, or decisive time/resources invalidate earlier reviews. Run all five fresh agents sequentially on the revised normalized project, linking the previous history and preserving the original record. Believer still receives no prior opinions; later roles receive relevant prior objections along with their permitted current reviews.

For an evidence update, run only a new independent Academic Judge. Supply the full original normalized context, all four accepted prior reviews, exact previous Judge ruling, current objection ledger, and the accumulated evidence ledger from all applicable earlier updates plus the new evidence. Include the measurements, conditions, provenance, limits, acceptance thresholds, and referenced evidence artifacts supporting both resolved and unresolved objections; a prior verdict or status label alone is not evidence. Mark new, superseded, and contradicted observations explicitly. If earlier evidence is unavailable, label that gap and do not silently treat an earlier resolution as independently verified. Copy the common preamble and complete Judge section from agent-prompts.md, the complete verdict-policy.md, the relevant course-coverage.md standard when courses are required, and this extra prompt into its isolated dispatch:

```text
RE-JUDGE MODE: EVIDENCE UPDATE
PRIOR SESSION: [PRIOR SESSION]
PREVIOUS VERDICT: [PREVIOUS VERDICT]
PREVIOUS RULING: [PREVIOUS RULING]
PREVIOUS BIGGEST RISKS AND OBJECTION HISTORY: [OBJECTION HISTORY]
CUMULATIVE EVIDENCE AND AUTHORIZED ARTIFACTS: [CUMULATIVE EVIDENCE]
NEW EVIDENCE: [NEW EVIDENCE]

What changed? Did the evidence resolve the previous objection? Should the verdict
move? Answer these questions concisely inside WHY using the same required Judge
structure. Treat unchanged specialist reviews as historical, not new reviews.
Test whether the evidence addresses the same task, operating conditions, metrics,
and acceptance thresholds. Do not promote a verdict merely because a number
improved. Explain each objection you resolve, retain, mitigate, or reopen.
If the new facts invalidate the original design or previous specialist reasoning,
state PROJECT PIVOT REQUIRED in WHAT MUST CHANGE; the coordinator must obtain a
full fresh council before publishing a completed updated verdict.
```

Bind all additional bracketed tokens explicitly. A headline such as “82% accuracy” is student-reported evidence until its test set, sample count, split, baseline, conditions, and relevance are established. It need not trigger a questionnaire; record those limits and rule accordingly. A ten-sample demo is not a generalization study. A purchased sensor is not proof of full system reliability.

Track repeated unresolved objections by ID. Persistent failure to perform a promised critical validation reduces confidence in feasibility and must be addressed in the next ruling; repetition alone is not additional empirical evidence. Reopen resolved objections if contradictory data arrives. Apply the same Judge quality gates and one corrective retry. If a full rerun becomes necessary, mark the evidence-only attempt superseded and initiate a clearly labeled full evaluation; do not publish its provisional verdict as final.

Show the transition even when unchanged, such as `REFINE → REFINE`, followed by what changed and what remains unresolved. Save a new session and append an index entry; never replace the old decision.
