# Best Practices and Examples

## Before/After Scenarios

Each scenario shows a common sloppy pattern alongside its intentional replacement. Use these as reference when designing or reviewing work.

---

### Scenario 1: Hero Section

| Aspect | Slop (Before) | Intentional (After) |
|---|---|---|
| **Layout** | Centered: badge pill -> huge heading -> gray subheading -> two buttons | Asymmetric split layout: product image bleeding to right edge, bold left-aligned headline |
| **Typography** | One size of Inter, default weights | Display font for headline (48px, tight leading), body font for description (16px, 1.6 leading) |
| **Color** | Purple-to-blue gradient background | Warm off-white background (#faf9f7), single coral accent for primary CTA only |
| **CTA** | "Get Started" + "Learn More" pills | "Start Free Trial" primary button (coral) + "See How It Works" text link |
| **Why it matters** | The centered hero is the most common AI landing page template. It signals "I did not think about this." | The split layout creates visual tension, uses real product imagery, and has a clear single action. |

---

### Scenario 2: Feature Cards

| Aspect | Slop (Before) | Intentional (After) |
|---|---|---|
| **Layout** | Three identical cards in a row, each with icon + heading + body + link | Two prominent feature cards (larger, with images) + one detailed case study card (full-width, with quote) |
| **Sizing** | All cards same width, same padding, same icon size | Cards vary by content importance: primary feature gets 50% width, secondary gets 50%, case study spans full width below |
| **Content** | Generic icons (sparkle, lightning, shield), headings like "Fast", "Secure", "Reliable" | Screenshots of actual features, headings like "Deploy in 30 Seconds", "SOC 2 Type II Certified" |
| **Borders** | 1px gray border on every card | No borders; separation through whitespace (48px gap) and background color shifts |
| **Why it matters** | Three identical cards is a template-filling pattern. It says "I needed a features section" not "these features matter." | Varied sizing and real content show that each feature has different importance and real evidence. |

---

### Scenario 3: Color Usage

| Aspect | Slop (Before) | Intentional (After) |
|---|---|---|
| **Background** | Purple-to-blue gradient on every section | Warm off-white (#faf9f7) primary, light warm gray (#f0eeeb) for alternate sections |
| **Text** | Pure black (#000000) on white | Near-black (#1a1a1e) on warm off-white for comfortable reading |
| **Accent** | Blue for links, green for success, purple for brand, orange for warnings | Single coral accent (#c45c4a) for all interactive elements; semantic colors only for status indicators |
| **Neutrals** | Gray (#888888) for secondary text | Warm gray (#5a5a5e) that harmonizes with the dominant warm tone |
| **Why it matters** | The purple-blue gradient is the most recognizable AI slop signature. Multiple accent colors create visual chaos. | A single warm palette with one sharp accent creates cohesion and brand recognition. |

---

### Scenario 4: Typography

| Aspect | Slop (Before) | Intentional (After) |
|---|---|---|
| **Font choice** | Inter at default weights everywhere | Geist for body and UI, Playfair Display for headlines (documented: "serif adds editorial authority to a technical product") |
| **Type scale** | Arbitrary sizes: 14px body, 18px heading, 24px hero | Modular scale: 12px label, 14px body, 16px H3, 20px H2, 24px H1, 32px display, 48px hero |
| **Line height** | 1.5 everywhere | 1.1 for hero, 1.2 for H1, 1.3 for H2, 1.6 for body, 1.5 for small text |
| **All caps** | Default tracking | Increased tracking (+10%) for labels and tags in all-caps |
| **Why it matters** | Default Inter with arbitrary sizes signals no thought was given. | A documented type system with intentional pairing and measured spacing shows craft. |

---

### Scenario 5: Buttons and CTAs

| Aspect | Slop (Before) | Intentional (After) |
|---|---|---|
| **Button text** | "Learn More" | "Read the Documentation" |
| **Shape** | Fully rounded pill | Slightly rounded rectangle (4px radius) — more serious, better for dense UIs |
| **States** | Default + hover (color change only) | Default, hover (darken), focus-visible (2px ring), active (scale 0.98), loading (spinner inside), disabled (opacity 0.5) |
| **Hierarchy** | Two equally styled buttons side by side | One primary (coral fill) + one secondary (outlined) + one tertiary (text link) |
| **Why it matters** | "Learn More" is the weakest possible CTA. Pill shapes and missing states signal unfinished work. | Specific action text, full state coverage, and clear hierarchy guide users confidently. |

---

### Scenario 6: Data Visualization

| Aspect | Slop (Before) | Intentional (After) |
|---|---|---|
| **Chart type** | Pie chart with 8 categories | Horizontal bar chart, grouped by category, top 5 shown, remainder in "Other" |
| **Y-axis** | Truncated at 50% to exaggerate differences | Starts at zero; differences are honest |
| **Data labels** | Only visible on hover tooltip | Values displayed directly on bars; tooltips show supplementary context |
| **Colors** | Rainbow palette, one color per category | Single hue with value variation; accent color highlights the key metric |
| **Empty state** | Blank white area with no message | Designed empty state: "No data for March. Select a different month or add a data source." |
| **Why it matters** | Truncated axes and tooltip-only data are misleading. Rainbow palettes distract from the story. | Honest scales, direct labels, and intentional empty states build trust and clarity. |

---

## Summary: The Slop Signals

When reviewing design, watch for these instant tells:

1. **Template-filling layout** — Sections that exist because "every landing page has them"
2. **Default aesthetics** — Inter font, purple-blue gradients, 1px gray borders, pill buttons
3. **Missing states** — Buttons without focus, forms without errors, data without empty states
4. **Generic copy** — "Elevate", "Unlock", "Seamlessly", "Learn More"
5. **Even distribution** — Even spacing, even sizing, even color = no hierarchy, no point of view

Fix these by asking: "What is the specific reason this choice exists for THIS product?" If there is no answer, it is slop.
