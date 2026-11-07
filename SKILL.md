---
name: anti-slop-design
description: "Design, build, audit, and document distinctive interfaces. Use for websites, apps, components, creative direction, screenshot studies, redesigns, accessibility, design systems, and developer handoffs. Includes Frontend Design, Hallmark, and UI/UX Pro Max internally; not prose-only editing, backend-only work, or AI-authorship detection."
metadata:
  version: "4.0.0"
---
# Anti-Slop Design

One skill for creative direction, implementation, audits/studies, UI/UX search, and specifications. Use internal modes; do not load or reinstall the four retired companion skills.

## Contract and modes

Accessibility/functionality, user/project constraints, and established brand outrank optional defaults. Preserve routes, ownership, content intent, framework conventions, and tokens. No compulsory house style or aesthetic authorship verdicts.

Read `references/linked-design-workflow.md` for mode selection and internal module access. Audit is read-only; study diagnoses before an optional build; direction-only stops at a brief; a focused component fix stays narrow. For developer documentation read `references/specification-mode.md`. Prose-only work belongs to humanizer; video and illustration remain their own specialties.

## Workflow

1. Establish reader, product, primary task, actual content, existing brand, stack, and scope. For implementation read `README.md`, `references/integration.md`, and `references/design-quality-gate.md`; record a short direction before styling.
2. For new directions/full audits read `references/design-indicators.md`; for small fixes use its relevant category. Use the creative module for up to three materially different directions; select for product fit without repeating completed decisions.
3. For audit/redesign/study/posture use Hallmark mode in `references/linked-design-workflow.md`. Read its index and selected guides, not conflicting legacy defaults or external-skill routing.
4. For UI/UX recommendations read `references/ui-ux-integration.md` and run the bundled search through the internal module. Choose design-system, domain, or detected-stack search proportionally. Verify fit; database output is a candidate, not a mandate.
5. Read `tokens.json` and selected `components/<Pattern>/README.md` guides: H hero, N navigation, Ft footer, F feature, C CTA, S heading, T proof. Read `components/bundle.css` only when using its classes. Bind accepted decisions to tokens. Seven themes are optional starting points, never a compulsory default.
6. Implement real destinations, interactions, and applicable states. Preserve semantics, keyboard operation, responsive content, and reduced motion. Never invent metrics, testimonials, customers, countdowns, backend success, or save claims.
7. Run `scripts/design_audit.py "<project-root>" --json`. It flags source-review candidates, not browser conformance or authorship. Render desktop/mobile views, exercise primary flows/failures, fix and retest. Record actual screenshots, viewport, observed behavior, exceptions, and unverified checks.

For alternatives outside the themes read `assets/Reference/README.md` and needed catalog rows. For bundle-cover preview use `components/Cover/preview.html` only. For evidence or changing recommendations read `references/design-evidence.md`. A full Anti-Slop standards document additionally uses `references/document-workflow.md`; do not impose its 16 sections on ordinary handoffs.

Internal resources are indexed in `assets/design-library.json`; access selected entries with `scripts/design_library.py` as documented in `references/module-library.md`. Do not read the whole dataset into context. For library maintenance run `tests/test_design_library.py`; preserve the original source-review tests too.

Completion: the requested brief, ranked audit, implementation, study, or specification, with evidenced checks and explicit limitations; no duplicate passes.
