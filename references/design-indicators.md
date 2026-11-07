# Design indicators and remedies

Read for a new visual direction or a full audit; for a focused fix use only its matching category. These 102 review prompts are an original operational synthesis, not 102 experimentally validated predictors of AI authorship. A pattern's presence calls for contextual review; absence does not prove quality.

## Layout and composition

Convergent hero structures, unmotivated card grids, weak hierarchy, and ungrounded illustration recur in practitioner critiques; AI prototype evaluations also identify weak grouping and emphasis. ([Design Slop](https://www.adriankrebs.ch/blog/design-slop/), [Nielsen Norman Group](https://www.nngroup.com/articles/vague-prototyping/))

| ID | Review for | Prefer |
|---|---|---|
| L01 | Badge, centered slogan, gray paragraph, two buttons, floating screenshot in every hero | A composition driven by the user's task and real product artifact |
| L02 | Every section using the same width and center alignment | One deliberate primary axis and content-specific hierarchy |
| L03 | Three equal icon/title/body feature cards regardless of importance | A comparison, workflow, evidence, list, or unequal spans justified by content |
| L04 | Arbitrary asymmetry with no reading-order logic | Unequal composition that still makes order and relationships clear |
| L05 | Identical hero/features/proof/CTA rhythm across unrelated projects | A page outline derived from the decision the visitor must make |
| L06 | Decorative overlap obscuring product content | Controlled overlap only when it clarifies layering or emphasis |

## Color and surfaces

Purple-gradient conventions are not the only convergent look: cream backgrounds, rust accents, and desaturated editorial palettes are also reported as a recurring house style. These observations are not a prevalence study or a causal detector. ([Anthropic](https://claude.com/resources/articles/improving-frontend-design-through-skills), [The New Yorker](https://www.newyorker.com/culture/infinite-scroll/the-ai-design-aesthetic-thats-taking-over-the-internet))

| ID | Review for | Prefer |
|---|---|---|
| C01 | Purple/blue aurora used as an unrelated product's identity | Palette relationships grounded in brand, subject, and use |
| C02 | Cream/rust substituted automatically to “look human” | A justified palette, not a replacement house style |
| C03 | Neon outline or glow around every dark panel | Functional state contrast and restrained elevation |
| C04 | Every surface elevated, tinted, blurred, and bordered | A clear small number of surface roles |
| C05 | Arbitrary rainbow accents or a different category color per card | Semantic color assignments and non-color cues |
| C06 | Low-contrast gray dismissed as tasteful or premium | Measured readability in every real foreground/background pair |

## Typography

Provider guidance describes default font and color convergence, while current cultural reporting also flags overused serif emphasis and tracked subheadings; neither supports banning a typeface in every context. ([Anthropic](https://claude.com/resources/articles/improving-frontend-design-through-skills), [The New Yorker](https://www.newyorker.com/culture/infinite-scroll/the-ai-design-aesthetic-thats-taking-over-the-internet))

| ID | Review for | Prefer |
|---|---|---|
| T01 | A default font stack selected without brand or reading rationale | A tested type system suited to content and device |
| T02 | Replacing every sans with a fashionable serif | Contrast of roles where needed, not trend-based substitution |
| T03 | One italic/gradient/underlined word in every headline | Emphasis tied to meaning; the selected system's upright-heading rule |
| T04 | Huge display text that pushes useful content out of view | Type hierarchy proportional to task and viewport |
| T05 | Tiny uppercase, widely tracked eyebrow labels everywhere | Labels only when they improve navigation or comprehension |
| T06 | Uncontrolled wrapping, orphaned headings, numeric jitter, missing glyphs | Real text testing, tabular numbers where useful, glyph-complete fallbacks |

## Spacing and density

AI prototype reviews identify density mismatches, weak relationships, and excessive visual grouping; polished spacing is not sufficient if information priority is wrong. ([Nielsen Norman Group](https://www.nngroup.com/articles/vague-prototyping/))

| ID | Review for | Prefer |
|---|---|---|
| D01 | Marketing-page whitespace applied to an expert operations console | Density aligned to task frequency and expertise |
| D02 | Every gap using one token so all relationships look equal | Distinct within-group and between-group spacing |
| D03 | Excessive padding that makes users scroll for routine decisions | Useful information in the working viewport |
| D04 | Dense content solved by shrinking body text | Better prioritization, layout, or progressive disclosure |
| D05 | Pixel-perfect empty shells that break with real text | Content-first sizing and stress cases |
| D06 | Inconsistent alignment that is defended as personality | An intentional grid with deliberate, limited exceptions |

## Containers and components

Practitioner catalogs identify cardification, repeated radius treatments, weak pills, and overused decorative containers as common review targets; context determines whether a container is useful. ([Design Slop](https://www.adriankrebs.ch/blog/design-slop/), [Impeccable](https://github.com/pbakaus/impeccable))

| ID | Review for | Prefer |
|---|---|---|
| B01 | A card inside a card inside another card | Fewer containment levels and clear semantic grouping |
| B02 | Every sentence placed inside a rounded rectangle | Open layout, dividers, lists, or typography where sufficient |
| B03 | Pill shapes applied to every action, tag, and input | A coherent shape system and distinct component roles |
| B04 | Decorative left stripes or icon bubbles on every panel | Hierarchy expressed through real meaning and priority |
| B05 | Multiple equivalent-looking primary actions in one decision area | One clear primary action with appropriate secondary choices |
| B06 | Generic component-library defaults pasted without adaptation | Product-specific composition built on reliable primitives |

## Imagery and iconography

Illustration quality and inappropriate visuals can undermine AI prototypes; practitioner guidance emphasizes imagery relevant to content rather than filler. ([Nielsen Norman Group](https://www.nngroup.com/articles/ai-prototyping/), [Impeccable](https://github.com/pbakaus/impeccable))

| ID | Review for | Prefer |
|---|---|---|
| I01 | Abstract orbs, meaningless 3D objects, or dashboard-shaped decoration | A real product view, useful diagram, or subject-relevant art |
| I02 | Fake browser chrome used to imply a real product screenshot | An authentic labeled product artifact or honest concept image |
| I03 | Stock-like smiling teams unrelated to the organization | Approved genuine photography or no photo |
| I04 | Different icon weights, baseline, fill/stroke styles | One consistent icon family and optical sizing |
| I05 | Emoji or random sparkle icons standing in for product meaning | Clear functional SVG icons with labels where needed |
| I06 | Cropped faces, illegible screenshots, generated text artifacts | Asset inspection at final size and meaningful alternatives |

## Motion

Nonessential animation needs reduced-motion handling, and large panning/scaling can be uncomfortable; animation is not a substitute for hierarchy or usable feedback. ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion), [Impeccable](https://github.com/pbakaus/impeccable))

| ID | Review for | Prefer |
|---|---|---|
| M01 | Every block fading upward on scroll | Immediate content with meaningful, selective transitions |
| M02 | Hover scale and lift on all controls and cards | Feedback appropriate to component semantics |
| M03 | Scroll hijacking, custom cursors, or pointer effects on task-heavy pages | Native interaction unless a justified experience requires otherwise |
| M04 | Infinite ticker/marquee decoration stealing attention | Static evidence or user-controlled content where appropriate |
| M05 | Animated widths/heights, transition-all, excessive scroll handlers | The system's transform/opacity tokens and measured performance |
| M06 | Reduced-motion mode that hides content or stops essential feedback | Equivalent information and usable controls with motion reduced |

## Copy and information specificity

Weak content detail and generic explanations are observed prototype problems; design context should include real domain terminology and user needs. ([Nielsen Norman Group](https://www.nngroup.com/articles/ai-prototyping/), [Curation, Not Handoff](https://www.nngroup.com/articles/ux-context-design/))

| ID | Review for | Prefer |
|---|---|---|
| W01 | “Unlock,” “revolutionize,” or “seamless” replacing an actual benefit | What the product does, for whom, and under what conditions |
| W02 | Generic “Learn more” across unrelated actions | Labels describing the actual destination or outcome |
| W03 | Repeated eyebrow/slogan/subtitle trios with no new information | Specific headings that carry the argument |
| W04 | Equal-length filler forced into a symmetrical layout | Real information with natural variation |
| W05 | Hype, invented superlatives, or false precision | Verifiable claims, clear limitations, useful specifics |
| W06 | Tone mismatched to stress, risk, or domain | Language suited to the user's circumstances and approved voice |

## Trust and honest persuasion

Fake proof, urgency, scarcity, hidden costs, and disguised subscriptions are deceptive-pattern categories rather than signs of good craft. ([Deceptive Patterns](https://deceptive.design/types/browse/?sel=/types/obstruction/))

| ID | Review for | Prefer |
|---|---|---|
| P01 | Invented testimonials, logos, avatars, awards, or customer counts | Approved evidence or omit the claim |
| P02 | Countdown timers and scarcity labels without a real basis | Honest availability and deadlines |
| P03 | “Trusted by” strips made from arbitrary recognizable logos | Permissioned relevant proof with context |
| P04 | Hidden fees or recurring billing behind a low headline price | Complete material terms before commitment |
| P05 | Cookie/cancel choices visually manipulated to obstruct refusal | Clear equivalent choices and understandable consequences |
| P06 | Decorative security/compliance badges implying certification | Accurate, scoped claims with substantiation |

## Forms and feedback

GOV.UK guidance preserves entered values, locates useful errors beside fields and in a summary, and tells users how to recover; its exact components and language conventions are service-specific. ([GOV.UK](https://design-system.service.gov.uk/components/error-message/))

| ID | Review for | Prefer |
|---|---|---|
| F01 | Placeholder-only labels or missing units/examples | Persistent labels and useful constraints |
| F02 | Generic “Something went wrong” for a correctable field issue | What failed, why, and the next action |
| F03 | Clearing the form after a validation error | Preserve entries and focus the relevant recovery path |
| F04 | Fake loading/success states not backed by an operation | Honest operation status and durable success criteria |
| F05 | Errors visible only by red color or an inaccessible toast | Text, field association, and appropriate announcements |
| F06 | Users blamed for service failure or lack of permission | Distinguish input errors from service/access problems |

## Navigation and action semantics

Prototype evaluation finds pattern misuse and missing interaction detail; interaction quality must be checked separately from appearance. ([Nielsen Norman Group](https://www.nngroup.com/articles/ai-prototyping/))

| ID | Review for | Prefer |
|---|---|---|
| N01 | Dead buttons and `href="#"` presented as working destinations | Real targets or explicitly labeled unavailable/prototype behavior |
| N02 | Buttons that navigate and links that perform state changes arbitrarily | Semantics aligned to action |
| N03 | Desktop hover-only menus copied directly to touch devices | Operable touch and keyboard navigation |
| N04 | Search, filters, sort, tabs, and pagination that only alter decoration | Correct state/data changes with clear feedback |
| N05 | Lost back behavior or deep-link state | Predictable navigation and recoverable location |
| N06 | Important actions hidden until hover or keyboard focus clipped by chrome | Discoverable actions and visible focus |

## Charts and data

Decorative chart effects can obscure or distort values; whether labels, axes, and gridlines are needed depends on the chart's message and task. ([Nielsen Norman Group](https://www.nngroup.com/articles/clutter-charts/))

| ID | Review for | Prefer |
|---|---|---|
| G01 | Attractive upward curves invented to imply product success | Real data or clearly labeled demo data |
| G02 | Missing units, periods, sources, denominators, or freshness | Enough context to interpret the values |
| G03 | 3D effects, gradients, shadows, or texture competing with data | Clear visual encoding and restrained emphasis |
| G04 | Misleading scales, inappropriate chart types, or unclear comparisons | Chart choices justified by data and user question |
| G05 | Blindly removing axes/legends to look minimal | Keep information necessary for correct interpretation |
| G06 | Color-only distinctions or unreadable chart labels | Redundant encoding and accessible supporting values |

## Responsive and content stress

WCAG reflow requires usable content at 320 CSS px equivalent, with exceptions for genuinely two-dimensional content; masking overflow is not a substitute. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))

| ID | Review for | Prefer |
|---|---|---|
| R01 | Desktop layout scaled down without priority changes | Recomposition around mobile tasks |
| R02 | Horizontal clipping hidden by global overflow rules | Fix the source of overflow; scope intentional artwork clipping |
| R03 | Hero text, buttons, tables, or screenshots broken by long content | Stress tests for localization, large data, and zoom |
| R04 | Sticky headers/footers obscuring content or controls | Reserved space and tested focus/scroll behavior |
| R05 | Nonwrapping chips or fixed-height cards truncating meaning | Content-aware sizing and intentional truncation with access to full text |
| R06 | “Mobile ready” claimed from one static view | Multiple widths, touch behavior, orientation, and real interaction tests |

## Accessibility

WCAG 2.2 distinguishes text, non-text contrast, target-size exceptions, reflow, authentication, and focus visibility; a visual-style checklist alone cannot establish conformance. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))

| ID | Review for | Prefer |
|---|---|---|
| A01 | Missing labels/alternatives or decorative imagery announced as content | Correct semantics and purpose-specific alternatives |
| A02 | Focus removed, keyboard traps, or broken modal focus | Visible logical focus, escape/return behavior, keyboard access |
| A03 | Low-contrast gray or translucent text over variable imagery | Measured worst-case contrast and legibility |
| A04 | Tiny targets and tightly packed controls | Usable target areas with the exact criterion's exceptions understood |
| A05 | Drag-only interactions, blocked paste, inaccessible authentication | Alternatives and assistance suited to the criterion |
| A06 | UI unusable at zoom, reduced motion, high contrast, or screen reader | Test relevant modes and report actual coverage |

## Engineering and performance

Core Web Vitals measure loading, interaction, and visual stability; field thresholds cannot be established by source lint or a screenshot. ([web.dev](https://web.dev/articles/vitals))

| ID | Review for | Prefer |
|---|---|---|
| E01 | Heavy hero media and font chains delaying useful content | Sized/optimized assets and intentional loading priority |
| E02 | Layout jumps from images, fonts, embeds, or banners | Reserved dimensions and stable fallback metrics |
| E03 | Runtime errors, hydration issues, missing assets, or console spam | Clean verified loading and interaction paths |
| E04 | Huge z-index, arbitrary raw values, duplicated styling systems | Named tokens and maintainable component boundaries |
| E05 | Decorative libraries adding cost without product value | Purposeful effects within a measured budget |
| E06 | Claimed performance/accessibility results that were never measured | Named tools, actual results, and explicit untested scope |

## Product substance

UX context needs goals, users, terminology, constraints, and interaction standards; attractive visual defaults alone do not encode those decisions. ([Nielsen Norman Group](https://www.nngroup.com/articles/ux-context-design/))

| ID | Review for | Prefer |
|---|---|---|
| U01 | Logo-swap-ready copy and imagery | Details that could only belong to this product or audience |
| U02 | A beautiful landing shell with no primary task | A complete useful journey |
| U03 | Invented domain terminology or unrealistic sample records | Accurate language and plausible, labeled demo content |
| U04 | One ideal happy path only | Empty, failure, permission, offline, and recovery paths as applicable |
| U05 | Brand identity confused with functional app styling | Distinct expression where appropriate and calm consistency for repeated tasks |
| U06 | Aesthetic novelty overriding established conventions | Meaningful differentiation without avoidable learning cost |

## Second-wave anti-slop clichés

Handmade texture or asymmetry can itself become a template, and changing the default palette does not necessarily create genuine variety. ([Inky Design Works](https://www.inkydesignworks.com/posts/anti-ai-design-styles), [The New Yorker](https://www.newyorker.com/culture/infinite-scroll/the-ai-design-aesthetic-thats-taking-over-the-internet))

| ID | Review for | Prefer |
|---|---|---|
| S01 | Automatic cream, rust, editorial serif, and thin-rule styling | A direction selected for this brief, not an anti-AI uniform |
| S02 | Grain/noise added to every flat surface | Texture only when grounded in the material/story and still legible |
| S03 | Random tilted labels, stickers, arrows, or scribbles | Authored details with real informational or brand purpose |
| S04 | Giant all-caps headlines used as a universal originality fix | A scale and voice appropriate to reading context |
| S05 | Brutalist borders, arbitrary broken grids, or forced asymmetry | Deliberate structure, useful tension, and predictable interaction |
| S06 | Unnecessary defects inserted to fake human workmanship | Real specificity and iteration, not manufactured mistakes |

## Applying the catalog

Log observed evidence, affected screen/flow, user impact, proposed remedy, and whether it is a blocker, craft defect, or contextual style concern. Do not add indicators into a pseudo-scientific “AI percentage.” A legitimate brand choice can resemble a trend; the question is whether the decision serves this product and survives the full quality gate.
