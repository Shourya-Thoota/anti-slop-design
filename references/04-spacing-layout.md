# Spacing and Layout Rules

## Grid System

Use a consistent grid system as the foundation for all layouts.

| Grid Type | Use Case | Base Unit |
|---|---|---|
| 8px grid | Most digital products, web apps, dashboards | 8px |
| 12px grid | Editorial layouts, content-heavy sites | 12px |
| 4px grid | Dense interfaces, design tools, data-heavy apps | 4px |

Rules:
- All spacing values must be multiples of the base unit
- Column count: 12 for general use, 8 for simpler layouts, 16 for complex dashboards
- Gutter width: 24px standard, 16px for dense layouts, 32px for spacious layouts
- Margin width: Equal to or greater than gutter width

## Spacing Scale

| Token | Value | Usage |
|---|---|---|
| Space 0 | 0px | No spacing |
| Space 1 | 4px | Tight internal padding, icon gaps |
| Space 2 | 8px | Button padding, inline element gaps |
| Space 3 | 16px | Card internal padding, form field gaps |
| Space 4 | 24px | Section internal padding, related content groups |
| Space 5 | 32px | Major component separation |
| Space 6 | 48px | Section breaks within a page |
| Space 7 | 64px | Major section separation |
| Space 8 | 96px | Page-level section breaks |
| Space 9 | 128px | Hero section padding, major divides |

Spacing rules:
- Related content = tighter spacing (Space 2-3)
- Unrelated sections = looser spacing (Space 6-8)
- Vary spacing to create rhythm and visual pace
- Evenly-spaced sections with identical padding read as mechanical and templated

## Margin and Padding Standards

| Element | Padding | Margin |
|---|---|---|
| Card | Space 3-4 (16-24px) | Space 3 (16px) |
| Button | Space 2 vertical, Space 3 horizontal (8px/16px) | Space 2 (8px) |
| Input field | Space 2 vertical, Space 3 horizontal | Space 3 (16px) |
| Section container | Space 6-8 (48-96px) vertical | 0 (uses its own padding) |
| Page wrapper | Space 4-6 (24-48px) horizontal | Auto-centered |

## Measure and Line Length

- Optimal reading measure: 60-75 characters per line
- Maximum: 90 characters
- Minimum: 45 characters
- Achieve measure control through container width, not font size reduction
- On wide screens, use sidebars, pull quotes, or whitespace rather than stretching text

## Breakpoint Philosophy

- Design for content, not devices. Break when the layout breaks, not at device widths
- Use a limited set of breakpoints (3-4 max) and document them
- Fluid layouts between breakpoints, not just stacked versions

| Breakpoint | Width | Purpose |
|---|---|---|
| Small | < 640px | Mobile phones |
| Medium | 640-1024px | Tablets, small laptops |
| Large | 1024-1440px | Desktops |
| XLarge | > 1440px | Large monitors |

## Layout Bans

| Banned Pattern | Why | Replacement Strategy |
|---|---|---|
| Centered hero: badge pill -> heading -> gray subheading -> two buttons | The most common AI landing page template | Break the pattern: left-aligned, split layout, or full-bleed image with overlay text |
| Three identical feature cards in a row | Template-filling, no content reason | Use 2, 4, or an asymmetric grid; vary card sizes based on content importance |
| Uniform 1px gray border on every card | Default decoration, no intention | Use shadows, background color shifts, or spacing to separate; vary border weight if used |
| Evenly-spaced sections with identical padding | Mechanical, no rhythm | Vary spacing to create pace; tighter for related content, looser for section breaks |
| Full-width content on all breakpoints | Ignores reading comfort | Constrain text measure to 60-75 characters; use sidebars or whitespace for wider screens |
| Every page looks like a landing page | One pattern applied everywhere | Match layout to content type: editorial, dashboard, gallery, form |
| Sticky header with drop shadow on scroll | Overused pattern | Use only when navigation needs to remain accessible; consider hide-on-scroll |
| Hamburger menu on desktop | Hides navigation unnecessarily | Show primary links directly; use hamburger only on mobile |
