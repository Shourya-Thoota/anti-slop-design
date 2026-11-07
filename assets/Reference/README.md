Lookup tables for picking a visual direction when none of the seven themes fits. Read a row, then express the choice as tokens in this system; do not paste a row's hex values or CSS into components.

- `colors.csv`: one palette per product type (primary, accent, background, foreground, border, destructive, ring) with notes. Use as a starting point for a new theme's `color-*` tokens and check contrast before adopting.
- `typography.csv`: heading and body font pairings with mood, best-for and Google Fonts import. Several pairings use Inter, Roboto or Playfair Display, which this system's README bans as defaults; take the mood and role split, choose another face.
- `styles.csv`: visual styles (minimalism, brutalism, glass and more) with best-for, do-not-use-for, accessibility and performance notes. Check each against the README's rules on glow, gradients and decoration before use.
- `ux-guidelines.csv`: interaction and usability rules with a do, a don't and a severity. Apply the High-severity rows by default.
