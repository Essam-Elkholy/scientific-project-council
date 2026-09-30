# Contributing

Keep changes focused on scientific project evaluation, evidence handling, and academic decisions. Describe the problem, resulting behavior, and validation in a pull request.

Use Python 3.9+; no third-party packages are required for the helper, builder, or tests.

```text
python -X utf8 -B scripts/build_skill.py
python -X utf8 -B -m unittest discover -s tests -v
python -X utf8 -B scripts/build_skill.py --check
```

Rebuild the `.skill` archive when installable files change. Keep repository and installable copies of LICENSE and CREDITS.md synchronized. Preserve the upstream copyright notice and MIT permission text.

For prompt changes, check each isolated agent's payload: reading a reference in the coordinator does not automatically pass it to a subagent. Preserve justified approval and rejection, and distinguish missing evidence from demonstrated impossibility. Use realistic examples when changing verdicts, course coverage, or re-judging.

Add regression cases for demonstrated failures. Use synthetic fixtures; do not commit real council histories, credentials, or private evidence. Contributions are distributed under the repository's [MIT License](LICENSE). See [CREDITS.md](CREDITS.md) for upstream provenance.
