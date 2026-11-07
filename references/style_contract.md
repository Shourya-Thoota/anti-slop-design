# Visual Style Contract

## Page Setup

- **Size**: A4 (210mm x 297mm) = 11906 twips x 16838 twips
- **Body margins**: Top 1.25in (1800 twips), Bottom 1in (1440 twips), Left 1in (1440 twips), Right 1in (1440 twips)
- **Header distance**: 0.5in (720 twips) from top
- **Footer distance**: 0.5in (720 twips) from bottom
- **Cover/backcover**: Full-bleed (0 margins) with background images anchored behind text

## Color Palette

| Role | Hex | Usage |
|---|---|---|
| Primary accent | `#c45c4a` | Heading 1, table top/bottom rules, cover accent geometry |
| Dark text | `#2d2d30` | Body text, Heading 2 |
| Medium text | `#5a5a5e` | Heading 3, table body text |
| Light text | `#8a8a8e` | Captions, headers, footers, secondary text |
| Border | `#d0d0d5` | Table inner horizontal borders |
| Table header bg | `#f5f5f7` | Table header row background |
| Cover text | `#f0f0f2` | White-ish text on dark cover |
| Cover bg | `#1a1a1e` | Deep charcoal cover background |
| White | `#ffffff` | Body page background |

## Typography

| Element | Font | Size | Weight | Color | Spacing |
|---|---|---|---|---|---|
| Heading 1 | Body font (sans-serif) | 20pt | Bold | `#c45c4a` | Before 24pt, After 12pt |
| Heading 2 | Body font (sans-serif) | 14pt | Bold | `#2d2d30` | Before 18pt, After 8pt |
| Heading 3 | Body font (sans-serif) | 12pt | Bold | `#5a5a5e` | Before 14pt, After 6pt |
| Body | Body font (sans-serif) | 11pt | Regular | `#2d2d30` | After 10pt, Line 1.15 |
| Bullet text | Body font (sans-serif) | 11pt | Regular | `#2d2d30` | Same as body |
| Table header | Body font (sans-serif) | 10pt | Bold | `#2d2d30` | Before 3pt, After 3pt |
| Table body | Body font (sans-serif) | 10pt | Regular | `#5a5a5e` | Before 2pt, After 2pt |
| Caption | Body font (sans-serif) | 10pt | Regular | `#8a8a8e` | Centered |
| Running header | Body font (sans-serif) | 9pt | Regular | `#8a8a8e` | Right-aligned |
| Page number | Body font (sans-serif) | 9pt | Regular | `#8a8a8e` | Centered |
| Cover title | Body font (sans-serif) | 40pt | Bold | `#f0f0f2` | Letter-spacing 3pt |
| Cover subtitle | Body font (sans-serif) | 12pt | Regular | `#8a8a8e` | Letter-spacing 2pt |

### Font Selection Strategy

- **Preferred body**: Geist, Satoshi, Manrope, or Space Grotesk — distinctive modern sans-serif with character
- **Preferred display pairing**: Playfair Display, Newsreader, or Fraunces for serif contrast when needed
- **Fallback chain**: Calibri → Arial → sans-serif (for compatibility)
- **CJK fallback**: Noto Sans CJK → Microsoft YaHei → PingFang SC
- Apply consistently across all elements; never mix more than two typeface families

## Table Style

- **Width**: 100% of page width
- **Top border**: Single, 8pt, `#c45c4a`
- **Bottom border**: Single, 8pt, `#c45c4a`
- **Inner horizontal**: Single, 4pt, `#d0d0d5`
- **No vertical borders**
- **Header row**: Background `#f5f5f7`, bold text
- **Data rows**: No background, regular weight
- **Cell padding**: Minimal (2-3pt vertical)
- **Alignment**: Left-aligned throughout

## Cover Page

- Full-bleed background image: dark charcoal (`#1a1a1e`) with geometric coral accent strip
- Coral strip: angled or vertical band occupying ~30% of left side
- Title: "Anti-Slop" + "Design System" in large bold white text, left-aligned with indent
- Subtitle: Descriptive text in light gray
- Version line: Bottom left in small light gray text
- No page number on cover

## Back Cover

- Matching full-bleed dark background with coral accent on right side
- Centered tagline: "Design with Intention" in large white bold
- Sub-tagline: "Every decision matters. Every detail counts." in light gray
- Footer: "Anti-Slop Design System | Version 1.0 | 2026"
- No page number

## Header and Footer

- **Header**: Right-aligned "Anti-Slop Design System" in 9pt light gray
- **Footer**: Centered page number in 9pt light gray
- Cover and backcover have no header/footer
- First content page may start at page 3 (after cover + TOC)
