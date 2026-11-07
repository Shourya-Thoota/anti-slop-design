# Product-specific design quality gate

Read before a new UI build or full visual review; use the relevant subsection for a focused fix. This gate is a workflow contract, not a validated AI-origin classifier.

## Direction record

Record the primary user and task, product/domain vocabulary, context of use, existing brand, content/proof available, required platform, interaction model, chosen layout posture, typography roles, density, imagery source, and one distinguishing decision. UX context includes users, behavior, terminology, and context of use, not only a palette or radii. ([Nielsen Norman Group](https://www.nngroup.com/articles/ux-context-design/))

For greenfield work, compare three genuinely different directions. Vary composition, type roles, imagery, hierarchy, and density, not only accent hue. Choose by product fit; preserve approved decisions within an existing product. Avoid chasing novelty for its own sake.

## Review sequence

1. **Content first:** use real tasks, domain terms, product artifacts, approved claims, and honest unknowns. Build around actual information length and priority, not equal-length filler.
2. **Structure first:** inspect a wireframe or grayscale view. Verify grouping, relationships, hierarchy, and next actions before decoration. AI prototypes can misrepresent patterns, density, hierarchy, and detail even while appearing polished. ([Nielsen Norman Group](https://www.nngroup.com/articles/ai-prototyping/))
3. **Identity:** apply the selected tokens and imagery. Run the logo-swap test: if a competitor's name could replace the current one without changing the content or layout, revise the product-specific choices.
4. **Interaction:** exercise navigation, primary and secondary actions, form validation, loading, empty/error/success states, cancellation, recovery, filters, sorting, and persistence where implemented. Never make a decorative control look functional.
5. **Responsive:** inspect at 320, 375, 414, 768, and a representative desktop width, plus long labels/content and zoom. Test content-driven breakpoints; a mobile screenshot alone is not interaction validation.
6. **Accessibility:** test keyboard order, visible/unobscured focus, labels, contrast, semantics, reduced motion, and alternatives for non-text content. State the tested scope rather than declaring universal compliance.
7. **Performance:** inspect assets, font loading, stable dimensions, blocking scripts, scroll work, and interaction latency. Distinguish lab checks from field measurement.
8. **Iteration:** capture evidence, list defects by severity, fix the root cause, and rerun the affected views/flows. Do not satisfy this step with a source-code-only review or one screenshot.

## Blockers

Block delivery on fabricated proof, misleading pricing/urgency, hidden subscriptions, critical broken flows, keyboard traps, missing meaningful labels, unusable contrast, content lost at required reflow, unannounced destructive actions, or false claims of saved/server state. Fake proof, urgency, scarcity, obstruction, and hidden costs are documented deceptive-pattern types, not mere aesthetic preferences. ([Deceptive Patterns](https://deceptive.design/types/browse/?sel=/types/obstruction/))

Handle style suspicions separately: repeated hero recipes, gradients, cream palettes, serif emphasis, bento grids, and library defaults require contextual review, not automatic rejection or a claim of machine authorship. Pattern detectors can produce false positives on well-designed or human-authored sites. ([Design Slop Cop](https://github.com/AdrianKrebs/design-slop-cop))

## Measurable checks

- **Contrast:** normal text at least 4.5:1; large text at least 3:1. Large means at least 18pt regular or 14pt bold, not any 16px label. Essential non-text control/state graphics need 3:1 against adjacent colors, subject to the criterion's exceptions. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))
- **Reflow:** test 320 CSS px equivalent without two-dimensional scrolling except content needing two-dimensional layout, such as a genuine data table or map. Do not hide overflowing text to claim success. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))
- **Targets:** WCAG 2.2 AA target minimum is 24 by 24 CSS px with stated exceptions; 44 by 44 is the enhanced AAA criterion. Keep 44px as this system's preferred touch target where practical, not a misquoted universal AA rule. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))
- **Focus and input:** keyboard focus must not be entirely hidden by author-created content; provide non-drag alternatives where required and support authentication assistance/alternatives rather than blocking paste and password managers. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))
- **Motion:** remove, reduce, or replace nonessential motion when reduced motion is requested; large scaling and panning can cause vestibular discomfort. Keep information and controls available in the reduced-motion version. ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion))
- **Web Vitals:** target LCP at most 2.5s, INP at most 200ms, and CLS at most 0.1 at the 75th percentile, separating mobile/desktop. Local lab evidence does not establish field performance or replace real-user INP measurement. ([web.dev](https://web.dev/articles/vitals))

## Acceptance record

Record: route and chosen direction; viewports/screenshots reviewed; flows/states exercised; tooling and actual results; unresolved issues; allowed brand exceptions; evidence or unknown status for claims and data. Score Philosophy, Hierarchy, Execution, Specificity, Restraint, and Variety from 1 to 5 using observed reasons, then revise any score below 3. The score is an internal craft rubric, not an authorship probability.

If browser, assistive-technology, backend, or field data is unavailable, mark those checks not run. Static-lint success, a high craft score, or a pretty screenshot is never evidence that every user flow, accessibility requirement, or live metric passed.

## Local tool maintenance

After changing the source-review tool, run `python -B -m unittest discover -s tests -v` from this skill directory; `tests/test_design_audit.py` checks its source-review contract and contrast arithmetic. For an opaque color-pair calculation only, run `python -B scripts/design_audit.py --contrast "#112233" "#ffffff" --json`. Do not treat this pair calculation as a measurement of composited or rendered content.
