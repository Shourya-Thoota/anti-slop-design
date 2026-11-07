# Integrated UI/UX intelligence

UI/UX Pro Max is bundled inside this skill. Do not load or reinstall the retired skill. Follow `module-library.md` to materialize `ui-ux-pro-max`, then read its `SKILL.md` query contract as reference documentation, not a separate lead.

## Search and reconcile

1. Read the existing brand, design-system master, and page overrides. Detect the actual stack from the repository; never assume one or upgrade it to match a dataset.
2. Run the materialized `scripts/search.py` by its full path. For a new page/system use `--design-system`; for a focused concern use `--domain`; for implementation guidance use the detected `--stack`. Use one dominant intent and 2–5 meaningful terms per query.
3. For accessibility/text layout, search the semantic outcome first: `error summary validation`, `focus not obscured`, `badge chip label wraps`, or `live badge count screen reader`. Query stack details separately.
4. Verify result domain, top match, platform, and product fit. Retry empty/off-topic results once with a narrower query or explicit domain. If still inadequate, label general guidance as fallback; never imply a database match.
5. Reconcile with the main hub's precedence. Accept only applicable recommendations, then bind colors, fonts, space, radii, shadows, and motion to tokens. GSAP snippets do not authorize installing dependencies or adding decorative motion.
6. For category details read the module's `references/quick-reference.md`; for native/mobile delivery also read `references/pro-rules.md`. Adapt web CSS advice to native semantics and platform units. Apply the core quality gate and report actual test results.

Example after materialization:

```bash
python3 "<module-root>/scripts/search.py" "analytics dashboard" --design-system
python3 "<module-root>/scripts/search.py" "error summary validation" --domain ux
python3 "<module-root>/scripts/search.py" "suspense streaming" --stack nextjs
```

The module retains its 22 stack datasets, search modes, reasoning profiles, tests, provenance, and licenses. Use only the relevant result, not the entire database as a universal design standard.

## Persistence and fallback

Generate without persistence first. Persist only reconciled decisions, always with `--output-dir "<project-root>"`. Read existing `design-system/<project-slug>/MASTER.md` and page overrides first; do not use `--force` without explicit authorization. Inspect generated files and replace rejected defaults with the actual accepted decisions.

Page overrides cannot waive accessibility/functionality. Avoid private project data in queries and public output. If Python/search fails, read the module's `references/manual-mode.md`; identify the fallback rather than claiming search ran. Prose-only editing and document formatting do not require database search.
