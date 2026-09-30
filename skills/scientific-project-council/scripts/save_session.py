#!/usr/bin/env python3
"""Save council transcripts and retrieve exact project history (Python 3.9+).

save --root PROJECT --content-file TRANSCRIPT --metadata-file METADATA_JSON
history --root PROJECT [--slug PROJECT_ID | --title EXACT_TITLE] [--json]

Markdown is the human record. Per-session JSON sidecars hold explicit project
identity and a save sequence; filenames are never used to infer recency.
"""

import argparse
from contextlib import contextmanager
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
from uuid import uuid4


VERDICTS = {"APPROVE", "REFINE", "RESCOPE", "RETHINK", "REJECT"}
KINDS = {"FULL COUNCIL", "EVIDENCE UPDATE", "PROJECT PIVOT"}
STATUSES = {"COMPLETE", "INCOMPLETE"}
SUMMARY_FIELDS = ("biggest_risk", "prior_art", "mvp", "validation_test", "course_coverage")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
SESSION = re.compile(r"\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md\Z")


class CouncilError(ValueError):
    pass


def text_field(value, name):
    if not isinstance(value, str) or not value.strip():
        raise CouncilError(f"{name} must be a nonempty string")
    return " ".join(value.split())


def validate_metadata(raw):
    if not isinstance(raw, dict):
        raise CouncilError("Metadata must be a JSON object")
    required = ("project_id", "title", "date", "kind", "status", "verdict") + SUMMARY_FIELDS
    missing = [key for key in required if key not in raw]
    if missing:
        raise CouncilError("Missing metadata fields: " + ", ".join(missing))
    m = {key: text_field(raw[key], key) for key in required}
    if not SLUG.fullmatch(m["project_id"]) or len(m["project_id"]) > 80:
        raise CouncilError("project_id must be a stable lowercase ASCII kebab-case ID (max 80 characters)")
    try:
        valid_date = date.fromisoformat(m["date"])
    except ValueError as exc:
        raise CouncilError("date must be a real YYYY-MM-DD date") from exc
    if valid_date.isoformat() != m["date"]:
        raise CouncilError("date must use YYYY-MM-DD format")
    if m["kind"] not in KINDS or m["status"] not in STATUSES:
        raise CouncilError("Invalid kind or status")
    if m["status"] == "COMPLETE" and m["verdict"] not in VERDICTS:
        raise CouncilError("A COMPLETE session needs one of the five verdicts")
    if m["status"] == "INCOMPLETE" and m["verdict"] != "PENDING":
        raise CouncilError("An INCOMPLETE session must use verdict PENDING")
    m["timezone"] = text_field(raw.get("timezone", "UNKNOWN"), "timezone")
    for key in ("previous_session", "transition"):
        value = raw.get(key)
        if value is not None:
            m[key] = text_field(value, key)
    previous = m.get("previous_session")
    if previous and not SESSION.fullmatch(previous):
        raise CouncilError("previous_session must be a session filename, not a path")
    transition = m.get("transition")
    if transition:
        pair = transition.split(" → ")
        if (len(pair) != 2 or any(v not in VERDICTS for v in pair)
                or pair[1] != m["verdict"] or not previous
                or m["status"] != "COMPLETE"):
            raise CouncilError("transition must be OLD → NEW with valid verdicts, matching this completed session and a previous_session")
    return m


def confined(path, parent):
    if not path.resolve().is_relative_to(parent.resolve()):
        raise CouncilError(f"Path escapes the intended directory: {path}")
    return path


def locations(root):
    workspace = Path(root).resolve()
    base = confined(workspace / "scientific-council", workspace)
    sessions = confined(base / "sessions", base)
    confined(base / "council.md", base)
    return base, sessions


