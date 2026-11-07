# Motion and Animation Standards

## Motion Principles

1. **One high-impact reveal beats ten micro-interactions.** A dramatic entrance for the hero beats subtle hover effects on every card.
2. **Motion should answer a question.** What changed? Where did it go? What happens next?
3. **Respect the user.** Honor `prefers-reduced-motion`. Never animate in a way that causes discomfort.
4. **Timing is character.** Snappy (150-200ms) feels precise. Smooth (400-600ms) feels elegant. Slow (>800ms) feels luxurious or annoying.
5. **Easing is personality.** `ease-out` feels responsive. `ease-in-out` feels balanced. Custom cubic-bezier curves feel crafted.

## Timing Guidance

| Duration | Feeling | Use Case |
|---|---|---|
| 0ms | Instant | State changes that should feel immediate |
| 100-150ms | Snappy | Micro-interactions: hover, focus, toggle |
| 200-300ms | Responsive | Button presses, menu opens, tab switches |
| 400-600ms | Elegant | Page transitions, modal appearances, reveals |
| 700-1000ms | Dramatic | Hero entrances, major content reveals |
| 1000ms+ | Cinematic | Special moments only; use sparingly |

Rules:
- Never use default `ease` without consideration
- Staggered animations: 50-100ms delay between items
- Loading animations: loop at a speed that feels active but not frantic

## Easing Character

| Easing | Character | Use Case |
|---|---|---|
| `ease-out` | Responsive, snappy | UI feedback: buttons, toggles, hovers |
| `ease-in-out` | Balanced, smooth | Transitions: page changes, expand/collapse |
| `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful, bouncy | Delight moments: success states, celebrations |
| `cubic-bezier(0.22, 1, 0.36, 1)` | Smooth, decelerating | Hero reveals, content entrances |
| `linear` | Mechanical, constant | Progress bars, spinners, continuous motion |

## Motion Types by Purpose

### State Changes

- Use motion to communicate what changed and where
- Form validation: shake or slide in error message
- Toggle: smooth slide between states, not instant swap
- Accordion: height animation with content fade

### Hierarchy and Reveal

- Animate the most important element most notably
- Secondary elements: subtler or no animation
- Everything else: instant appearance
- One entrance per viewport scroll, not every element

### Feedback

- Button press: scale down slightly (0.98) on active
- Form submit: button transitions to loading state
- Success: brief celebratory motion (checkmark draw, confetti)
- Error: subtle shake or red flash

## prefers-reduced-motion

- Always respect `prefers-reduced-motion: reduce`
- Provide instant-state fallbacks for all animations
- Never auto-play motion that cannot be paused
- No flashing content (more than 3 flashes per second)

## Motion Bans

| Banned Pattern | Why | Replacement Strategy |
|---|---|---|
| Generic fade-in-on-scroll applied to everything | Mechanical, no hierarchy | Animate the most important element; use different animations for different content types |
| `:hover` carrying meaning in mobile app | Mobile has no hover | Use tap, swipe, or visible state changes instead |
| Parallax on every scroll | Distracting, performance cost | Use only when depth genuinely enhances the narrative |
| Loading spinners with no progress indication | Uncertainty for long operations | Use progress bars, skeleton screens, or step indicators |
| Auto-playing carousels | User loses control | Let the user control progression; show one item at a time |
| Every element animates on page load | Visual chaos | One high-impact staggered entrance; everything else instant |
| Spring/bounce animations for serious products | Mismatched personality | Match motion character to brand: crisp for professional |
| Animations ignoring prefers-reduced-motion | Excludes motion-sensitive users | Always respect the media query; provide instant fallbacks |
