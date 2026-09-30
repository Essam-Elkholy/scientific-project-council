# File Guide

Copy the entire `skills/scientific-project-council/` folder when installing. Everything outside it supports documentation, development, testing, or distribution.

## Installable skill

| File | Purpose |
| --- | --- |
| [SKILL.md](../skills/scientific-project-council/SKILL.md) | Entry point: activation, coordinator workflow, role order, isolated payloads, quality checks, and persistence. |
| [project-context.md](../skills/scientific-project-council/references/project-context.md) | Normalizes the proposal, extracts resources/courses, and records evidence, assumptions, and objections. |
| [agent-prompts.md](../skills/scientific-project-council/references/agent-prompts.md) | Complete prompts and operating addenda for all five reviewers, plus their common preamble. |
| [verdict-policy.md](../skills/scientific-project-council/references/verdict-policy.md) | Defines APPROVE, REFINE, RESCOPE, RETHINK, and REJECT, including approval gates. |
| [quality-control.md](../skills/scientific-project-council/references/quality-control.md) | Checks review quality, limits retries, and distinguishes an unsound project from an unreliable review. |
| [course-coverage.md](../skills/scientific-project-council/references/course-coverage.md) | Assesses actual student work and learning outcomes, with course examples and an FPGA image-processing example. |
| [rejudge.md](../skills/scientific-project-council/references/rejudge.md) | Chooses evidence-only re-judging or a full council after a pivot; carries cumulative evidence forward. |
| [memory.md](../skills/scientific-project-council/references/memory.md) | Documents history storage, helper commands, metadata, incomplete sessions, and legacy/recovery behavior. |
| [output-templates.md](../skills/scientific-project-council/references/output-templates.md) | Layouts for the student report and full saved transcript. |
| [scripts/save_session.py](../skills/scientific-project-council/scripts/save_session.py) | Saves transcripts and retrieves exact project history. It does not run the council or judge scientific quality. |
| [LICENSE](../skills/scientific-project-council/LICENSE) | MIT terms and both copyright notices, retained with a copied installation. |
| [CREDITS.md](../skills/scientific-project-council/CREDITS.md) | Upstream origin and scientific-adaptation credit, retained with a copied installation. |

All eight reference documents are in the installable folder's `references/` directory. They are loaded when their workflow stage needs them; a copied `SKILL.md` alone is not a complete installation.

## Repository and development files

| File | Purpose |
| --- | --- |
| [README.md](../README.md) | Public overview, installation, examples, verdicts, memory, testing, and attribution. |
| [LICENSE](../LICENSE) | Repository-wide MIT license, preserving the upstream notice and adding the adaptation notice. |
| [CREDITS.md](../CREDITS.md) | Names and links the original business council and describes this fork's changes. |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | How to propose changes and validate contributions. |
| [docs/FILE_GUIDE.md](FILE_GUIDE.md) | This explanation of the repository. |
| [docs/QUALITY.md](QUALITY.md) | What automated tests and manual review establish, and their limits. |
| [tests/test_sessions.py](../tests/test_sessions.py) | Synthetic regression tests of saving, exact selection, recency, transitions, incomplete sessions, corruption, and write failure. |
| [tests/test_distribution.py](../tests/test_distribution.py) | Checks the installable archive, notices, source/archive agreement, metadata, and documentation links. |
| [scripts/build_skill.py](../scripts/build_skill.py) | Rebuilds the `.skill` archive deterministically or verifies it with `--check`. |
| [.github/workflows/checks.yml](../.github/workflows/checks.yml) | Runs tests and archive verification on Windows/Linux with Python 3.9/3.14. |
| [.gitignore](../.gitignore) | Excludes local council history, temporary test data, Python caches, and virtual environments. |
| [.gitattributes](../.gitattributes) | Keeps text line endings consistent and treats `.skill` archives as binary. |
| [scientific-project-council.skill](../scientific-project-council.skill) | Downloadable ZIP-format bundle of the whole skill folder, including license and credits. Generated from source. |

## Tests are different from project results

`tests/` contains reusable programs that check code with artificial data. Publishing them lets contributors verify changes without exposing students' evaluations. The temporary test fixtures are cleaned up after execution.

`scientific-council/council.md` and `scientific-council/sessions/` are created in the student workspace when the council runs. They hold proposals, evidence, and judgments. They are not distributed or committed as test results and are excluded by `.gitignore`.

[execution-modes.md](../skills/scientific-project-council/references/execution-modes.md) selects independent dispatch, an explicitly labeled single-context fallback, or strict independent execution.
