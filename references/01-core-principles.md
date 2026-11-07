# Core Design Principles

## Introduction

This document establishes a comprehensive design system focused on one critical objective: preventing sloppy, inconsistent, and low-quality design output. It is both a style guide prescribing positive standards AND a filter removing prohibited patterns. Teams apply these principles, standards, and actionable guidelines to maintain high design quality across all outputs.

The central thesis: if a design choice exists because "it looks modern" or "it works for most sites" or "it's the default," it is slop. Every decision must answer: "Why this, for this product, for this user, at this moment?" No answer means the choice is wrong.

## What Is Slop?

Slop is a choice made by reflex rather than for the product. Treat a choice as suspect when:

- It could be pasted into an unrelated product unchanged
- It repeats a familiar generated-design pattern
- It conflicts with the local design system or nearby sections
- It communicates no useful information, state, action, hierarchy, or brand meaning
- It competes with content, weakens trust, or makes the interface harder to use

## Why Prohibitions Beat Aspirations

A model's default output is the statistical center of its training data. For design, the center is competent, inoffensive, and instantly recognizable as machine-made. Asking for "beautiful" or "modern" or "professional" moves nothing, because the model already believes its default *is* those things.

What moves output is **subtraction**. Naming specific things the model must not do removes the default without requiring it to have taste.

1. **Prohibitions are checkable; aspirations are not.** A model can verify "did I use Inter?" It cannot verify "is this beautiful?"
2. **The failure mode is convergence, not incompetence.** Models are not bad at design. They are *average* at design, reliably, every time.
3. **Specificity carries information; adjectives do not.** "Distinctive typography" is a word the model will happily believe it satisfied. "Not Inter, not Roboto, not Arial, source from Fontshare" leaves nowhere to hide.

## How to Use This Document

Use this system in two modes:

- **During construction** — Let these rules guide work as it is built. Reference the positive standards for each design dimension.
- **After completion** — Audit existing work against the Delivery Gate checklist, fix findings, and re-run the gate.

This system applies to all design outputs: websites, landing pages, dashboards, web applications, mobile applications, components, design systems, micro-interactions, and any user-facing artifact.

## The Anti-Slop Hierarchy of Needs

Every element must survive this ladder, bottom to top. If it fails at any level, it is slop regardless of how attractive it appears above.

### Level 1: Correctness

- No invented facts, fake testimonials, or placeholder data presented as real
- No internal workflow language rendered to users ("Option A", template names, "here is your deck")
- All interactive elements actually work; broken interactions are defects, not decoration
- All states handled: empty, loading, error, success, offline

### Level 2: Function

- Every section exists because the product's content needs it
- No template-filling sections that only repeat what every other landing page has
- Navigation labels describe what the user finds, not what the company calls it
- CTAs say what happens, not what the company wants the user to feel

### Level 3: Resilience

- Holds at every breakpoint, not just desktop and mobile
- Keyboard-navigable; focus states visible and styled
- Color contrast meets WCAG 2.1 AA at minimum
- Motion respects `prefers-reduced-motion`
- Works in high-contrast mode and when user overrides fonts

### Level 4: Distinctiveness

- A named visual direction that would not fit an unrelated product
- Typography chosen with intention, not reached for by default
- Color system has a dominant tone and a sharp accent; no timid evenly-distributed palette
- Layout has a point of view: asymmetric, editorial, dense, airy — chosen, not defaulted

### Level 5: Liveliness

- The interface feels alive, not merely clean
- Motion has personality: one high-impact reveal beats ten micro-interactions
- Copy has voice; the product sounds like a person, not a brand manual
- Surfaces have depth: gradients, textures, or patterns that create atmosphere

## The Craftsmanship Standard

"Not slop" is the floor, not the goal. Evaluate every output against these five criteria:

### C-1: Intentionality
Every visual and copy decision has a reason you can articulate. If the only reason is "it's the default," that is a red flag: revisit the decision. Document the rationale for typeface choices, color roles, spacing values, and layout structures.

### C-2: Functional Completeness
Every interactive element works, or it does not exist. A button that cannot do anything is a defect, not decoration. Design and implement all states: default, hover, focus, active, loading, disabled, error, and empty.

### C-3: Content-Driven Composition
Every section exists because the product's content needs it, not because every landing page has one. Remove sections that only fill a template. If a section does not serve a specific content purpose, remove it.

### C-4: Resilience
The UI holds up in every state (empty, loading, error), every theme you ship, every breakpoint, and keyboard-only use. Test with screen readers, keyboard navigation, and device simulators.

### C-5: Evidence Over Claims
Anything presented as fact (testimonials, statistics, security claims) is real and verifiable, or it is not shown at all. Fake social proof destroys trust faster than no social proof.
