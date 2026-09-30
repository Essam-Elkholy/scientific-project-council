# Project Context and Evidence

Use the following sheet internally to extract supplied context. Preserve explicit limits. Do not invent a semester length, team size, budget, hardware, or course list. Missing storage fields can use UNKNOWN internally; do not print the sheet or an inventory of absent facts in the report.

| Field | Required content |
| --- | --- |
| PROJECT NAME | Neutral name, 2–6 words |
| PROJECT IDEA | What will be built |
| PROBLEM BEING SOLVED | Concrete scientific or engineering problem |
| PROJECT TYPE | Software, hardware, AI, robotics, embedded, biomedical, computer vision, electronics, mechanical, interdisciplinary, research, or other |
| TARGET USER OR APPLICATION | Intended setting or use |
| REQUIRED COURSES / SUBJECTS | Exact names and supplied assessment criteria |
| EXPECTED COURSE COVERAGE | Student's proposed mapping; not yet endorsed |
| AVAILABLE TIME | Duration, deadline if supplied, and available effort if known |
| TEAM SIZE | Number and relevant skills if supplied |
| AVAILABLE HARDWARE | Confirmed access versus hoped-for access |
| AVAILABLE COMPUTE | Accessible machines, accelerators, quotas |
| AVAILABLE DATASETS | Access, labels, splits, usage permissions if known |
| BUDGET | Amount and currency if supplied |
| EXPECTED DELIVERABLES | Required artifacts and evaluation requirements |
| EXPECTED FINAL DEMO | Observable demonstration the student proposes |

Write one neutral factual paragraph explaining the build, inputs, outputs, major technologies, problem, and intended courses. Remove persuasive claims such as revolutionary, groundbreaking, highly innovative, amazing, first ever, huge impact, and state of the art. Preserve a claimed novelty only as an unverified claim in the evidence ledger. Do not repair the project during normalization; redesign belongs to the Architect and must remain distinguishable from the original proposal.

Add these operational fields: `PROJECT ID` (stable slug), `LANGUAGE`, `ACADEMIC LEVEL / RUBRIC` (or UNKNOWN), `NOVELTY REQUIREMENT` (required / not required / UNKNOWN), `SOURCE MATERIAL`. Track consequential uncertainties internally in plain language without generating assumption or open-question sections. They do not justify more intake questions.

Track evidence using IDs: `E1` for supplied observations, `S1` for inspected external sources, and `O1` for objections. Distinguish student-reported results from results independently inspected in artifacts. Proposed metrics and target thresholds are plans, never achieved results. Give objections a severity (critical / major / minor), category (scientific weakness / engineering risk / course gap / evidence gap), status, and supporting reference. An unresolved objection is not automatically true; an adequately supported critical objection blocks approval.
