#!/usr/bin/env python3
"""Build or check the distributable skill using only the Python standard library."""

import argparse
from io import BytesIO
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/scientific-project-council"
OUTPUT = ROOT / "scientific-project-council.skill"


def archive_content(path):
    """Use Git's LF representation for skill text; preserve binary assets."""
    content = path.read_bytes()
    if path.suffix in {".md", ".py"} or path.name == "LICENSE":
        content = content.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return content


def package_bytes():
    buffer = BytesIO()
    files = sorted((p for p in SKILL.rglob("*") if p.is_file()
                    and "__pycache__" not in p.parts and p.suffix not in {".pyc", ".pyo"}),
                   key=lambda p: p.relative_to(SKILL.parent).as_posix())
    with ZipFile(buffer, "w", compression=ZIP_STORED) as archive:
        for path in files:
            if path.is_symlink():
                raise ValueError(f"Refusing a symlink in the installable skill: {path}")
            info = ZipInfo(path.relative_to(SKILL.parent).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            # No compression avoids zlib-version differences between platforms.
            archive.writestr(info, archive_content(path))
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = package_bytes()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != expected:
            parser.exit(1, "Archive is missing or stale. Run python scripts/build_skill.py and commit the updated .skill file.\n")
        print("Skill archive matches source, including license and credits.")
    else:
        OUTPUT.write_bytes(expected)
        print(f"Built {OUTPUT.name} ({len(expected):,} bytes).")


if __name__ == "__main__":
    main()
