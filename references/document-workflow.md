# Anti-Slop Design System

Generate a professionally styled DOCX design system document that combines positive design standards with prohibited patterns. The document serves as both a reference guide and a quality gate for design work.

## Reference Source

- **Type**: Previous-round artifact + judge feedback refinement
- **Artifact type**: DOCX
- **Reference File Type**: DOCX
- **Primary output**: Markdown unless the user explicitly requests DOCX or PDF
- **Supported outputs**: DOCX, PDF

## Visual Style Contract

See [`style_contract.md`](style_contract.md) for complete visual specifications.

### Summary

- **Page**: A4 (210 x 297mm), body margins 1in all sides; cover and back cover are full-bleed (0 margins) with background images
- **Color palette**: Deep charcoal near-black (`#2d2d30`) body text, warm coral accent (`#c45c4a`) for Heading 1 and table rules, medium gray (`#5a5a5e`) for Heading 2, light gray (`#8a8a8e`) for captions and secondary text, warm off-white (`#f5f5f7`) table header background, light border (`#d0d0d5`)
- **Typography**: Body uses a distinctive modern sans-serif (e.g., Geist, Inter with explicit justification, or similar). Avoid default Calibri. Heading 1 at 20pt bold coral. Heading 2 at 14pt bold dark. Heading 3 at 12pt medium gray. Body at 11pt dark with 1.15 line spacing. Cover text uses large white/light text over dark background.
- **Tables**: Coral top and bottom rules (8pt), light gray horizontal inner borders (4pt), warm off-white header background, left-aligned content
- **Cover page**: Full-bleed dark background with geometric reddish-coral accent strip on left third, large bold white title, subtitle in light gray, version/date at bottom
- **Back cover**: Matching dark background with centered white tagline, coral accent strip on right side
- **Running header**: Right-aligned "Anti-Slop Design System" in light gray, small caps
- **Page numbers**: Centered footer in light gray
- **TOC**: No placeholder instructional text. Clean dotted-leader entries with page numbers. Auto-update on open.

## Document Structure Contract

The document **must** contain the following explicitly titled sections in this order:

1. **Cover Page** — Full-bleed dark background with geometric accent, title, subtitle, version/date
2. **Table of Contents** — Clean, no placeholder text, auto-updating page numbers
3. **Core Design Principles** — Introduction, What Is Slop, Why Prohibitions Beat Aspirations, How to Use This Document, The Anti-Slop Hierarchy of Needs (5 levels), The Craftsmanship Standard (5 criteria)
4. **Typography Standards** — Positive type scale definitions, recommended font pairing logic, line height ratios, paragraph spacing rules, tracking guidance, AND the Typography Bans table
5. **Color and Contrast Guidelines** — Defined color palette structure (dominant 60%/secondary 30%/accent 10%), explicit WCAG contrast ratio requirements, semantic color usage (success, error, warning, info), warm neutral guidance, AND the Color Bans table
6. **Spacing and Layout Rules** — Grid system definition, spacing scale (4px, 8px, 16px, 24px, 32px, 48px, 64px), margin/padding standards, measure/line-length rules, responsive breakpoint philosophy, AND the Layout Bans table
7. **Component Guidelines** — Button anatomy and states (default, hover, focus, active, loading, disabled), form input standards, card/container patterns, navigation structure, AND the Component Bans table
8. **Imagery and Iconography** — Image quality standards, sizing and treatment rules, icon style consistency (single-weight SVG, stroke width), photography guidelines, AND the Data/Content Bans table
9. **Motion and Animation Standards** — Motion principles, timing guidance (150-200ms snappy, 400-600ms elegant), easing character, prefers-reduced-motion rules, AND the Motion Bans table
10. **Copywriting and Content Standards** — Headline rules, body copy guidance, CTA standards, testimonial requirements, error/empty state copy, microcopy rules, AND the Copy Bans table
11. **Code Quality and Accessibility** — Semantic HTML requirements, design token architecture, WCAG 2.1 AA compliance, keyboard navigation, touch targets, focus indicators, AND the Code Bans table
12. **Product Types and Visual Directions** — Six Personality Axes table, category starting positions (8 product types), direction commitment guidance
13. **Liveliness Toolkit** — Three Dials (Energy, Rhythm, Motion), Design Read checklist, common failures and fixes
14. **Delivery Gate Checklist** — Block A (Correctness), Block B (Anti-Slop Rules), Block C (Craftsmanship), Block D (Liveliness), with scoring and audit mode
15. **Best Practices and Examples** — Concrete before/after scenarios showing sloppy vs. intentional design across typography, color, layout, components, and copy
16. **Back Cover** — Matching cover style with tagline

