# Imagery and Iconography

## Image Quality Standards

### Photography

- Use real photography over stock images whenever possible
- Stock images must be carefully selected: no generic "people in meetings" or "handshake" photos
- Images should show the product, the outcome, or the context — not generic concepts
- Screenshots must be real, not mockups presented as real
- All images need proper licensing or must be created/original

### Image Treatment

| Treatment | Use Case | Guideline |
|---|---|---|
| Full-bleed | Hero sections, backgrounds | Must have sufficient contrast with overlaid text |
| Contained | Product shots, content images | Consistent border radius or sharp edges per system |
| Circular | Avatars, profile pictures | Only for actual people; never for product images |
| Rounded corners | Cards, thumbnails | Consistent radius across all images (e.g., 8px, 12px) |

### Image Sizing

- Define aspect ratios and stick to them: 16:9, 4:3, 1:1, 3:2
- Never stretch or squish images to fit containers
- Use `object-fit: cover` for containers, `object-fit: contain` for product shots
- Provide `srcset` or responsive images for appropriate resolution

## Icon Standards

### Style

- Use single-weight vector SVG icons at a consistent stroke width
- Stroke width: 1.5px or 2px — chosen once, applied everywhere
- Icon weight should match the text weight they accompany
- Never mix outlined and filled icons in the same interface

### Usage

- Icons describe function, not decorate
- Every icon should be immediately recognizable without a label
- When in doubt, use text + icon, not icon alone
- Icon size should relate to text size: 16px for body, 20px for headings, 24px for standalone

### Prohibited Icon Patterns

- Emoji as iconography (inconsistent across platforms)
- Sparkle/star/magic icons for AI features (cliched)
- Generic silhouette avatars (signals fake testimonials)
- Icons with inconsistent stroke weights
- Low-resolution raster icons (PNG, GIF)

## Data Visualization Standards

### Charts

- Bar charts must start y-axis at zero
- Never truncate y-axes to exaggerate differences
- Pie charts: maximum 5 categories; otherwise use bar charts
- Data labels must be visible without hover/tooltip
- Color must not be the only way to distinguish data series

### States for Data Displays

| State | Requirement |
|---|---|
| Empty | Design intentional empty states with guidance and next steps |
| Loading | Use skeletons, spinners, or progress indicators |
| Error | Design error states with recovery actions |
| Success | Show confirmation without blocking further interaction |

## Data and Content Bans

| Banned Pattern | Why | Replacement Strategy |
|---|---|---|
| Invented statistics ("99.9% uptime") | False claims, legal risk | Use real data, or remove the claim |
| Fake user counts or growth numbers | Deceptive | Use real metrics, or qualitative social proof |
| Placeholder images that look real | Misleading | Use obvious placeholders, or real imagery |
| Charts with truncated y-axes | Misleading visualization | Start bar charts at zero; document any exceptions |
| Pie charts with more than 5 categories | Unreadable | Use bar charts, or group smaller categories |
| Data in tooltips only | Hides information | Show key values directly |
| No empty state | Confuses users when data absent | Design intentional empty states with guidance |
| No error state | Leaves users stranded | Design error states with recovery actions |
| No loading state | Users think app is broken | Use skeletons, spinners, or progress indicators |
| Mock data that looks like real data in production | Confuses users | Clearly label mock data, or remove it |
