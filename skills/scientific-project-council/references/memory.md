# Session Memory

Apply [execution-modes.md](execution-modes.md) to context isolation, stage execution, and completeness. SINGLE-CONTEXT REVIEW can finish with an advisory verdict when all stages pass; it must remain explicitly labeled in reports and history. STRICT INDEPENDENT retains its delegation requirement.

Only the coordinator writes history. Use the active student project/workspace, never the installed skill folder or a global assistant memory store. Respect a no-save instruction. Use the user's local date and known timezone in metadata; if unavailable, use the runtime date and identify that timezone honestly.

## Layout

```text
scientific-council/
  council.md
  sessions/
    YYYY-MM-DD-project-id.md
    YYYY-MM-DD-project-id.json
    YYYY-MM-DD-project-id-02.md
    YYYY-MM-DD-project-id-02.json
```

Markdown holds the full transcript. JSON sidecars hold stable project identity, status, a save sequence, timestamp, and summary fields. The script appends an entry to `council.md` while preserving all prior content. Same-day files receive numeric suffixes; no prior session is overwritten. Save sequence, not filename ordering or student-supplied date, defines recency.

Inventory existing IDs before assigning one to a new proposal. Use the same `project_id` across title changes, re-judgments, and pivots in the same identified project history. Distinct proposals must have distinct IDs even when their names coincide; add a meaningful qualifier or numeric suffix after checking for collisions. The ID must be lowercase ASCII kebab-case, at most 80 characters. Transliterate an Arabic title or choose a short neutral English ID. Never interpret student text as a path or command.

## Retrieve before a re-judge

Use the actual installed skill directory in place of `SKILL_DIR` and the active project in place of `PROJECT_DIR`; quote paths according to the shell. On Windows, use real accessible paths rather than a hard-coded `/tmp` location.

```text
python "SKILL_DIR/scripts/save_session.py" history --root "PROJECT_DIR" --slug "exact-project-id" --json
```

An exact, case-insensitive title lookup is also supported:

```text
python "SKILL_DIR/scripts/save_session.py" history --root "PROJECT_DIR" --title "Exact Project Title" --json
```

Omit the selector to inventory projects. With multiple projects, the helper returns no selected latest session; ask which project if the conversation does not identify it. Title matches that resolve to several IDs produce an ambiguity error. A title alias from an older session retrieves the same project's full history, including later renamed sessions. Slug matching is exact: `motor` never matches `motor-controller`.

Read `latest` and `latest_complete` separately, along with all warnings. Inspect the full applicable transcripts, not only metadata summaries. If the latest session is incomplete, follow `rejudge.md` before dispatching any Judge. If no completed ruling exists, do not invent a verdict transition. Corrupt metadata stops retrieval because recency cannot be trusted. A legacy Markdown file without JSON produces a warning and must be inspected manually before choosing history or saving a continuation.

## Prepare the full transcript

Use the session template in `output-templates.md`. Store the original and normalized proposal; full context/constraints/courses; assumptions and unknowns; student-reported versus inspected evidence; source list and search limitations; all accepted and superseded role outputs; execution metadata; quality-control defects; exact Judge ruling; objection history; MVP; validation test and stop condition; action plan; and user-facing report. Do not store credentials, unrelated personal data, copied source documents, or private chain-of-thought.

On evidence-only updates, copy or link each prior specialist's complete output and label it `REUSED — NOT RERUN`. Missing reviewers in an incomplete run are marked `NOT RUN` or `FAILED`; never fabricate transcripts to fill the template.

## Save

Write the transcript and metadata to separate temporary files in an accessible workspace. Use UTF-8. Example metadata (illustrative fields, not an evaluated project):

```json
{
  "project_id": "motor-monitor",
  "title": "Motor Vibration Monitor",
  "date": "2026-09-30",
  "timezone": "Africa/Cairo",
  "kind": "FULL COUNCIL",
  "status": "COMPLETE",
  "verdict": "REFINE",
  "biggest_risk": "O1: Ground-truth fault labels are not yet validated.",
  "prior_art": "UNCLEAR: the supplied evidence does not settle the closest comparison.",
  "mvp": "A controlled comparison on a documented test rig.",
  "validation_test": "Check label consistency before building the full pipeline; stop if no defensible reference can be obtained.",
  "course_coverage": "Signal Processing: MEDIUM; other requirements UNKNOWN."
}
```

Replace the illustrative date and values with the actual session. Required keys are the ones shown except `timezone`, which defaults to UNKNOWN. `kind` is FULL COUNCIL, EVIDENCE UPDATE, or PROJECT PIVOT. COMPLETE requires a real verdict; INCOMPLETE requires `verdict: "PENDING"`. An incomplete summary may use UNKNOWN for unavailable fields.

For a continuation, set `previous_session` to the indexed filename of the same project's preceding applicable session. The helper requires this explicit link whenever an ID already exists; a new distinct proposal must use a different ID. For a completed re-judge with a previous completed ruling, include `transition`, for example `"REFINE → APPROVE"`. The old verdict must match that referenced completed ruling and the new verdict must match this session. Do not include a transition after an incomplete-only history. Retrieval also verifies predecessor existence, project identity, sequence order, and transition agreement.

```text
python "SKILL_DIR/scripts/save_session.py" save --root "PROJECT_DIR" --content-file "TRANSCRIPT_FILE" --metadata-file "METADATA_FILE"
```

Never place arbitrary proposal text into a command string. The metadata file carries it safely. The helper reads back the written artifacts, prints `saved: true` with paths, and returns success only after verification. Check the exit status and returned paths; do not claim a failed write succeeded. Temporary input files are not the persisted record.

## Failure and legacy handling

- Concurrent saves are blocked by a lock. If a previous interrupted process left a lock, first establish that no save is running; do not blindly delete it or repeatedly retry.
- Ordinary write failures before index publication roll back only the new files created by that attempt, leaving older history unchanged. A process crash or external modification can still leave partial files: inspect warnings/errors and artifacts before retrying.
- Legacy transcripts without sidecars remain untouched. Read them manually. If continuing that history, save a new self-contained session that records the legacy paths and previous evidence in its transcript. Omit `previous_session` only when this project has no indexed session yet; once any applicable indexed session exists, including an incomplete one, supply its filename as the predecessor. Omit `transition` metadata until an indexed completed ruling can be referenced. A verified legacy verdict transition may still be explained in the report and transcript with its provenance. Do not invent a metadata link to a missing record.
- If Python or the helper is unavailable, manually save a unique Markdown transcript and append its human index entry, verify both, and clearly report that the file is unindexed. Later history retrieval requires manual inspection. Do not improvise JSON sequences.
- If writes are unavailable or prohibited, provide the unsaved transcript through an available artifact mechanism and state that future re-judging needs it supplied again. Do not silently switch to global memory.

The helper checks storage integrity and project identity. It does not inspect whether the transcript actually contains valid independent reviews; the coordinator must complete those checks first.
