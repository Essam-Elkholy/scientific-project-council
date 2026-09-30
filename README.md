# Scientific Project Council

[![Quality checks](https://github.com/Essam-Elkholy/scientific-project-council/actions/workflows/checks.yml/badge.svg)](https://github.com/Essam-Elkholy/scientific-project-council/actions/workflows/checks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A skill that evaluates whether a scientific or engineering project is meaningful, measurable, feasible, and worth implementing.

It supports university, seminar, PBL, graduation, and research projects. Four reviewers examine the proposal, then an **Academic Judge** makes the final decision: **Believer → Skeptic → Domain Expert → Research Architect → Academic Judge**.

This is a scientific adaptation of **[Claude Council Khalifa](https://github.com/faroukahmed89-droid/claude-council-khalifa)** by **Farouk Ahmed**. The original reviews business ideas; this fork reviews academic projects. The upstream MIT copyright notice is preserved. See [credits and attribution](CREDITS.md).

## What it does

The council examines scientific value, relevant previous work, technical risks, achievable scope, measurable experiments, and required-course coverage. Its report explains the decision, the strongest arguments, necessary changes, and a practical first validation test.

Reports use readable paragraphs and useful headings. They omit administrative filler, assumption inventories, and unrequested assignments to individual students. The response follows your language, including Arabic or Egyptian Arabic with English scientific terms.

When separate agents are available, reviewers run in fresh contexts. Otherwise, the skill completes the five stages in one conversation and clearly labels the judgment **SINGLE-CONTEXT REVIEW**. You can request **STRICT INDEPENDENT** if separate reviewer contexts are essential.

## Get started in Codex

Download [scientific-project-council.skill](scientific-project-council.skill) and give Codex access to the downloaded file. Ask: **"Install Scientific Project Council from this file for me."** Codex can unpack and install the skill; you do not need to type terminal commands.

Once installed, start your next message with **`$scientific-project-council`**, followed by your project idea.

## Get started in Claude

1. Download [scientific-project-council.skill](scientific-project-council.skill).
2. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**, upload the package, and enable it.
3. Start a conversation, ask Claude to use **Scientific Project Council**, and describe your project.

The `.skill` package is already a ZIP archive containing the complete skill. If the upload picker requires a `.zip` extension, rename the downloaded file to `scientific-project-council.zip`; its contents stay the same. See [Claude's upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

No terminal commands or repository download are needed for this upload workflow.

## Example

> Use Scientific Project Council to evaluate an FPGA image-enhancement and Sobel edge-detection project for an Electronics and Communication seminar. We plan to send the output to Python and investigate tumor localization. Assess the scientific value, realistic scope, relevant previous work, and the first experiment we should run.

Include your time, resources, dataset, or required courses if you know them. Missing details are mentioned only when they affect the assessment; they are not invented.

## Decisions

| Verdict | Meaning |
| --- | --- |
| APPROVE | Ready to implement under the supplied constraints |
| REFINE | Keep the direction and repair specific weaknesses |
| RESCOPE | Keep the valuable core and reduce scope |
| RETHINK | Redesign the fundamental approach |
| REJECT | Do not pursue the proposed direction |

The Judge resolves disagreements using evidence rather than averaging opinions. A polished demo does not replace a baseline, measurable experiments, or meaningful academic work. Similarity to previous work does not automatically disqualify a rigorous implementation or comparison project.

When saved history is available, you can supply new measurements and ask for re-judging. The council preserves the earlier decision and explains what changed.

## Documentation and license

[File guide](docs/FILE_GUIDE.md) explains the repository. [Quality checks](docs/QUALITY.md) describes validation and its limits. [Contributing](CONTRIBUTING.md) covers development. [Optional local installation](docs/INSTALLATION.md) is for Claude Code users.

Released under the [MIT License](LICENSE). The original copyright notice belongs to **faroukahmed89-droid**; the scientific adaptation and additions are credited to **Essam-Elkholy**. Keep both notices and the license when redistributing the skill. See [CREDITS.md](CREDITS.md).
