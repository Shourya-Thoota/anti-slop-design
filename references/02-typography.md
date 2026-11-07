# Typography Standards

## Type Scale

Establish a modular type scale and apply it consistently. Do not choose font sizes arbitrarily per element.

| Token | Size | Usage | Line Height |
|---|---|---|---|
| Display XL | 48px / 3rem | Hero headlines, major announcements | 1.1 |
| Display L | 32px / 2rem | Page titles, section heroes | 1.15 |
| H1 | 24px / 1.5rem | Major section headings | 1.2 |
| H2 | 20px / 1.25rem | Subsection headings | 1.25 |
| H3 | 16px / 1rem | Sub-subsection headings, card titles | 1.3 |
| Body | 14px / 0.875rem | Primary body text | 1.6 |
| Body Small | 12px / 0.75rem | Captions, metadata, footnotes | 1.5 |
| Label | 11px / 0.6875rem | Tags, badges, buttons | 1.4 |

Scale rationale: Based on a 1.25 major third ratio. Every size is mathematically related. No arbitrary values.

## Font Pairing

Choose 1-2 typefaces with a documented rationale. Document the pairing logic.

| Role | Recommendation | Example Pairings |
|---|---|---|
| Body text | Clean, highly readable sans-serif | Geist, Satoshi, Inter (with justification), Manrope |
| Display/headlines | Either same family at heavier weight OR contrasting serif | Playfair Display, Newsreader, Fraunces |
| Code/monospace | Purpose-built monospace | JetBrains Mono, IBM Plex Mono, Fira Code |

Rules:
- One typeface for body + one for display is the maximum without explicit justification
- If using one family, leverage weight variation (400/600/700/900) to create hierarchy
- Never use more than two typefaces in a single interface

## Line Height and Spacing

Line height must respond to size and context, not be a global constant.

| Context | Line Height | Rationale |
|---|---|---|
| Large display (32px+) | 1.1 - 1.15 | Tight tracking for impact; descenders need less room |
| Headings (16-24px) | 1.2 - 1.3 | Slightly loose for readability without losing density |
| Body text (14px) | 1.5 - 1.6 | Comfortable reading; accommodates descenders and diacritics |
| Small text (12px and below) | 1.5 | Minimum for legibility at small sizes |
| All-caps labels | 1.2 - 1.3 | No descenders means tighter is acceptable |

Paragraph spacing: 0.5em to 0.75em after paragraphs. Never use double line breaks.

## Tracking and Letter Spacing

| Context | Tracking | Rationale |
|---|---|---|
| All-caps text | +5% to +15% | Prevents visual tightness; varies by typeface |
| Body text | Default (0%) | Only adjust if the specific face requires it |
| Large display | -2% to -5% | Tightening adds weight and presence |
| Labels and UI text | Default to +2% | Slight openness aids scannability |

## Measure and Line Length

- Optimal measure: 60-75 characters per line for body text
- Maximum measure: 90 characters
- Minimum measure: 45 characters
- Constrain text containers, not font size, to control measure

## Typography Bans

| Banned Pattern | Why | Replacement Strategy |
|---|---|---|
| Inter, Roboto, or Arial as unexamined headline face | Default font signals no choice was made | Source from Fontshare, Google Fonts, or local library; pick something with a point of view |
| System font stack for everything | Erases brand personality | Choose 1-2 typefaces with a rationale; document the pairing logic |
| Font size chosen arbitrarily per element | No system, no hierarchy | Build a modular type scale and apply it consistently |
| Line height at 1.5 everywhere | Ignores measure and x-height | Adjust by size: tighter for large display, looser for small body |
| Tracking at default for all caps | Too tight or too loose | Increase tracking for all-caps by 5-15% depending on face |
| More than two typefaces without justification | Visual chaos | One face for body, one for display; or one family with multiple weights |
