"""Checks of the shipped artifact and its documented installation contract."""

import importlib.util
from io import BytesIO
from pathlib import Path
import re
import unittest
import shutil
import uuid
from unittest.mock import patch
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/scientific-project-council"
spec = importlib.util.spec_from_file_location("skill_builder", ROOT / "scripts/build_skill.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class DistributionTests(unittest.TestCase):
    def test_committed_archive_matches_installable_source(self):
        self.assertEqual((ROOT / "scientific-project-council.skill").read_bytes(), builder.package_bytes())
        with ZipFile(BytesIO(builder.package_bytes())) as archive:
            files = [p for p in SKILL.rglob("*") if p.is_file() and "__pycache__" not in p.parts
                     and p.suffix not in {".pyc", ".pyo"}]
            expected = {p.relative_to(SKILL.parent).as_posix(): builder.archive_content(p) for p in files}
            self.assertEqual(set(archive.namelist()), set(expected))
            self.assertEqual(archive.namelist(), sorted(archive.namelist()))
            for name, content in expected.items():
                self.assertEqual(archive.read(name), content)
            self.assertIsNone(archive.testzip())

    def test_notices_survive_standalone_distribution(self):
        for name in ("LICENSE", "CREDITS.md"):
            self.assertEqual((ROOT / name).read_bytes(), (SKILL / name).read_bytes())
        license_text = (SKILL / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 faroukahmed89-droid", license_text)
        self.assertIn("Copyright (c) 2026 Essam-Elkholy", license_text)

    def test_relative_documentation_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            if ".test-runs" in path.parts:
                continue
            text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if "://" in link or link.startswith("#"):
                    continue
                self.assertTrue((path.parent / link.split("#")[0]).exists(), f"{path}: {link}")

    def test_entrypoint_has_installable_metadata(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        self.assertIsNotNone(match)
        fields = dict(line.split(": ", 1) for line in match.group(1).splitlines())
        self.assertEqual(fields["name"], SKILL.name)
        self.assertEqual(fields["license"], "MIT")
        self.assertTrue(0 < len(fields["description"]) <= 1024)
        self.assertNotIn("context", fields)

    def test_distribution_excludes_history_and_development_data(self):
        with ZipFile(BytesIO(builder.package_bytes())) as archive:
            for name in archive.namelist():
                parts = Path(name).parts
                for excluded in ("scientific-council", "tests", "__pycache__", ".github"):
                    self.assertNotIn(excluded, parts)

    def test_lf_and_crlf_checkouts_produce_identical_archives(self):
        scratch = ROOT / "tests" / ".test-runs"
        work = scratch / ("package-" + uuid.uuid4().hex)
        skill = work / "scientific-project-council"
        skill.mkdir(parents=True)
        try:
            text_file = skill / "SKILL.md"
            asset = skill / "sample.bin"
            binary = b"\x00\xff\r\n\x80"
            asset.write_bytes(binary)
            with patch.object(builder, "SKILL", skill):
                text_file.write_bytes(b"name: council\nreview: evidence\n")
                lf_archive = builder.package_bytes()
                text_file.write_bytes(b"name: council\r\nreview: evidence\r\n")
                self.assertEqual(lf_archive, builder.package_bytes())
            with ZipFile(BytesIO(lf_archive)) as archive:
                self.assertEqual(archive.read("scientific-project-council/SKILL.md"),
                                 b"name: council\nreview: evidence\n")
                self.assertEqual(archive.read("scientific-project-council/sample.bin"), binary)
        finally:
            if work.resolve().parent != scratch.resolve():
                raise RuntimeError("Test cleanup path escaped its workspace")
            shutil.rmtree(work)

    def test_builder_has_no_timestamp_variation(self):
        self.assertEqual(builder.package_bytes(), builder.package_bytes())


if __name__ == "__main__":
    unittest.main(verbosity=2)