def read_records(sessions):
    records, warnings, seen = [], [], set()
    if not sessions.exists():
        return records, warnings
    for path in sessions.glob("*.json"):
        confined(path, sessions)
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            validate_metadata(record)
            if record.get("schema_version") != 1:
                raise CouncilError("Unsupported metadata schema")
            seq = record.get("sequence")
            if type(seq) is not int or seq <= 0 or seq in seen:
                raise CouncilError("Invalid or duplicate save sequence")
            expected = path.with_suffix(".md").name
            if record.get("session_file") != expected or not SESSION.fullmatch(expected):
                raise CouncilError("Session filename does not match its metadata")
            transcript = confined(sessions / expected, sessions)
            if not transcript.is_file():
                raise CouncilError("Transcript is missing")
            seen.add(seq)
            records.append(record)
        except (ValueError, TypeError, OSError) as exc:
            raise CouncilError(f"Cannot trust history metadata {path.name}: {exc}") from exc
    records.sort(key=lambda r: r["sequence"])
    by_file = {r["session_file"]: r for r in records}
    project_ids_seen = set()
    for record in records:
        previous = record.get("previous_session")
        if not previous and record["project_id"] in project_ids_seen:
            raise CouncilError("Existing project history is missing its predecessor link: " + record["session_file"])
        if previous:
            prior = by_file.get(previous)
            if (prior is None or prior["project_id"] != record["project_id"]
                    or prior["sequence"] >= record["sequence"]):
                raise CouncilError("Invalid historical predecessor: " + record["session_file"])
            if record.get("transition"):
                old_verdict = record["transition"].split(" → ")[0]
                if prior["status"] != "COMPLETE" or prior["verdict"] != old_verdict:
                    raise CouncilError("Historical transition disagrees with its predecessor: " + record["session_file"])
        project_ids_seen.add(record["project_id"])
    indexed = set(by_file)
    for path in sessions.glob("*.md"):
        if path.name not in indexed:
            warnings.append(f"Unindexed or legacy transcript requires manual inspection: {path.name}")
    return records, warnings


@contextmanager
def save_lock(base):
    lock = base / ".save.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise CouncilError("Another save may be active (.save.lock exists). Do not delete the lock without checking that no save is running.") from exc
    try:
        os.close(fd)
        yield
    finally:
        lock.unlink()


def memory_entry(record):
    r = record
    lines = [f"## {r['date']} — {r['title']}", "",
             f"PROJECT ID: {r['project_id']}", f"SESSION ID: {r['session_id']}",
             f"SESSION: [Full session](sessions/{r['session_file']})",
             f"MODE: {r['kind']}", f"STATUS: {r['status']}", ""]
    if r.get("transition"):
        lines += [f"TRANSITION: {r['transition']}", ""]
    for label, key in (("VERDICT", "verdict"), ("BIGGEST RISK", "biggest_risk"),
                       ("PRIOR ART", "prior_art"), ("MVP", "mvp"),
                       ("VALIDATION TEST", "validation_test"), ("COURSE COVERAGE", "course_coverage")):
        value = "PENDING — INCOMPLETE" if key == "verdict" and r["status"] == "INCOMPLETE" else r[key]
        lines += [label + ":", value, ""]
    return "\n".join(lines) + "---\n\n"


