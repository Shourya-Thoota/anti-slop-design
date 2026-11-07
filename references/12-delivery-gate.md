# Delivery Gate Checklist

Run this checklist **every time** before emitting design output. Do not skip. Do not ship and apologize.

## How to Use

For each block, answer every question. A "No" or "Unsure" is a finding — fix it before proceeding.

Report the results in four blocks with a PASS/FAIL summary.

---

## Block A: Correctness (Hard Gate)

**All must be YES to pass.**

| # | Question | Pass Criteria |
|---|---|---|
| A-1 | Are all facts, statistics, and testimonials real and verifiable? | Every claim has a source or is removed |
| A-2 | Is there no placeholder text ("Lorem ipsum", "Coming soon") in the UI? | All copy is production-ready |
| A-3 | Are there no internal workflow labels visible to users? | No "Option A", template names, or internal notes |
| A-4 | Does every interactive element have a working action? | No decorative buttons or broken links |
| A-5 | Are all images and media properly licensed or created? | No unauthorized stock photos or stolen assets |

**Block A Result:** PASS / FAIL

If FAIL: Stop. Fix all findings before proceeding to Block B.

---

## Block B: Anti-Slop Rules (Hard Gate)

**All must be YES to pass.**

| # | Question | Pass Criteria |
|---|---|---|
| B-1 | Did I avoid Inter, Roboto, or Arial as unexamined defaults? | Chosen typefaces have a stated rationale |
| B-2 | Did I avoid purple/indigo-to-blue gradients as decoration? | Gradients have product-specific justification |
| B-3 | Did I avoid glassmorphism, floating blobs, or mesh gradients without purpose? | Decorative effects carry information or are removed |
| B-4 | Did I avoid three identical feature cards in a row? | Layout varies based on content importance |
| B-5 | Did I avoid the centered hero template (badge -> heading -> subheading -> buttons)? | Hero has a chosen structure, not the default |
| B-6 | Did I avoid uniform 1px gray borders on every card? | Separation uses spacing, shadow, or varied borders |
| B-7 | Did I avoid generic fade-in-on-scroll on every element? | Motion is intentional, hierarchical, and varied |
| B-8 | Did I avoid emoji as iconography? | Icons are single-weight SVG or purpose-built |
| B-9 | Did I avoid generic marketing copy ("Elevate", "Unlock", "Seamlessly")? | Copy is specific, plain, and product-focused |
| B-10 | Did I avoid dark mode that nobody asked for? | Dark mode shipped only with justification |
| B-11 | Did I avoid fake data, invented stats, or placeholder avatars? | All data is real or clearly labeled as mock |
| B-12 | Did I avoid decorative color bars under titles? | Hierarchy uses weight, size, and whitespace |

**Block B Result:** PASS / FAIL

If FAIL: Stop. Fix all findings before proceeding to Block C.

---

## Block C: Craftsmanship Standard (Quality Lock)

**Score each C-1 through C-5 as YES / PARTIAL / NO.**

| # | Criterion | YES | PARTIAL | NO |
|---|---|---|---|---|
| C-1 | **Intentionality** — Can I articulate a reason for every visual and copy decision? | Every decision has a stated rationale | Most decisions have rationale; a few are default-adjacent | Many decisions are "because it's modern" or "default" |
| C-2 | **Functional Completeness** — Does every interactive element work? | All elements functional; all states handled | Most work; some edge cases unhandled | Broken elements exist; missing states |
| C-3 | **Content-Driven Composition** — Does every section exist for the content? | No template-filling sections | One or two sections are template-adjacent | Multiple sections exist only because "landing pages have them" |
| C-4 | **Resilience** — Does it hold in all states, breakpoints, and input methods? | Tested across breakpoints, themes, keyboard | Desktop + mobile only; some states unhandled | Single breakpoint; missing states; no keyboard support |
| C-5 | **Evidence Over Claims** — Are all facts verifiable? | Every claim sourced | Most claims sourced; minor assertions | Unsupported claims present |

**Block C Score:** ___ / 5 (Count YES=1, PARTIAL=0.5, NO=0)

**Block C Result:** PASS (>= 4.0) / CONDITIONAL (2.5-3.5) / FAIL (< 2.5)

If CONDITIONAL: Note the gaps and plan fixes for the next iteration.
If FAIL: Stop. Revisit the design direction and fix fundamentals.

---

## Block D: Liveliness (Quality Lock)

**Score each D-1 through D-3 as YES / PARTIAL / NO.**

| # | Criterion | YES | PARTIAL | NO |
|---|---|---|---|---|
| D-1 | **Energy** — Does the interface feel purposeful, not merely clean? | One or more bold choices that show conviction | Competent but conservative | Flat, timid, afraid to commit |
| D-2 | **Rhythm** — Is there visual pacing, not mechanical repetition? | Spacing, size, and color vary intentionally | Mostly consistent with minor variation | Mechanical sameness throughout |
| D-3 | **Motion** — Does motion enhance meaning, not just decorate? | Motion communicates state or hierarchy | Some motion; mostly decorative | No motion, or generic motion applied uniformly |

**Block D Score:** ___ / 3 (Count YES=1, PARTIAL=0.5, NO=0)

**Block D Result:** PASS (>= 2.0) / CONDITIONAL (1.0-1.5) / FAIL (< 1.0)

---

## Final Report Format

Emit the Delivery Gate report in this exact format:

```
## Delivery Gate Report

**Mode:** [During / After]
**Artifact:** [What was reviewed]

### Block A: Correctness — [PASS / FAIL]
- [List any findings, or "None"]

### Block B: Anti-Slop Rules — [PASS / FAIL]
- [List any findings, or "None"]

### Block C: Craftsmanship — [PASS / CONDITIONAL / FAIL] (X/5)
- C-1 Intentionality: [YES/PARTIAL/NO]
- C-2 Functional Completeness: [YES/PARTIAL/NO]
- C-3 Content-Driven Composition: [YES/PARTIAL/NO]
- C-4 Resilience: [YES/PARTIAL/NO]
- C-5 Evidence Over Claims: [YES/PARTIAL/NO]

### Block D: Liveliness — [PASS / CONDITIONAL / FAIL] (X/3)
- D-1 Energy: [YES/PARTIAL/NO]
- D-2 Rhythm: [YES/PARTIAL/NO]
- D-3 Motion: [YES/PARTIAL/NO]

### Overall: [PASS / CONDITIONAL / FAIL]

[If CONDITIONAL or FAIL: List the top 3 actions required to pass.]
[If PASS: List 2-3 deliberate choices made and why.]
```

---

## Audit Mode (After)

When auditing existing work:

1. Run Blocks A-D against the existing artifact.
2. For each finding, assign a severity:
   - **Critical** — Must fix (blocks pass)
   - **Major** — Should fix (significant slop)
   - **Minor** — Could fix (polish)
3. Present numbered findings grouped by block.
4. Fix approved findings.
5. Re-run the Delivery Gate and emit a follow-up report.

### Audit Report Format

```
## Anti-Slop Audit Findings

**Artifact:** [What was audited]
**Total Findings:** [N critical, N major, N minor]

### Critical
1. [Finding description] — [Location/element]
   Suggested fix: [Action]

### Major
1. [Finding description] — [Location/element]
   Suggested fix: [Action]

### Minor
1. [Finding description] — [Location/element]
   Suggested fix: [Action]

### Approved for Fix
[List user-approved findings]

### Follow-up Report
[After fixes: Re-run Delivery Gate and report results]
```
