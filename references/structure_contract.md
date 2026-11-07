# Structure Contract

## Required Section Order

The document MUST contain these sections in exact order:

1. **Cover Page** (full-bleed, no page number)
2. **Table of Contents** (clean, no placeholder text, starts on new page)
3. **Core Design Principles**
4. **Typography Standards**
5. **Color and Contrast Guidelines**
6. **Spacing and Layout Rules**
7. **Component Guidelines**
8. **Imagery and Iconography**
9. **Motion and Animation Standards**
10. **Copywriting and Content Standards**
11. **Code Quality and Accessibility**
12. **Product Types and Visual Directions**
13. **Liveliness Toolkit**
14. **Delivery Gate Checklist**
15. **Best Practices and Examples**
16. **Back Cover** (full-bleed, no page number)

## Section Content Requirements

### Sections 4-9 (Design Dimension Sections)

Each of these sections MUST follow this pattern:

1. **Positive Guidelines subsection(s)** — Define what TO do (standards, scales, rules)
2. **Bans table** — The prohibited patterns with Why and Replacement Strategy columns

Example structure for Typography Standards:
- Heading 1: Typography Standards
  - Heading 2: Type Scale
    - Paragraph: Define the scale with specific px values
  - Heading 2: Font Pairing
    - Paragraph: How to choose and rationale
  - Heading 2: Line Height and Spacing
    - Paragraph: Ratios by context
  - Heading 2: Typography Bans
    - Table: Banned Pattern | Why | Replacement Strategy

### Section 15 (Best Practices and Examples)

Must contain at minimum 5 before/after scenarios in table format:

| Scenario | Slop (Before) | Intentional (After) |
|---|---|---|
| [Name] | [Description of sloppy pattern] | [Description of intentional replacement] |

Each scenario must cover a different design dimension (typography, color, layout, component, copy).

## Heading Hierarchy

- **Heading 1** (20pt coral): Major section titles (16 sections)
- **Heading 2** (14pt dark): Subsections within each major section
- **Heading 3** (12pt medium): Sub-subsections where needed

TOC captures Heading 1 and Heading 2 levels.

## Page Break Rules

- Cover page: Section break (next page) after
- TOC: Section break (next page) after
- Each major section: Starts on new page OR continues from previous if space permits
- Back cover: Final section, no break after

## TOC Requirements

- Field code: `TOC \o "1-3" \h \z \u`
- `UpdateFieldsOnOpen` enabled in document settings
- **NO placeholder instructional text** anywhere on the TOC page
- Use the native field's refreshed cached result as the visible fallback. Do not add independent static entries or invent page numbers.
- Dotted leaders with right-aligned page numbers

## Cross-Reference Rules

- Delivery Gate Checklist references all prior sections
- Each bans table references its positive guidelines section
- Before/after examples reference specific bans where applicable