Each positive-guidelines section must precede its corresponding bans table within the same section. Do not isolate all bans into a single "Banned Patterns Database" section.

## Content Requirements

### Positive Guidelines (Required)

Every design dimension section must include **both** positive standards and negative prohibitions:

- **Typography Standards**: Define a modular type scale (e.g., 12/14/16/20/24/32/48px), specify font pairing rationale, line-height ratios (1.2 for display, 1.5 for body, 1.6 for small), tracking rules for all-caps, maximum two typefaces
- **Color and Contrast Guidelines**: 60/30/10 distribution rule, WCAG AA minimums (4.5:1 normal, 3:1 large), semantic colors defined, warm neutrals preferred, no pure black/white
- **Spacing and Layout Rules**: 4px base unit, spacing scale multiples, grid system (8px or 12px), measure constraint (60-75 characters), breakpoint philosophy
- **Component Guidelines**: Button states fully enumerated, form label visibility, card padding relative to content, navigation label rules
- **Imagery and Iconography**: SVG single-weight stroke consistency, icon function over decoration, real photography over stock, screenshot authenticity

### Before/After Examples (Required)

The "Best Practices and Examples" section must contain at least **5 concrete before/after scenarios**:

| Scenario | Slop (Before) | Intentional (After) |
|---|---|---|
| Hero Section | Centered badge → heading → gray subheading → two buttons | Asymmetric split layout with product image bleeding edge, one bold headline left-aligned |
| Feature Cards | Three identical cards with icon + heading + body | Two prominent cards + one detailed case study card, varying sizes by importance |
| Color Usage | Purple-to-blue gradient background | Single warm neutral background with one sharp accent color for CTAs only |
| Typography | Inter at default weights everywhere | Paired typeface with display weight for headlines, regular for body, documented rationale |
| Buttons | "Learn More" pill button | "Start Free Trial" rectangular button with loading and error states designed |

### TOC Requirements for requested DOCX

- Use an auto-updating TOC field (`TOC \o "1-3" \h \z \u`)
- **Never** include placeholder instructional text like "Right-click the TOC and select Update Field"
- Enable `UpdateFieldsOnOpen` in document settings
- Refresh the native TOC field's cached result against actual pagination; never add an independent handwritten fallback TOC or fabricate page numbers. If a renderer cannot update the cache, report that limitation.

### Font Strategy

- Use a distinctive modern sans-serif font. Preferred: **Geist**, **Satoshi**, or **Manrope** for body; pair with **Playfair Display** or **Newsreader** for display if a serif contrast is appropriate
- If embedding is problematic, use **Calibri** only as a fallback, but document the preferred font choice
- CJK compatibility: Use **Noto Sans CJK** or **Microsoft YaHei** for East Asian text when needed
- Font must be applied consistently across all text elements including headings, body, tables, captions, headers, and footers

## Workflow

1. **Read reference files** for detailed content per section:
   - [`01-core-principles.md`](01-core-principles.md) — Philosophy, hierarchy, craftsmanship
   - [`02-typography.md`](02-typography.md) — Type scale, font pairing, spacing, bans
   - [`03-color.md`](03-color.md) — Palette structure, contrast, semantic colors, bans
   - [`04-spacing-layout.md`](04-spacing-layout.md) — Grid, spacing scale, measure, bans
   - [`05-components.md`](05-components.md) — Button, form, card, nav anatomy, bans
   - [`06-imagery.md`](06-imagery.md) — Icon standards, photography, treatment, bans
   - [`07-motion.md`](07-motion.md) — Timing, easing, principles, bans
   - [`08-copywriting.md`](08-copywriting.md) — Headlines, CTAs, microcopy, bans
   - [`09-code-a11y.md`](09-code-a11y.md) — Semantic HTML, tokens, WCAG, bans
   - [`10-product-types.md`](10-product-types.md) — Personality axes, categories
   - [`11-liveliness.md`](11-liveliness.md) — Three dials, Design Read
   - [`12-delivery-gate.md`](12-delivery-gate.md) — Checklist, audit mode
   - [`13-examples.md`](13-examples.md) — Before/after scenarios
   - [`style_contract.md`](style_contract.md) — Visual specifications
   - [`structure_contract.md`](structure_contract.md) — Section ordering and requirements

2. **Generate cover/backcover background images** as full-page PNGs (dark charcoal with coral geometric accent)

3. **Build the DOCX** following the style contract and structure contract exactly

4. **Validate**: Ensure all 16 sections are present, TOC has no placeholder text, before/after examples exist, positive guidelines accompany every bans table
