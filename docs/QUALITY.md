# Quality and Validation Scope

## Automated checks

The [GitHub Actions workflow](../.github/workflows/checks.yml) runs on pushes to `main`, pull requests, and manual dispatch. It uses read-only repository permissions and requires no API key or model account. It runs standard-library tests on Windows/Linux with Python 3.9/3.14 and checks that the committed archive matches source.

[test_sessions.py](../tests/test_sessions.py) checks exact project identity, ambiguous and renamed projects, same-day recency, backdated display dates, separate latest/latest-complete sessions, retained history, predecessor links, verdict transitions, invalid metadata, corrupt history, legacy files, Unicode content, write-error rollback, and competing-save locks.

These tests create synthetic fixtures under `tests/.test-runs/`. Cleanup verifies that its target stays inside the test directory. No real student evaluation is used or published.

[test_distribution.py](../tests/test_distribution.py) checks package contents, licensing/attribution, source/archive agreement, entrypoint metadata, and local documentation links. [build_skill.py](../scripts/build_skill.py) uses fixed entry order, timestamps, and uncompressed entries for reproducible archives across platforms.

Run from the repository root:

```text
python -X utf8 -B -m unittest discover -s tests -v
python -X utf8 -B scripts/build_skill.py --check
```

If installable files change, run `python scripts/build_skill.py` first and commit the updated archive.

## Academic workflow review

In independent mode the skill requires fresh sequential reviewer contexts. Both modes require evidence provenance, inspected prior art, measurable experiments, meaningful course work, dispute resolution, and explicit handling of incomplete reviews. Re-judging includes cumulative evidence and distinguishes a design pivot from an evidence update.

Manual inspection of the merged instructions covered missing constraints, unknown PBL courses, replication projects, unmeasurable objectives, failed reviewers, unavailable subagents, changed courses, and repeated evidence updates. This is workflow inspection, not a benchmark of model performance.

## Limits

- Automated tests do not invoke Claude Code or prove that a model follows every instruction.
- They do not establish literature completeness or the correctness of scientific verdicts across disciplines.
- They do not clinically validate medical-image projects used as examples.
- Ordinary write failures are tested; process crashes or external changes can still require manual recovery.

Native end-to-end council execution has not been verified as part of this package's local validation. Use the workflow's actual status for current CI evidence, rather than assuming a previous successful run covers new edits.

The uploaded 2026-09-30 transcript demonstrates that mandatory delegation prevented execution in a tool-limited Claude environment. AUTO now specifies a disclosed single-context fallback; STRICT INDEPENDENT retains the original requirement. This correction is based on an observed failure, but has not yet been run end-to-end in that Claude environment.
