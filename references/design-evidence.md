# Evidence, uncertainty, and maintenance

Research reviewed October 25, 2026. This reference records the basis for the operational catalog and its limits; the catalog is an editorial synthesis, not an exhaustive web inventory or validated authorship test.

## Convergence and its limits

Anthropic describes convergence on common fonts, purple gradients, predictable layouts, and generic design defaults, recommending explicit direction and richer context; replacing one default with another is not genuine variety. ([Anthropic](https://claude.com/resources/articles/improving-frontend-design-through-skills))

Journalistic interviews and examples describe a newer house style involving cream backgrounds, rust accents, serif emphasis, tracked labels, tickers, and layered rounded dashboards; the article is not a quantified prevalence or causality study. ([The New Yorker](https://www.newyorker.com/culture/infinite-scroll/the-ai-design-aesthetic-thats-taking-over-the-internet))

Adrian Krebs's practitioner catalog and accompanying tool identify recurring layout and styling patterns, but the tool explicitly allows false positives and is not reliable proof that a site was authored by AI. ([Design Slop](https://www.adriankrebs.ch/blog/design-slop/), [Design Slop Cop](https://github.com/AdrianKrebs/design-slop-cop))

Impeccable provides practical guidance for typography, color, layout, motion, content, and selective polish; its recommendations remain a practitioner system, not a universal ban on gradients, libraries, cards, or particular fonts. ([Impeccable](https://github.com/pbakaus/impeccable))

Handmade visual cues and deliberate imperfection can also become repetitive stylistic defaults; adding grain, stickers, or arbitrary asymmetry is not sufficient evidence of authored quality. ([Inky Design Works](https://www.inkydesignworks.com/posts/anti-ai-design-styles), [Nielsen Norman Group](https://www.nngroup.com/articles/handmade-designs/))

## Empirical research

A 33-participant ideation study found greater group-level semantic similarity with ChatGPT versus Oblique Strategies, while finding no significant individual-level diversity difference; the work evaluates textual ideas, not website appearance or visual authorship. ([Anderson and colleagues](https://arxiv.org/html/2402.01536))

A university summary of a review of 19 empirical studies reports convergence concerns across creative output while distinguishing potentially improved individual output from reduced collective diversity; it does not validate a UI “AI detector.” ([Tilburg University](https://www.tilburguniversity.edu/current/press-releases/ai-making-creative-output-increasingly-similar))

These studies motivate diverse inputs, product-specific context, and independent review, not claims that any observed typeface, palette, or composition proves machine origin.

## Usability and context

NN/G's prototype evaluation identifies failures of visual hierarchy, component/pattern usage, density, illustration, and content detail; attractive rendering does not establish readiness for usability testing. ([AI Prototyping Tools in Practice](https://www.nngroup.com/articles/ai-prototyping/))

NN/G's “vague prototyping” guidance calls attention to grouping, hierarchy, density, references, and interaction details that generic prompts can omit. ([Vague Prototyping](https://www.nngroup.com/articles/vague-prototyping/))

NN/G proposes curated UX context encompassing research, interaction standards, glossary, users, and context of use; its effectiveness must be tested against actual output rather than assumed from a tidy context file. ([Curation, Not Handoff](https://www.nngroup.com/articles/ux-context-design/))

GOV.UK error guidance preserves entered values, associates clear corrective messages with fields, and separates user-correctable input errors from service/access problems; do not impose its exact component or language conventions on every product without adaptation. ([GOV.UK Design System](https://design-system.service.gov.uk/components/error-message/))

NN/G's chart guidance treats clutter in context: remove distracting decoration but retain axes, labels, legends, or gridlines when they are needed to interpret the information correctly. ([Clutter-Free Charts](https://www.nngroup.com/articles/clutter-charts/))

## Standards and measurements

WCAG 2.2 provides testable criteria, including contrast, reflow, targets, focus, dragging alternatives, and accessible authentication; these are accessibility requirements, not aesthetic-origin indicators. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))

MDN documents the user's reduced-motion preference and the need to reduce or replace nonessential motion, including potentially uncomfortable panning and scaling. ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion))

Web.dev defines Core Web Vitals and good thresholds for LCP, INP, and CLS, assessed at the 75th percentile; lab checks do not establish real-user field performance. ([web.dev](https://web.dev/articles/vitals))

Fake proof, fake scarcity/urgency, hidden costs/subscriptions, obstruction, and visual interference belong to deceptive-design taxonomies; address these as honesty and interaction failures rather than decorating around them. ([Deceptive Patterns](https://deceptive.design/types/browse/?sel=/types/obstruction/))

## Maintenance rules

Recheck standards and source dates before changing numerical requirements. For new trend claims, seek independent examples and counterexamples; do not count copied blog posts as independent corroboration. Preserve useful conventional patterns and approved brands. Do not import third-party code or assets merely because this reference links to them.

New rules need a concrete failure, observable user/design impact, applicability condition, remedy, exception, and test. Keep speculative aesthetic observations separate from normative standards and measured results. Record inaccessible evidence or missing browser/field testing explicitly. Never promise that following this system guarantees every design will look human to every observer.
