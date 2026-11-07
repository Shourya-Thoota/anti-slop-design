# Component Guidelines

## Button Anatomy and States

Every button must have designed states. A button without states is unfinished.

### Required States

| State | Visual Treatment | Purpose |
|---|---|---|
| Default | Solid fill or outlined, clearly clickable | Resting state |
| Hover | Slight darkening/lightening, cursor pointer | Indicates interactivity |
| Focus-visible | Distinct ring or outline (not just color change) | Keyboard navigation indicator |
| Active/Pressed | Darker shade, slight downward shift | Indicates activation |
| Loading | Spinner or progress inside button, disabled interaction | Indicates ongoing action |
| Disabled | Reduced opacity (not grayed out), no pointer events | Indicates unavailable action |
| Error | Red tint or icon, recovery option visible | Indicates failed action |

### Button Content Rules

- Button text must say what happens: "Save changes", "Send message", "Delete file"
- Never use "Learn more", "Click here", or "Submit" as button text
- One primary action per view. Multiple primary actions create decision paralysis
- Secondary actions must not compete visually with primary

### Button Types

| Type | Use Case | Visual Treatment |
|---|---|---|
| Primary | Main CTA, most important action | Solid accent color, high contrast |
| Secondary | Alternative action, less critical | Outlined or ghost style |
| Tertiary | Minor action, text-only | Text with subtle underline or icon |
| Destructive | Delete, remove, irreversible action | Red/error color, requires confirmation |

## Form Input Standards

### Labels

- Labels must always be visible, not placeholder-only
- Placeholder text shows format or example, never replaces the label
- Required fields: marked with asterisk or "Required" text
- Optional fields: no mark (not "Optional" on every field)

### Error States

- Error messages must say what went wrong AND how to fix it
- Never use "Invalid input" or "Error" alone
- Position error text adjacent to the field, not in a generic banner
- Use color + icon + text to indicate errors (never color alone)

### Help Text

- Help text guides; it does not apologize
- Use for format hints: "MM/DD/YYYY" not "Please enter a valid date"
- Keep help text visible, not in a tooltip

## Card and Container Patterns

### Card Rules

- Cards should not all look identical. Vary size, prominence, or treatment based on content importance
- Internal padding should relate to content density, not be a global constant
- Avoid cards for content that does not need containment — let it breathe
- Cards need elevation strategy: flat, bordered, or shadowed — chosen, not defaulted

### Elevation

| Level | Treatment | Usage |
|---|---|---|
| 0 | Flat, no border | Content that needs no separation |
| 1 | Subtle border (1px) | Grouped content, form sections |
| 2 | Light shadow | Interactive cards, dropdowns |
| 3 | Medium shadow | Modals, popovers |
| 4 | Heavy shadow | Full-screen overlays, toasts |

## Navigation Structure

### Desktop Navigation

- Show primary links directly. Hamburger only when space demands
- Navigation labels describe what the user finds, not what the company calls it
- Current page clearly indicated (not just color — use weight or underline)
- Footer contains useful links, not just a repeat of the header

### Mobile Navigation

- Hamburger with clear categories
- Bottom tab bar for apps with 3-5 primary destinations
- Never hide the only path to critical features behind a menu

## Component Bans

| Banned Pattern | Why | Replacement Strategy |
|---|---|---|
| Badge pills ("New", "Beta") as decoration | Fake urgency, often meaningless | Use only for genuine status; prefer text or simple labels |
| Sparkle/star/magic icons for AI features | Cliched, tells the user nothing | Use icons that describe what the feature does, not that it uses AI |
| Emoji as iconography | Inconsistent across platforms, unprofessional | Use single-weight vector SVG icons at consistent stroke width |
| Placeholder avatars with generic silhouettes | Signals fake testimonials or unfinished work | Use real photos, initials in colored circles, or remove entirely |
| Star ratings with no review count | Unverifiable social proof | Show real reviews with real names, or remove the rating |
| "Trusted by" logos without partnerships | False social proof | Use only real, verifiable logos with permission |
| Pricing cards with three tiers | Default SaaS template | Match tiers to actual offerings; use 2, 4, or a custom structure |
| Toggle switches for binary settings that look like actions | Confuses affordance | Use buttons for actions, toggles for state changes |
| Tooltips as the only way to see values | Hides information behind interaction | Show critical values directly; use tooltips for supplementary info |
| Infinite scroll without alternative | Inaccessible, breaks search | Offer pagination or load-more button as default |
