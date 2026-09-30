# Output and Session Templates

Apply [execution-modes.md](execution-modes.md) to context isolation, stage execution, and completeness. SINGLE-CONTEXT REVIEW can finish with an advisory verdict when all stages pass; it must remain explicitly labeled in reports and history. STRICT INDEPENDENT retains its delegation requirement.

## Readability rules for every output

Use connected prose with blank lines between paragraphs. Each full specialist review normally groups its checklist into about three short paragraphs. Do not reproduce a long numbered checklist, concatenate items such as "1. ... 2. ... 3. ..." in a single paragraph, or add a subsection per question. A short specialist summary can remain one paragraph. Avoid decorative horizontal rules and unnecessary headings. Use lists for concise action steps and tables for useful comparisons only.

Do not generate individual student assignments or Assumptions/Unknowns/Open Questions sections. Explain consequential missing information naturally where it affects the judgment. Keep evidence traceability in the saved record, without repeated administrative labels in the displayed report.

## User-facing report

Lead with the verdict and keep specialist summaries to 2–4 sentences each. The template below is a content guide, not a demand to print every heading: combine related findings, omit irrelevant or empty sections, and show Course Coverage only when actual course requirements are supplied or course assessment is requested. Narrative follows the student's language; labels remain English. Show the Judge's decisive findings without printing every full specialist review. Preserve its exact full output in the transcript. Summaries must not erase disagreement or uncertainty.

```markdown
# Scientific Project Council

## VERDICT: <VERDICT>

<ONE-LINE RULING and WHY, faithfully summarized from the accepted Judge.>
<For re-judging: previous → current, what changed, and what remains unresolved.>

Scientific value: <rating> | Novelty: <rating> | Feasibility: <rating>
Measurability: <rating> | Demo potential: <rating>

STRONGEST ARGUMENT: <agent, argument, reason>
WEAKEST ARGUMENT: <agent, argument, reason>
WHAT MUST CHANGE: <minimum required repairs before implementation>

### Believer
<Strongest honest scientific case.>

### Skeptic
<Killer objection, whether it survived, and why.>

### Domain Expert
<Closest inspected work with links, classification, and research limitations.>

### Research Architect
<MVP, biggest technical risk, and proposed repair.>

## Course Coverage
<Course | Component | Concept | Project work / assessable evidence | Rating>

## Scientific Contribution
<What students build, analyze, compare, or discover beyond reused components.>

## Minimum Viable Project
<Concrete scope; CORE FEATURES, STRETCH GOALS, DO NOT BUILD.>

## Biggest Risk
<Evidence, objection ID/status, and fallback.>

## Previous Work
<Direct source links, similarities/differences, and effect on contribution.>

## First Validation Test
<Action, metric, test conditions, justified threshold, and STOP CONDITION.>

## Recommended Final Project Definition
<Judge's strongest realistic academic project statement.>

## Action Plan
<Ordered actions with deliverable, dependency, and exit criterion.>

Full transcript: <link to the saved session, or explicit unsaved status>
Execution: <actual independent role runs or Judge-only update; search limits>
```

Do not repeat paragraphs across sections. An action plan for APPROVE uses Stage 1 — Validation, Stage 2 — Core Prototype, Stage 3 — Integration, Stage 4 — Experiments, and Stage 5 — Final Demo. For REFINE or RESCOPE, required repairs come first and implementation is conditional. For RETHINK or REJECT, recommend stopping or pivoting and identify any justified salvageable core; do not recommend implementing the rejected direction. Do not invent dates or team assignments.

For an incomplete run, lead with `COUNCIL INCOMPLETE` or `INDEPENDENT COUNCIL UNAVAILABLE`, identify the missing reviews or quality blockers, and give the next action and partial-transcript link. Do not use a completed-verdict template. If no-save was requested, state that status.

## Full session transcript

Use this Markdown layout; add detail needed to retain all evidence. The metadata sidecar described in `memory.md` must match the accepted ruling.

```markdown
# <Project Name> — Council Session <local date>

PROJECT ID: <stable ID>
DATE / TIME / TIMEZONE: <actual values>
MODE: <FULL COUNCIL / EVIDENCE UPDATE / PROJECT PIVOT>
STATUS: <COMPLETE / INCOMPLETE>
LANGUAGE: <student language>
PREVIOUS SESSION: <link, or NONE>
EXECUTION: <actual delegation capability, role IDs/statuses, browsing capability>

## Original Proposal
<Student's proposal, excluding unrelated private details.>

## Normalized Project and Context
<Two or three readable paragraphs covering the project and supplied decision-relevant context; do not print the internal intake form.>

## Constraints and Required Courses
<Explicit limits, course names and rubric, expected coverage.>

## Evidence and Previous Work
<Cumulative evidence ledger, with new/superseded observations marked, provenance,
source IDs, authorized evidence artifacts, measurement conditions, and search limits.>

## Change Classification
<New council or evidence/pivot rationale; what changed since the last session.>

## Believer
<Full review in readable paragraphs, followed by compact execution metadata; or explicit NOT RUN / FAILED / REUSED link.>

## Skeptic
<Full output and attempt metadata, or explicit status.>

## Domain Expert
<Full output, source table, and attempt metadata, or explicit status.>

## Research Architect
<Full output and attempt metadata, or explicit status.>

## Quality Control
<Defects, superseded complete attempts, selected outputs, unresolved limitations.>

## Academic Judge
<Complete Judge findings grouped under a few useful headings with readable paragraphs; or NOT RUN / FAILED.>

## Objection Ledger
<ID | Category | Severity | First raised | Unresolved review count | Latest evidence | Status>
<Status: OPEN / MITIGATED / RESOLVED / REOPENED>

## Decision and Validation
<Verdict/transition, biggest risk, prior-art classification, MVP, course coverage,
first validation test, justified threshold, stop condition, and validation status.>

## Action Plan
<Ordered steps, deliverables, dependencies, and exit criteria.>

## User-Facing Report
<Link to a separate report if one exists, or note that the findings above were presented to the student. Do not duplicate the entire report inside the same transcript.>
```

Record the full substantive conclusions and their supporting evidence, not repeated summaries or private chain-of-thought. Length should follow the complexity of the project; do not pad the Markdown file to satisfy every example heading. A reused review must be linked or copied in full and explicitly labeled `REUSED — NOT RERUN`; do not imply a new independent execution. Preserve superseded attempts so the final Judge's evidence can be traced.
