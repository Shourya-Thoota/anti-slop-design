# Integrating the supplied patterns

Read alongside the root README before implementing UI. The theme data is preserved from the uploaded bundle; examples are sketches and do not override the rules.

- Use the root README over contradictory pattern styling, and accessibility over both. H8 includes fake browser chrome: use its documented hairline or no-frame option with a real screenshot instead. Lumen permits one hero glow, not general glow shadows.
- Convert raw spacing, shadow, duration, font-size, and z-index values in snippets into named tokens before reuse. Structural values such as zero, percentages, and grid fractions need not become design tokens. Define missing custom properties before use; `tokens.css` mentioned by patterns is generated project output, not a bundled file.
- Preserve JSON token values as the source palette, but choose accessible foreground/background pairs for each rendered use. Cobalt's accent-ink on accent is documented below 4.5:1; do not use that pair for normal-sized button text. Use an ink/paper CTA or define an accessible accent variant token and verify it.
- Cobalt muted text below 4.5:1 is not safe merely because it is 16px. Use neutral or ink-2 for normal text and verify contrast. Hum needs the documented ink focus outline. Low-contrast rule tokens must not be a control's only boundary.
- Replace sample numbers, quotes, addresses, and product names before delivery. Supply working destinations, visible form labels, meaningful accessible names, image alternatives, and keyboard interactions. Product-card actions must remain discoverable without hover and have 44px touch hit areas.
- References to N1a mean `components/N1-Wordmark-2-links/README.md`. The sticky “gate 56,” illustration tiers, and Terminal/Garden/Atelier genre labels refer to source material not bundled here: use the explicit sticky, illustration, and theme rules instead of looking for missing files.
- Do not hide layout defects with global overflow clipping. Fix unintended overflow first; clip only intentional artwork without clipping focus indicators or interactive content.
