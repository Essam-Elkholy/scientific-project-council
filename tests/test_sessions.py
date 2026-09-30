"""Regression tests for session identity, retrieval, and safe persistence."""

import importlib.util
import json
from pathlib import Path
import shutil
import unittest
from unittest.mock import patch
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "council_sessions", ROOT / "skills/scientific-project-council/scripts/save_session.py")
council = importlib.util.module_from_spec(spec)
spec.loader.exec_module(council)


class SessionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sandbox = ROOT / "tests/.test-runs"
        cls.sandbox.mkdir(exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        if cls.sandbox.exists() and not any(cls.sandbox.iterdir()):
            cls.sandbox.rmdir()

    def setUp(self):
        self.root = self.sandbox / uuid4().hex
        self.root.mkdir()

    def tearDown(self):
        target = self.root.resolve()
        self.assertEqual(target.parent, self.sandbox.resolve())
        self.assertTrue(target.is_relative_to(self.sandbox.resolve()))
        shutil.rmtree(target)

    def save(self, body="Review", link_previous=True, **changes):
        data = dict(project_id="motor", title="Motor Monitor", date="2026-09-30",
                    timezone="Africa/Cairo", kind="FULL COUNCIL", status="COMPLETE",
                    verdict="REFINE", biggest_risk="Unvalidated labels", prior_art="UNCLEAR",
                    mvp="Controlled experiment", validation_test="Check reference labels",
                    course_coverage="UNKNOWN")
        data.update(changes)
        if link_previous and "previous_session" not in data:
            records, _ = council.read_records(self.root / "scientific-council/sessions")
            prior = [r for r in records if r["project_id"] == data["project_id"]]
            if prior:
                data["previous_session"] = prior[-1]["session_file"]
        content, metadata = self.root / "input.md", self.root / "input.json"
        content.write_text(body, encoding="utf-8")
        metadata.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return council.save(self.root, content, metadata)

    def latest_body(self, **selector):
        return Path(council.history(self.root, **selector)["latest"]).read_text(encoding="utf-8")

    def change_record(self, saved, **changes):
        path = Path(saved["metadata"])
        data = json.loads(path.read_text(encoding="utf-8"))
        data.update(changes)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_same_day_latest_after_twelve_saves(self):
        paths = [self.save(body=f"review-{i}")["session"] for i in range(12)]
        self.assertEqual(self.latest_body(slug="motor"), "review-11")
        self.assertEqual(len(set(paths)), 12)
        self.assertEqual(Path(paths[0]).read_text(encoding="utf-8"), "review-0")

    def test_title_does_not_select_another_project(self):
        self.save(body="Motor", date="2026-09-29")
        self.save(body="Weather", project_id="weather", title="Weather Station")
        self.assertEqual(self.latest_body(title="Motor Monitor"), "Motor")

    def test_slug_matching_is_exact(self):
        self.save(body="Exact")
        self.save(body="Substring", project_id="motor-controller", title="Motor Controller")
        self.assertEqual(self.latest_body(slug="motor"), "Exact")

    def test_inventory_never_selects_between_projects(self):
        self.save()
        self.save(project_id="weather", title="Weather Station")
        result = council.history(self.root)
        self.assertIsNone(result["latest"])
        self.assertIsNone(result["latest_complete"])

    def test_title_ambiguity_is_reported(self):
        self.save()
        self.save(project_id="different-project")
        with self.assertRaisesRegex(council.CouncilError, "ambiguous"):
            council.history(self.root, title="Motor Monitor")

    def test_title_alias_survives_rename(self):
        self.save(body="Old")
        self.save(body="Renamed", title="Vibration Monitor")
        self.assertEqual(self.latest_body(title="motor monitor"), "Renamed")

    def test_latest_complete_is_separate(self):
        complete = self.save()
        incomplete = self.save(status="INCOMPLETE", verdict="PENDING")
        result = council.history(self.root, slug="motor")
        self.assertEqual(result["latest"], incomplete["session"])
        self.assertEqual(result["latest_complete"], complete["session"])

    def test_backdated_date_does_not_change_recency(self):
        self.save(body="First")
        self.save(body="Second", date="2026-09-01")
        self.assertEqual(self.latest_body(slug="motor"), "Second")

    def test_index_retains_old_entries(self):
        index = Path(self.save()["index"])
        old = index.read_bytes()
        self.save()
        self.assertTrue(index.read_bytes().startswith(old))
        self.assertEqual(index.read_text(encoding="utf-8").count("SESSION ID:"), 2)

    def test_transition_validates_project_and_prior_verdict(self):
        name = Path(self.save()["session"]).name
        self.save(kind="EVIDENCE UPDATE", verdict="APPROVE", previous_session=name,
                  transition="REFINE → APPROVE")
        with self.assertRaisesRegex(council.CouncilError, "exact project"):
            self.save(project_id="weather", previous_session=name)
        with self.assertRaisesRegex(council.CouncilError, "referenced COMPLETE"):
            self.save(previous_session=name, transition="APPROVE → REFINE")

    def test_incomplete_cannot_claim_approval(self):
        with self.assertRaisesRegex(council.CouncilError, "PENDING"):
            self.save(status="INCOMPLETE", verdict="APPROVE")

    def test_invalid_identity_and_date_are_rejected(self):
        for change in ({"project_id": "../outside"}, {"date": "../../outside"},
                       {"date": "2026-02-30"}, {"previous_session": "../outside.md"}):
            with self.subTest(change=change), self.assertRaises(council.CouncilError):
                self.save(**change)
        self.assertFalse((self.root / "scientific-council").exists())

    def test_empty_transcript_is_rejected(self):
        with self.assertRaisesRegex(council.CouncilError, "empty"):
            self.save(body=" \n")

    def test_legacy_files_are_preserved_and_reported(self):
        sessions = self.root / "scientific-council/sessions"
        sessions.mkdir(parents=True)
        legacy = sessions / "2026-09-30-motor.md"
        legacy.write_text("Legacy", encoding="utf-8")
        result = council.history(self.root, slug="motor")
        self.assertIsNone(result["latest"])
        self.assertTrue(result["warnings"])
        self.assertTrue(self.save()["session"].endswith("motor-02.md"))
        self.assertEqual(legacy.read_text(), "Legacy")

    def test_corrupt_metadata_stops_retrieval(self):
        Path(self.save()["metadata"]).write_text("not JSON", encoding="utf-8")
        with self.assertRaisesRegex(council.CouncilError, "Cannot trust history"):
            council.history(self.root, slug="motor")

    def test_failed_index_publication_rolls_back_new_save(self):
        first = self.save(body="Original")
        index = Path(first["index"])
        old = index.read_bytes()
        with patch.object(council.os, "replace", side_effect=OSError("Simulated write failure")):
            with self.assertRaises(OSError):
                self.save(body="Must roll back")
        self.assertEqual(index.read_bytes(), old)
        self.assertEqual(len(council.history(self.root, slug="motor")["sessions"]), 1)
        self.assertEqual(self.latest_body(slug="motor"), "Original")
        self.assertFalse((index.parent / ".save.lock").exists())

    def test_lock_blocks_save_and_history(self):
        self.save()
        lock = self.root / "scientific-council/.save.lock"
        lock.write_text("Active", encoding="utf-8")
        with self.assertRaisesRegex(council.CouncilError, "save may be active"):
            self.save()
        with self.assertRaisesRegex(council.CouncilError, "save may be in progress"):
            council.history(self.root, slug="motor")
        self.assertEqual(lock.read_text(), "Active")

    def test_unicode_title_and_transcript_round_trip(self):
        arabic = "\u0645\u0634\u0631\u0648\u0639"
        self.save(body=arabic + " — FPGA", title=arabic)
        self.assertEqual(self.latest_body(title=arabic), arabic + " — FPGA")

    def test_existing_id_needs_explicit_continuation(self):
        self.save()
        with self.assertRaisesRegex(council.CouncilError, "Project ID already exists"):
            self.save(link_previous=False, title="Distinct proposal")

    def test_missing_predecessor_stops_retrieval(self):
        self.save()
        self.change_record(self.save(), previous_session="2026-09-29-missing.md")
        with self.assertRaisesRegex(council.CouncilError, "Invalid historical predecessor"):
            council.history(self.root, slug="motor")

    def test_changed_transition_stops_retrieval(self):
        name = Path(self.save()["session"]).name
        second = self.save(kind="EVIDENCE UPDATE", verdict="APPROVE", previous_session=name,
                           transition="REFINE → APPROVE")
        self.change_record(second, transition="REJECT → APPROVE")
        with self.assertRaisesRegex(council.CouncilError, "Historical transition"):
            council.history(self.root, slug="motor")

    def test_forward_predecessor_stops_retrieval(self):
        first, second = self.save(), self.save()
        self.change_record(first, previous_session=Path(second["session"]).name)
        with self.assertRaisesRegex(council.CouncilError, "Invalid historical predecessor"):
            council.history(self.root, slug="motor")


if __name__ == "__main__":
    unittest.main(verbosity=2)
