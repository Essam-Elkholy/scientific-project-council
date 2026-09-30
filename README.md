# Scientific Project Council

[![Quality checks](https://github.com/Essam-Elkholy/scientific-project-council/actions/workflows/checks.yml/badge.svg)](https://github.com/Essam-Elkholy/scientific-project-council/actions/workflows/checks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A modular Claude Code skill that evaluates whether a scientific or engineering project is meaningful, measurable, feasible, and worth implementing.

It supports university, seminar, PBL, graduation, engineering, research-prototype, and interdisciplinary projects. Five roles challenge the proposal sequentially, using independent contexts when available: **Believer → Skeptic → Domain Expert → Research Architect → Academic Judge**. The result is a decision and an evidence-based action plan, not automatic encouragement.

This is a scientific adaptation of **[Claude Council Khalifa](https://github.com/faroukahmed89-droid/claude-council-khalifa)** by **Farouk Ahmed**. The original reviews business ideas; this fork reviews academic projects. The upstream MIT copyright notice is preserved. See [credits and attribution](CREDITS.md).

## Features

- A short entrypoint with focused references for agent prompts, course coverage, verdict rules, quality control, re-judging, memory, and output templates.
- Strong distinctions between assumptions, student-reported results, inspected artifacts, and sourced facts.
- AUTO execution: fresh independent reviewers when available; a clearly disclosed single-context review otherwise. STRICT INDEPENDENT remains available on request.
- Honest APPROVE / REFINE / RESCOPE / RETHINK / REJECT decisions with explicit approval gates.
- Concrete course-coverage examples, including an FPGA image-processing example.
- A tested memory helper that retrieves the exact project and most recently saved session, including a separate latest-complete result.

All package documentation, descriptions, prompts, and examples are written in English. The council can still respond in English, Arabic, or Egyptian Arabic according to the student's input.

## Package structure

```text
skills/
  scientific-project-council/
    SKILL.md
    references/
      agent-prompts.md
      project-context.md
      verdict-policy.md
      quality-control.md
      course-coverage.md
      rejudge.md
      memory.md
      output-templates.md
    scripts/
      save_session.py
tests/
  test_sessions.py
README.md
```

The installable skill folder is self-contained. Its [entrypoint](skills/scientific-project-council/SKILL.md) routes to the complete prompts and operating rules. References are part of the skill and must be copied along with it. Tests and this README belong to the source package, not the runtime skill.

The complete [file guide](docs/FILE_GUIDE.md) explains every file, including the license, credits, tests, package builder, and quality workflow. The installable folder also includes its own copies of LICENSE and CREDITS.md so attribution stays with it when copied.

## Requirements

- A Claude environment that can load the skill and its references. Fresh-context delegation enables independent mode; otherwise AUTO uses five sequential stages in one conversation.
- Relevant project files and permission to read them.
- Web search/page inspection for current, verified prior-art research. Without it, the council can review supplied evidence and label the research limitations.
- Write access to the student project for persistent history. No-save and read-only workflows remain possible with explicitly unsaved transcripts.
- Python 3.9 or newer for the memory helper; it uses only the standard library. If Python is unavailable, a documented manual Markdown fallback is available.

A full evaluation runs five sequential reviewers and permits one corrective retry per role. An evidence-only re-judge usually runs one new Judge, with one corrective retry. Model usage depends on the host and the proposal. This is a prompt-driven review process, not a hard enforcement engine or a guarantee of academic correctness.

## Install in Claude Code

Choose one destination:

| Scope | Location |
| --- | --- |
| One project | `<project>/.claude/skills/scientific-project-council/` |
| All local projects | `~/.claude/skills/scientific-project-council/` |

Copy the entire `scientific-project-council` skill folder, including `references` and `scripts`, into that destination. Install this edition in place of the older edition, not alongside another skill with the same name. Preserve a backup before replacing an existing installed copy. Student history lives separately and should not be overwritten during installation.

Download [scientific-project-council.skill](scientific-project-council.skill), a ZIP-format archive with the complete skill folder at its root, including its license and credits. For local Claude Code installation, extract it and copy that folder into the location above. GitHub's source ZIP additionally contains the repository documentation and tests. Archive packaging does not itself activate the skill.

For Windows PowerShell, run from the source package directory and set the actual student project path:

```powershell
$studentProject = 'D:\Path\To\StudentProject'
$source = Join-Path (Get-Location) 'skills\scientific-project-council'
$parent = Join-Path $studentProject '.claude\skills'
$destination = Join-Path $parent 'scientific-project-council'
if (Test-Path -LiteralPath $destination) {
    throw 'A skill already exists here. Back it up and review before replacement.'
}
New-Item -ItemType Directory -Path $parent -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
```

For macOS/Linux, from the source package directory:

```bash
student_project='/path/to/student-project'
destination="$student_project/.claude/skills/scientific-project-council"
if [ -e "$destination" ]; then
  printf '%s\n' 'Back up and review the existing skill before replacement.'
else
  mkdir -p "$student_project/.claude/skills"
  cp -R skills/scientific-project-council "$destination"
fi
```

Use your home directory as the base for a personal installation. Start a new Claude Code session in the student project and invoke `/scientific-project-council`. Official platform references: [skills](https://code.claude.com/docs/en/skills) and [subagents](https://code.claude.com/docs/en/sub-agents).

## Usage

```text
/scientific-project-council

Evaluate an FPGA-based image-processing accelerator for an Electronics and
Communication seminar. We plan an enhancement stage and Sobel edge detection
on the FPGA, then transfer the output to Python. We want to investigate whether
it can support a separate tumor-localization method on a medical-image dataset.
The localization method, dataset, FPGA board, time, team, and exact course rubric
are not yet selected. Treat localization as an unproven objective. Challenge
whether this connection is justified and propose the smallest measurable project.
```

```text
pbl council: Four students, 12 weeks, a microcontroller, an accelerometer,
and a laptop. Required courses: Signal Processing, Embedded Systems, Statistics.
We propose a motor-vibration monitor and want to compare fault detection with
a simple threshold baseline. Help us define the contribution, experiments,
scope, course evidence, and first validation test.
```

```text
judge my project: We want to implement an autonomous drone, custom flight
controller, visual navigation, and mobile application in eight weeks.
We are two students and have no confirmed drone access. Should we pursue it?
```

Natural-language triggers include `scientific council:`, `project council:`, `pbl council:`, `judge my project:`, `evaluate my project:`, and equivalent Arabic requests. Automatic selection depends on the host; the slash command is explicit.

Missing facts become UNKNOWN, and assumptions are labeled. The council asks only when a missing fact fundamentally blocks evaluation or identifying the correct project. Course requirements and publication novelty are not invented.

## Roles and decisions

| Role | Responsibility |
| --- | --- |
| Believer | Strongest honest scientific case for the project |
| Skeptic | Strongest academic or technical failure case |
| Domain Expert | Verified prior-art comparison and defensible contribution |
| Research Architect | Achievable MVP, architecture, baseline, experiments, course mapping, and demo |
| Academic Judge | Resolve disagreements and make the final decision |

Later roles receive only their authorized earlier reviews. Each gets a new context; reviewers do not share the entire conversation. If delegation is unavailable, AUTO completes the five stages in one conversation and labels the advisory verdict SINGLE-CONTEXT REVIEW. Request STRICT INDEPENDENT to require separate contexts and stop when they are unavailable.

| Verdict | Meaning |
| --- | --- |
| APPROVE | Meaningful, measurable, feasible, and ready to implement |
| REFINE | Viable direction with specific scientific or course-integration weaknesses to repair |
| RESCOPE | Valuable core but excessive size, risk, or complexity |
| RETHINK | Fundamental direction needs redesign |
| REJECT | Do not pursue this direction under the established constraints and requirements |

Approval requires more than a polished demo. Supported critical objections, missing required outcomes, an absent baseline, unmeasurable results, or unavailable essential resources cannot be ignored. A rigorous finding that the proposal is unworkable can reach REJECT; it is not confused with an incomplete review.

Prior-art similarity is not an automatic rejection. Rigorous replication or a standard-method comparison may be valuable under a course rubric. A graduation label does not automatically impose publication novelty. Uncertain research findings remain uncertain.

## What the report contains

The verdict comes first, followed by the Judge's reasons, short specialist summaries, course coverage, actual student contribution, MVP, biggest risk, relevant previous work, first validation test, stop condition, recommended project definition, and action plan. Full role outputs remain in the saved transcript.

Implementation stages are Validation, Core Prototype, Integration, Experiments, and Final Demo. REFINE/RESCOPE plans first address required repairs; RETHINK/REJECT plans prioritize stopping or pivoting. No dates are invented.

## Memory and re-judging

Runtime history is created in the student project:

```text
scientific-council/
  council.md
  sessions/
    YYYY-MM-DD-project-id.md
    YYYY-MM-DD-project-id.json
```

The human index preserves previous entries. JSON metadata stores explicit project identity, save sequence, status, and summary fields. Same-day saves do not overwrite each other. Exact IDs prevent `motor` from matching `motor-controller`. Name ambiguity is reported, and the latest incomplete attempt is distinguished from the latest completed evaluation.

```text
project council: What changed for the FPGA image-processing project?
We have measured end-to-end latency including transfer overhead, compared the
RTL output against a software reference, and documented resource utilization.
Here are the artifacts and test conditions. Re-judge the previous objections.
```

An EVIDENCE UPDATE on the same design runs a new Judge using full historical reviews and new evidence. A PROJECT PIVOT that invalidates prior reviews runs all five roles again. Required-course changes trigger a full council. The report shows a supported transition, even if unchanged, and preserves the earlier decision. A bare accuracy number does not automatically resolve an objection.

Persistent unresolved objections weigh against feasibility, but repetition is not new empirical evidence. Legacy Markdown-only history is inspected manually rather than silently guessed. The [memory reference](skills/scientific-project-council/references/memory.md) documents saving, retrieval, metadata, fallback, and recovery.

## Validation

Run the regression suite from the source package:

```text
python -X utf8 -B -m unittest discover -s tests -v
python -X utf8 -B scripts/build_skill.py --check
```

The local regression suite checks session storage and packaging. The suite covers same-day recency, exact title and ID selection, ambiguous and renamed projects, incomplete sessions, backdated display dates, preservation of old entries, valid transitions and predecessor relationships, project-ID collisions, invalid metadata and paths, empty transcripts, legacy files, corrupt history, interrupted index publication, concurrent-save locks, and Unicode content.

Structural checks verify reference links, prompt preservation, English-only package text, Markdown fences, and the distributable archives. Independent manual review inspects role isolation, evidence flow, decision gates, and re-judge scenarios. Native end-to-end Claude Code execution is not verified in this environment. Script tests and prompt inspection do not establish that a model will always follow the workflow or reach the right academic judgment.

## Claude compatibility and execution modes

A skill provides instructions; uploading it does not add a subagent tool. AUTO detects the actual runtime: it uses separate reviewers when possible and otherwise completes the same five analytical stages in one conversation. Every fallback report and saved transcript must state SINGLE-CONTEXT REVIEW and label the verdict advisory. No independent executions are claimed.

Use `AUTO: evaluate this project` for the default behavior. Use `STRICT INDEPENDENT: evaluate this project` to require fresh reviewer contexts. See [execution modes](skills/scientific-project-council/references/execution-modes.md).

The provided 2026-09-30 runtime transcript stopped before all reviewers because the former instructions made delegation mandatory. The compatibility revision addresses that demonstrated instruction-level failure. Native execution in your Claude environment still needs verification; storage tests do not verify model behavior.

## Report style

Reviews use connected paragraphs rather than a numbered answer for every prompt question. Reports omit assumption/unknown inventories and unrequested assignments to individual students. Missing information is mentioned naturally only when it affects the judgment. The project evaluation still distinguishes proposed outcomes from observed results.
