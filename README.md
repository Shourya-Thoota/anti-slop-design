# Anti-Slop Design

An agent skill for designing, building, auditing, and documenting interfaces that read as made by a person, not generated. One skill covers creative direction, implementation, screenshot studies and audits, UI/UX search, and developer handoff specifications — with accessibility, existing brand, and your project's constraints ranked above any house style.

**By [Vibhav Thoota](https://github.com/Shourya-Thoota) / [Pansophy LLC](https://github.com/Shourya-Thoota).**

## What it does

- **Implementation** — build pages and components from tokenized themes (seven bundled starting points: specimen, midnight, cobalt, carnival, lumen, hum, grid) and pattern guides for heroes, navigation, footers, features, CTAs, section heads, and proof.
- **Audits and studies** — read-only audits that flag generic design with concrete remedies, plus diagnostic studies before an optional rebuild.
- **Creative direction** — up to three materially different directions for a brief, selected for product fit.
- **Redesign** — a Hallmark mode that changes a page's structural fingerprint and component voice while preserving routes, copy intent, brand, and working logic.
- **UI/UX search** — a bundled design-system, domain, and detected-stack search library for evidence-based recommendations.
- **Specifications** — developer-handoff documents with a defined workflow, not a wall of boilerplate.

Everything is token-driven: colors, spacing, shape, depth, and type come from `tokens.json`, never raw values. The bundled audit script (`scripts/design_audit.py`) flags source-review candidates, and the design library (`assets/design-library.json` + `scripts/design_library.py`) indexes internal resources without loading them all into context.

## When to use it

Use for websites, apps, components, creative direction, screenshot studies, redesigns, accessibility, design systems, and developer handoffs. Not for prose-only editing (that's writing work), backend-only work, or AI-authorship detection.

## What's inside

```
SKILL.md                  # Hub: contract, modes, workflow
README.md                 # This design system reference (used by the skill itself)
tokens.json               # Design tokens — themes, type, spacing, color
components/               # Pattern guides: hero, nav, footer, feature, CTA, heading, proof
scripts/design_audit.py   # Source audit
scripts/design_library.py # Design library access
tests/                    # Python tests for the bundled tooling
references/               # Indicators, quality gates, evidence, workflows
assets/                   # Design library index and reference catalog
```

## Install

This is an [Agent Skill](https://agentskills.io) (a `SKILL.md` package). Clone it into your agent's skills directory:

```bash
git clone https://github.com/Shourya-Thoota/anti-slop-design ~/.claude/skills/anti-slop-design
```

Works with any agent that supports the Agent Skills format (Claude Code, Perplexity Computer, and others). No dependencies beyond Python 3 for the optional audit and library scripts.

## License

[MIT](LICENSE) — Copyright (c) 2026 Pansophy LLC.

---

# Design system reference

Use this system to build interfaces and copy that read as made by a person, not generated. Pick one theme, bind every value to a token, and run the checks at the end before you hand anything back.

## How to apply the system

- For a bundled-theme implementation, set `data-theme` on `<html>` to the selected `specimen`, `midnight`, `cobalt`, `carnival`, `lumen`, `hum`, or `grid`. Choose from the product brief; do not default every project to `specimen` or rotate themes merely for variety. Preserve an existing brand, or define justified tokens when none of these themes fits. Keep one coherent system inside a product.
- Reference tokens by name. Colors come from `color-*`, spacing from `space-*`, shape from `radius-*` and `rule-*`, depth from `shadow-card`. Never write a raw hex, `rgb()`, `oklch()` or a `font-family` string in a component. If you need a value that does not exist, add it as a token first.
- Fonts are hosted on Google Fonts and not bundled. Load the families your theme names, and keep to three families per page: one display, one body, and an optional outlier (the mono) used in two places at most.
- Set a theme's fonts from its keys in the table: `font-<key>` for each. Where a column shows `display`, `body` or `mono` with no suffix, use that default. Midnight, Hum and Grid set display text in their body key.
- Build components from the pattern guides in `components/`, grouped Hero, Navigation, Footer, Features, Calls to action, Section heads and Trust and proof. Pick a pattern whose "Use when" matches the brief. Do not reuse the same hero, three-feature, CTA, footer rhythm on two pages. The guides use the tokens here, plus the shared utility and hook classes in `components/bundle.css`.

| Theme | Paper | Display key | Body key | Mono key | Shape |
| --- | --- | --- | --- | --- | --- |
| `specimen` | warm oat, light | `display` (Fraunces) | `body` (Geist) | `mono` (Geist Mono) | square, no shadow |
| `midnight` | cool charcoal, dark | `body` (Geist) | `body` (Geist) | `mono` (Geist Mono) | square, no shadow |
| `cobalt` | cool white, light | `display-cobalt` (Space Grotesk) | `body-cobalt` (Inter) | `mono-jetbrains` (JetBrains Mono) | 10px cards, 6px pills |
| `carnival` | tinted pink-cream, light | `display-carnival` (Big Shoulders Display) | `body-carnival` (DM Sans) | `mono-jetbrains` (JetBrains Mono) | 8px cards, pill, hard offset shadow, 2px rules |
| `lumen` | near-black violet, dark | `display-lumen` (Instrument Serif) | `body` (Geist) | `mono-jetbrains` (JetBrains Mono) | 10px cards, pill, soft deep shadow |
| `hum` | warm cream, light | `body-hum` (Plus Jakarta Sans) | `body-hum` (Plus Jakarta Sans) | `mono-jetbrains` (JetBrains Mono) | 20px cards, pill, soft lift |
| `grid` | cool white, light | `body-grid` (Archivo) | `body-grid` (Archivo) | `mono-grid` (Spline Sans Mono) | square, 1px rules |

Per-theme font stacks are the single source of truth in `tokens.json` under `type.families`; if the table and the file ever disagree, the file wins.

## Color

- Use `color-paper` as the page ground, `color-paper-2` and `color-paper-3` for stepped surfaces, `color-ink` for headings and primary text, `color-ink-2` for body copy, `color-neutral` and `color-muted` for secondary text, `color-rule` and `color-rule-2` for dividers.
- Use one accent, `color-accent`, on no more than 3% of a viewport: links, active state, one primary CTA. A second accent (`color-accent-2`) is allowed in Carnival, Lumen and Hum. A third (`color-accent-3`) exists in Hum only.
- Text on an accent fill uses `color-accent-ink` in Cobalt, Carnival, Lumen, Hum and Grid. In Specimen use `color-ink` on accent fills; in Midnight use `color-paper` (`color-ink` is only 2.0:1 there). In those two themes `color-accent-ink` is a text tone for `color-paper`, not for fills.
- For the bundled themes, use their hue-tinted neutrals rather than arbitrary raw black/white values. Existing brand requirements, high-contrast needs, and genuine black/white editorial or product art are valid exceptions when tokenized and verified; hue matching alone does not establish quality.
- Never use a purple-to-blue gradient, gradient text, aurora blobs or floating orbs as decoration. Lumen's `color-glow` is allowed behind one hero element.
- Color never carries meaning alone. Pair success, error and warning with a word or icon.
- Known contrast gaps in the source, kept exact: `color-muted` is 4.45:1 on `color-paper` in Cobalt; `color-accent` is under 4.5:1 as text on `color-paper` in Specimen, Cobalt, Carnival and Hum; `color-focus` is 2.67:1 in Hum; `color-rule-2` is under 3:1 on `color-paper` in five themes. Use those pairs for fills and large marks only, and add a `color-ink` outline for focus in Hum.

## Typography

- Set display text with the `display` and `display-s` styles in your theme's display key, headings in the `text-*` scale, body in `text-base` or `text-md` in your theme's body key, and mono labels with `label` in your theme's mono key. Read sizes as variables (`--text-md`) or classes (`.text-md`).
- Use the display face at an extreme weight against a quiet body weight. Weight 200 beside 800 reads as a choice; 400 beside 600 reads as a default.
- Headings are always upright. Never italicize a heading or an emphasis word inside one. Carry emphasis with weight, accent color or an underline.
- Keep line length between 45 and 75 characters (`62ch` default). Display line height 1.02 to 1.2, body 1.45 to 1.6.
- Banned as defaults: Inter, Roboto, Open Sans, Lato, Poppins, Montserrat, Raleway, Work Sans, Arial, Helvetica, system-ui. Cobalt's body face is the one exception.
- Use tabular figures for prices, tables and timers. Use real quotes, ellipses and en/em punctuation where typography calls for them, never `--` or `...`.

## Layout, spacing and shape

- Give each layout a primary axis: left-heavy, right-heavy or bottom-weighted. Centre-everything is a default, not a choice. Let one element cross the grid on purpose.
- Space from the scale `space-3xs` to `space-5xl` only. Vary gaps inside a layout; if every gap is `space-lg` the page is a template. Use `gap` for siblings, `margin` only for optical fixes.
- Do not build the three-equal-columns, icon-above-heading feature grid. Vary spans or widths, or use a pattern from `components/` such as a bento or tabular spec sheet.
- Do not nest card in card, put a colored left-border stripe on a card, or put an eyebrow label on every section.
- Take radii from the theme: `radius-card`, `radius-pill`, `radius-input`. Do not mix a round pill into a square theme. Use `rule-card` for borders and `shadow-card` for depth; never glow shadows on dark.
- Prefer CSS Grid for page layout and Flexbox inside components. Use `minmax(0, 1fr)`, not bare `1fr`, for tracks that hold images.
- Stack from `z-base` to `z-tooltip`. Never `z-index: 9999`. Keep in-page sticky elements below `z-sticky-nav`.

## Components and states

- Account for default, hover, `:focus-visible`, `:active`, disabled, loading, error, and success where applicable. Render relevant states in a labeled demo; mark inapplicable states rather than fabricating loading/error semantics for a plain navigation link.
- Focus rings use `color-focus`, solid, 2px or more, 3:1 against the surface. They do not animate in.
- Hit areas are at least 44 by 44px on touch, with 8px between targets. Never rely on hover for a primary action. Icon-only buttons carry an accessible name.
- One primary CTA per view. Secondary actions sit visibly below it in weight.
- Clickable text stays on one line: buttons, nav links, footer links, breadcrumbs, CTAs.
- Do not draw fake browser bars, phone frames, window dots on code blocks or IDE chrome. Use a real screenshot in a `<figure>` with at most a hairline border, or no chrome.
- Use one icon set with one stroke width. Never emoji as a feature icon or as decoration.

## Motion

- Animate `transform` and `opacity` only. Use three durations: 120ms (micro), 220ms (short), 420ms (long). Exits run about 75% of the enter.
- Ease with `cubic-bezier(0.16, 1, 0.3, 1)` entering, `cubic-bezier(0.7, 0, 0.84, 0)` leaving, `cubic-bezier(0.65, 0, 0.35, 1)` for toggles. No bounce or elastic easing on UI.
- Do not use `transition: all`, a global `hover:scale-105`, cursor followers, scroll-triggered fade-up on every block, or auto-rotating carousels with no pause.
- Move one or two things per view with a reason you can state. Under `prefers-reduced-motion: reduce`, collapse spatial motion to an opacity crossfade.

## Content fundamentals

- Never invent a metric, testimonial, logo or customer count. Use the user's real figure, or a labeled placeholder (`metric to confirm`), or choose a layout that needs none. "+47% conversion" and "trusted by 50,000+ teams" are slop the moment they are made up.
- Name buttons with the verb the action performs: `Save changes`, `Create account`, `Copy link`. Not `OK`, `Submit` or `Click here`. Pick one of Delete or Remove, Sign in or Log in, and keep it.
- Label fields with a visible label. Write link text that stands alone (`View pricing plans`).
- Write errors as what happened, why if known, what to do next: `That card was declined. Your bank flagged the charge. Try another card, or contact your bank.` Do not say "Oops" and do not apologize for the user's input.
- Use real names and plausible content in samples. No "John Doe", no startup-cliché product names.

## Writing and editing prose

- Make the minimum effective edit. Keep the writer's vocabulary, cadence, bluntness and humor; a rough draft with a real voice must still sound like the same person afterward. Do not invent claims, stats or examples; ask when something is unclear.
- Lead with the point when the setup adds nothing. Use active voice, concrete verbs, names, numbers and mechanisms. If a sentence could move unchanged to another company or product, cut it or replace it with a fact specific to this one.
- Banned words: delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving.
- Cut these patterns: a binary contrast ("not X, it's Y"), throat-clearing openers ("Here's the thing"), faux-insight setups ("what most people miss"), colon reveals ("The best part: it learns"), trailing "-ing" analysis ("highlighting the team's commitment"), importance puffery, weasel attribution ("experts agree"), synonym cycling, negative listing, dramatic fragments, rhetorical setups, fake-profound closing lines and summary recaps.
- Use em dashes rarely: none in short copy, one or two in a long draft. Do not add emoji to headings, bold mid-sentence, or bullets where two sentences read better.
- To audit without editing, name each pattern found, quote the line, give the fix in a few words, and do not guess whether AI wrote it. For an edit, return the full draft and a short list of what changed.

## Self-checks before handing back

- Score the output 1 to 5 on Philosophy, Hierarchy, Execution, Specificity, Restraint and Variety. Revise anything under 3.
- Check at 320, 375, 414 and 768px: no horizontal scroll (set `overflow-x: clip` on `html` and `body`, never `hidden`), display headings wrap with `overflow-wrap: anywhere; min-width: 0`.
- Check body text contrast at 4.5:1 and large text and controls at 3:1 in the theme you chose, using the pairs listed under Color.
- Check that no component hard-codes a color, font or spacing value, that no heading is italic, and that no number or quote on the page is made up.
- When rules conflict, settle them in this order: accessibility, touch and interaction, performance, style, then layout, typography and motion.

## Reference data

`assets/Reference/` holds lookup tables for choosing a style when no theme fits: `colors.csv` (palettes by product type), `typography.csv` (font pairings), `styles.csv` (visual styles with when to use and avoid), `ux-guidelines.csv` (interaction rules with do and don't). Read a row, then express it as tokens in this system's format; do not paste its hex values into components.