def save(root, content_file, metadata_file):
    metadata = validate_metadata(json.loads(Path(metadata_file).read_text(encoding="utf-8")))
    body = Path(content_file).read_text(encoding="utf-8")
    if not body.strip():
        raise CouncilError("Transcript cannot be empty")
    base, sessions = locations(root)
    sessions.mkdir(parents=True, exist_ok=True)
    with save_lock(base):
        records, warnings = read_records(sessions)
        previous = metadata.get("previous_session")
        if not previous and any(r["project_id"] == metadata["project_id"] for r in records):
            raise CouncilError("Project ID already exists: provide an explicit previous_session for this continuation, or use a unique ID for a distinct project")
        if previous:
            matches = [r for r in records if r["session_file"] == previous]
            if not matches or matches[0]["project_id"] != metadata["project_id"]:
                raise CouncilError("previous_session must reference indexed history of this exact project")
            if metadata.get("transition"):
                prior = matches[0]
                if prior["status"] != "COMPLETE" or metadata["transition"].split(" → ")[0] != prior["verdict"]:
                    raise CouncilError("Transition must start from the referenced COMPLETE session's verdict")
        stem = f"{metadata['date']}-{metadata['project_id']}"
        dest, suffix = sessions / f"{stem}.md", 2
        while dest.exists() or dest.with_suffix(".json").exists():
            dest = sessions / f"{stem}-{suffix:02d}.md"
            suffix += 1
        record = dict(metadata, schema_version=1, session_id=uuid4().hex,
                      sequence=max((r["sequence"] for r in records), default=0) + 1,
                      created_at=datetime.now(timezone.utc).isoformat(), session_file=dest.name)
        index = base / "council.md"
        old_index = index.read_text(encoding="utf-8") if index.exists() else "# Scientific Project Council — Session Index\n\n"
        new_index = old_index + ("\n" if not old_index.endswith("\n") else "") + memory_entry(record)
        sidecar = dest.with_suffix(".json")
        temp_index = base / (".council-index-" + uuid4().hex + ".tmp")
        created = []
        try:
            with dest.open("x", encoding="utf-8", newline="\n") as stream:
                created.append(dest)
                stream.write(body)
            with sidecar.open("x", encoding="utf-8", newline="\n") as stream:
                created.append(sidecar)
                json.dump(record, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
            with temp_index.open("x", encoding="utf-8", newline="\n") as stream:
                created.append(temp_index)
                stream.write(new_index)
            if dest.read_text(encoding="utf-8") != body or json.loads(sidecar.read_text(encoding="utf-8")) != record:
                raise CouncilError("Written session failed read-back verification")
            os.replace(temp_index, index)
        except Exception:
            for path in reversed(created):
                confined(path, base)
                path.unlink(missing_ok=True)
            raise
        if index.read_text(encoding="utf-8") != new_index:
            raise CouncilError("Session files were saved but index read-back failed; inspect before retrying")
    return {"saved": True, "session": str(dest), "metadata": str(sidecar),
            "index": str(index), "sequence": record["sequence"], "warnings": warnings}


def history(root, slug=None, title=None):
    if slug and title:
        raise CouncilError("Use either --slug or --title, not both")
    if slug and not SLUG.fullmatch(slug):
        raise CouncilError("Use the exact project ID for --slug")
    base, sessions = locations(root)
    if (base / ".save.lock").exists():
        raise CouncilError("A save may be in progress; retry history after it finishes")
    records, warnings = read_records(sessions)
    projects = {}
    for r in records:
        p = projects.setdefault(r["project_id"], {"project_id": r["project_id"], "titles": []})
        if r["title"] not in p["titles"]:
            p["titles"].append(r["title"])
    if title:
        ids = {r["project_id"] for r in records if r["title"].casefold() == title.strip().casefold()}
        if len(ids) > 1:
            raise CouncilError("Title is ambiguous; use an exact --slug: " + ", ".join(sorted(ids)))
        slug = next(iter(ids), None)
        selected = [r for r in records if slug and r["project_id"] == slug]
    elif slug:
        selected = [r for r in records if r["project_id"] == slug]
    else:
        selected = records
    # An unfiltered inventory must never choose one project on the student's behalf.
    single_project = len({r["project_id"] for r in selected}) == 1
    complete = [r for r in selected if r["status"] == "COMPLETE"]
    latest = selected[-1] if selected and single_project else None
    latest_complete = complete[-1] if complete and single_project else None
    return {"projects": list(projects.values()), "sessions": selected,
            "latest": str(sessions / latest["session_file"]) if latest else None,
            "latest_complete": str(sessions / latest_complete["session_file"]) if latest_complete else None,
            "warnings": warnings, "found": bool(selected)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    writer = sub.add_parser("save")
    writer.add_argument("--root", required=True)
    writer.add_argument("--content-file", required=True)
    writer.add_argument("--metadata-file", required=True)
    reader = sub.add_parser("history")
    reader.add_argument("--root", required=True)
    group = reader.add_mutually_exclusive_group()
    group.add_argument("--slug")
    group.add_argument("--title")
    reader.add_argument("--json", action="store_true", help="Emit structured JSON instead of a readable inventory")
    args = parser.parse_args(argv)
    try:
        if args.command == "save":
            result = save(args.root, args.content_file, args.metadata_file)
        else:
            result = history(args.root, args.slug, args.title)
        if args.command == "history" and not args.json:
            for project in result["projects"]:
                print(f"PROJECT: {project['project_id']} | {' / '.join(project['titles'])}")
            for record in result["sessions"]:
                print(f"SESSION {record['sequence']}: {record['session_file']} | {record['status']} | {record['verdict']}")
            print("LATEST: " + (result["latest"] or "NONE — select an exact project or inspect missing history"))
            print("LATEST COMPLETE: " + (result["latest_complete"] or "NONE"))
            for warning in result["warnings"]:
                print("WARNING: " + warning)
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (CouncilError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
