# Code Quality and Accessibility

## Semantic HTML

Use correct elements for correct purposes:

| Element | Use For | Do Not Use For |
|---|---|---|
| `<button>` | Actions that trigger something | Navigation (use `<a>`) |
| `<a>` | Navigation to another page/section | Actions (use `<button>`) |
| `<nav>` | Primary and secondary navigation | Generic container |
| `<main>` | Primary content of the page | Secondary content |
| `<article>` | Self-contained content (post, card) | Layout wrapper |
| `<section>` | Thematic grouping with heading | Generic div replacement |
| `<header>` | Introductory content or nav | Random top area |
| `<footer>` | Footer content for section/page | Bottom of any container |
| `<aside>` | Tangentially related content | Sidebar with primary content |

## Design Token Architecture

Use design tokens (CSS custom properties) for all visual values:

```
--color-background: #faf9f7;
--color-surface: #f0eeeb;
--color-primary: #1a1a1e;
--color-accent: #c45c4a;
--space-1: 4px;
--space-2: 8px;
--font-body: 'Geist', sans-serif;
--radius-sm: 4px;
--radius-md: 8px;
```

Rules:
- No magic numbers. Every value should be a token or a documented calculation
- Group related styles. Avoid scattering properties across selectors
- Use CSS custom properties or a design token system
- Document the rationale for every token

## Accessibility Requirements

### Contrast

- Text meets WCAG 2.1 AA: 4.5:1 for normal text, 3:1 for large text
- UI components meet 3:1 against adjacent colors
- Do not rely on contrast-checker rounding: 4.4983:1 is a fail, not a pass

### Keyboard Navigation

- All interactive elements reachable by Tab
- Tab order follows visual order
- Focus indicators visible and styled distinctly from hover
- No keyboard traps

### Screen Readers

- Semantic HTML provides the structure
- ARIA used only when HTML semantics are insufficient
- Dynamic content announced with live regions
- Skip links provided for repetitive navigation

### Touch Targets

- Minimum 44x44pt for touch targets (iOS) or 48x48dp (Android)
- Adequate spacing between adjacent targets
- Gestures have alternatives (buttons for swipe actions)

### Motion

- Respect `prefers-reduced-motion`
- No auto-playing content without pause control
- No flashing content (more than 3 flashes per second)

## Performance

- Load above-the-fold content first
- Lazy-load images below the fold
- Avoid layout shift: size images and containers before content loads
- Minimize repaint and reflow in animations

## Code Bans

| Banned Pattern | Why | Replacement Strategy |
|---|---|---|
| Inline styles on components | Unmaintainable, breaks theming | Use CSS custom properties or design tokens |
| Magic numbers without comment | Unmaintainable | Use named constants or tokens; document rationale |
| `!important` in CSS | Overrides architecture | Fix specificity issues at the source |
| Unused imports / dead code | Clutter, confusion | Clean up before committing |
| Comments that state the obvious (`// increment counter`) | Noise | Remove or replace with *why*, not *what* |
| AI-generated comments with no value | Slop in code | Remove obvious comments; keep only explanatory ones |
| Hardcoded colors instead of tokens | Breaks theming | Use design token references |
| No semantic HTML | Accessibility failure | Use correct elements: button, a, nav, main, article |
| Missing alt text on images | Accessibility failure | Write descriptive alt text, or `alt=""` for decorative images |
| No focus styles | Keyboard navigation fails | Style `:focus-visible` with clear, visible indicators |
