# Optional local installation

This guide is for Claude Code users who want a local folder installation. These commands are not needed when uploading the packaged skill in Claude. For the simple upload workflow, see the [README](../README.md).


Choose one destination:

| Scope | Location |
| --- | --- |
| One project | `<project>/.claude/skills/scientific-project-council/` |
| All local projects | `~/.claude/skills/scientific-project-council/` |

Copy the entire `scientific-project-council` skill folder, including `references` and `scripts`, into that destination. Install this edition in place of the older edition, not alongside another skill with the same name. Preserve a backup before replacing an existing installed copy. Student history lives separately and should not be overwritten during installation.

Download [scientific-project-council.skill](../scientific-project-council.skill), a ZIP-format archive with the complete skill folder at its root, including its license and credits. For local Claude Code installation, extract it and copy that folder into the location above. GitHub's source ZIP additionally contains the repository documentation and tests. Archive packaging does not itself activate the skill.

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

