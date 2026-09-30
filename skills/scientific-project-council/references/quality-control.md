# Quality Control and Bounded Repair

Apply [execution-modes.md](execution-modes.md) to context isolation, stage execution, and completeness. SINGLE-CONTEXT REVIEW can finish with an advisory verdict when all stages pass; it must remain explicitly labeled in reports and history. STRICT INDEPENDENT retains its delegation requirement.

Inspect each specialist before the next role and inspect the Judge before publication. Check substance, source support, and consistency, not just the presence of headings. Keep a quality-control log with defects, reruns, selected attempt, and unresolved limitations. Do not rewrite an agent's opinion to create consensus.

| Role | Reasons to rerun |
| --- | --- |
| Believer | Generic encouragement, unsupported certainty, missing success assumptions, criticism replacing advocacy, or an unrealistic best case |
| Skeptic | Gentle praise instead of adversarial analysis, no concrete failure mechanism, no strongest rejection case, no examination of Believer's central claim |
| Domain Expert | Available research tools unused, previous-work claims without inspected sources when sources are accessible, invented references, or novelty asserted without comparison |
| Research Architect | No real baseline, no measurable experiment, vague course mapping, unrealistic scope, missing critical-path test/fallback, or a system that needs every risky part to work |
| Academic Judge | APPROVE despite unresolved major objections with no adequate disposition, LOW feasibility, missing required outcomes, inconsistency between verdict and reasons, oversized MVP, or missing required sections |

Distinguish a defective review from a defective project. When the Architect finds no defensible baseline or measurable experiment, request the corrective review to check whether a meaningful reduced version is possible. If the corrected review rigorously explains why none is possible under the fixed requirements, accept that as a valid negative finding and pass it to the Judge for RETHINK or REJECT. Do not mark the council incomplete simply because the project itself is infeasible or scientifically unsound. Incompleteness means missing or unreliable review evidence, not an unfavorable finding.

For a weak Skeptic rerun append exactly: “Your previous review was too gentle. Find the strongest reason this project could fail academically or technically.” Also identify the concrete missing analysis; do not demand a false fatal flaw if a rigorous review found none.

Start the replacement in a fresh context with its authorized payload and a short correction request; mark the old attempt superseded. Allow one corrective rerun per role per evaluation (at most ten review calls for a full run). A timeout or missing output counts as an attempt. If a role remains incomplete or unsupported after repair, mark the council `INCOMPLETE`, persist the limitation, and do not present a completed verdict. Do not coerce a desired verdict through retries. Limited browsing with an honest UNCLEAR comparison can be a valid review; fabricated sources cannot.

If a later check invalidates an upstream claim, correct the relevant review and refresh affected downstream roles before finalizing; do not reuse a Judge that ruled on superseded evidence. Respect the same attempt budget. If refreshing would exceed it, save an incomplete session with the next required step rather than loop indefinitely. Preserve all attempts in the transcript.

## Presentation check

Before accepting or saving a review, split any dense paragraph containing multiple numbered checklist answers into coherent paragraphs. Remove unrequested individual student assignments and assumption/unknown inventories. Preserve the technical findings, meaningful uncertainty, and evidence; this is an editorial correction, not a new substantive review. Apply the same check to displayed summaries and saved transcripts.
