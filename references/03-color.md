# Color and Contrast Guidelines

## Color Palette Structure

Use a dominant-tone palette. Every palette needs a point of view.

| Role | Proportion | Purpose |
|---|---|---|
| Dominant | 60% | Backgrounds, primary surfaces, the "feel" of the product |
| Secondary | 30% | Cards, elevated surfaces, sidebars, alternate sections |
| Accent | 10% | CTAs, active states, key data points, focus indicators |

Rules:
- One dominant tone + one sharp accent is the minimum for a distinctive palette
- Evenly-distributed palettes (no dominant tone) are timid and read as slop
- Gray as the only neutral is cold and lifeless

## Base Palette Example

| Token | Hex | Usage |
|---|---|---|
| Background | `#faf9f7` | Warm off-white primary background |
| Surface | `#f0eeeb` | Card and elevated surface background |
| Surface Alt | `#e8e5e1` | Alternate section backgrounds |
| Primary | `#1a1a1e` | Primary text, strong borders |
| Secondary | `#5a5a5e` | Secondary text, muted elements |
| Muted | `#8a8a8e` | Captions, placeholders, disabled states |
| Accent | `#c45c4a` | CTAs, links, active states, key indicators |
| Accent Hover | `#a84d3d` | Accent hover state |
| Border | `#d0d0d5` | Subtle separators, input borders |

## Semantic Colors

| State | Hex | Usage | Contrast Requirement |
|---|---|---|---|
| Success | `#2d7d46` | Completed actions, positive trends | 4.5:1 on white |
| Error | `#c9372d` | Failures, validation errors, destructive actions | 4.5:1 on white |
| Warning | `#b35900` | Cautions, pending states, non-blocking issues | 4.5:1 on white |
| Info | `#2563eb` | Neutral announcements, tips, help text | 4.5:1 on white |

Semantic color rules:
- Never rely on color alone to convey state. Pair with icon, text, or pattern.
- Success and error must be distinguishable by form AND color.

## WCAG Contrast Requirements

| Element | Minimum Ratio | Level |
|---|---|---|
| Normal text (< 18pt or < 14pt bold) | 4.5:1 | AA |
| Large text (>= 18pt or >= 14pt bold) | 3:1 | AA |
| UI components and graphical objects | 3:1 | AA |
| Normal text | 7:1 | AAA (recommended) |

Rules:
- Do not rely on contrast-checker rounding: 4.4983:1 is a fail, not a pass
- Test all color combinations, not just primary text on primary background
- Test focus indicators, placeholder text, and disabled states separately

## Neutral Guidance

- **Warm neutrals** over cool grays: Add slight yellow, red, or orange tint to grays
- **Near-black** over pure black: Use `#0a0a0f`, `#111111`, or `#1a1a1e` instead of `#000000`
- **Warm white** over pure white: Use `#faf9f7`, `#f5f5f0` instead of `#ffffff` as the only background
- Tinted grays carry atmosphere; pure grays read as unfinished

## Dark Mode

- Ship light mode first. Add dark mode only when requested or when the product is used at night
- Dark mode is not a default — it is a feature that requires justification
- When implemented, dark mode must maintain the same contrast ratios and semantic color meanings

## Color Bans

| Banned Pattern | Why | Replacement Strategy |
|---|---|---|
| Purple/indigo-to-blue gradient (Tailwind cascade) | The most recognizable AI slop signature | Choose a dominant tone specific to the product; add one sharp accent |
| Evenly-distributed palettes (no dominant tone) | Timid, no point of view | One dominant (60%), one secondary (30%), one accent (10%) |
| Gray as the only neutral | Cold and lifeless | Warm neutrals, tinted grays, or near-black with hue |
| Decorative color bars / accent lines under titles | Recognized AI-generation tell | Use whitespace, weight, or size to create hierarchy instead |
| Dark mode nobody asked for | Adds complexity without user need | Ship light mode first; add dark mode only when requested |
| Pure black (`#000000`) backgrounds | Harsh, causes eye strain | Use near-black with warmth (`#0a0a0f`, `#111111`) |
| Pure white (`#ffffff`) as the only background | Flat and sterile | Use warm white, off-white, or subtle tinted backgrounds |
| Gradient backgrounds as default decoration | Overused, often meaningless | Use only when the gradient communicates something (depth, atmosphere, brand) |
| Glassmorphism / frosted glass without purpose | Decoration without information | Use when layering genuinely needs depth separation; otherwise use solid surfaces |
