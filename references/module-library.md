# Internal resource library

The four former companion packages are consolidated into `assets/design-library.json`, an indexed, checksummed local resource database. The main skill is the sole entry point. The library preserves detailed recipes, scripts, datasets, tests, licenses, and provenance without requiring separate skill installations or loading hundreds of pages into context.

Use `scripts/design_library.py` from this skill's actual directory. The script uses only Python's standard library, makes no network calls, and refuses changed output files rather than overwriting them. It does not run imported code automatically.

## Read only what is needed

```bash
python3 "<skill-root>/scripts/design_library.py" list frontend-design
python3 "<skill-root>/scripts/design_library.py" read frontend-design references/source-guide.md
python3 "<skill-root>/scripts/design_library.py" read hallmark references/resource-routing.md
```

Use `read` for a single reference. For linked guides or executable UI/UX search, materialize the chosen module into a workspace resource folder:

```bash
python3 "<skill-root>/scripts/design_library.py" materialize hallmark --output-dir "<workspace>/anti-slop-modules"
python3 "<skill-root>/scripts/design_library.py" materialize ui-ux-pro-max --output-dir "<workspace>/anti-slop-modules"
```

The command prints the resulting module root. Use that path for relative links and scripts. Existing identical files are reused; changed files cause an error. Use a fresh resource folder after a library update rather than forcing an overwrite. Do not add materialized files back into the skill package.

| Module | Entry and exact use |
|---|---|
| `frontend-design` | `references/source-guide.md` for a new creative brief or meaningful alternative directions |
| `frontend-design-doc` | `references/source-guide.md`, `references/structure_contract.md`, and conditionally `references/style_contract.md` for specification mode |
| `hallmark` | `references/workflow.md` and `references/resource-routing.md` for audit/redesign/study/posture; use the index to choose individual recipes |
| `ui-ux-pro-max` | `SKILL.md` query contract, `scripts/search.py`, relevant dataset/reference; `references/manual-mode.md` if search cannot run |

Original `SKILL.md` entries remain provenance/reference records, not additional active skill hubs. The consolidated hub and mode guides replace their old companion routing and independent style authority. Follow local links within the materialized module; ignore instructions to reinstall retired skills. Where archived text names `user:pdf-document`, `user:professional-docx`, or `user:pptx-creator`, use `user:office-documents`; where it names `user:humanizer`, `user:no-ai-slop`, or `user:match-my-writing-style`, use `user:humanizer`.

## Maintenance and verification

Run `python3 scripts/design_library.py verify` after changing the library. Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'` for library and source-audit regressions. `tests/test_design_library.py` checks integrity, safe paths, reading, materialization, reuse, and overwrite refusal.

The library's SHA-256 values detect accidental corruption; they do not authenticate third-party advice or establish its correctness. For substantive changes, run the materialized UI/UX `scripts/tests/test_core.py`, `scripts/tests/test_design_system_mode.py`, and `scripts/tests/test_data_contracts.py`, then representative domain, stack, and design-system searches. Some other preserved upstream tests require repository-only generators or plugin trees not shipped by the original skill; do not claim the whole upstream suite ran. Preserve provenance/licenses and update evidence claims separately.
