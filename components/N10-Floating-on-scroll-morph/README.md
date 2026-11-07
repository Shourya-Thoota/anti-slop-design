A sticky bar at the top that **morphs into a floating pill** as the user scrolls past a threshold. Two visual modes share one DOM — `.nav` (outer) owns the bar look, `.nav__inner` (inner) owns the pill look. Cross-faded on a single class toggle (`.is-floating`) with one timing curve. Active layer feels seamless; AI defaults always botch this.
*Use when:* atmospheric / modern-minimal pages where the kinetic micro-moment earns its place. Adds a single tasteful surprise; resists novelty.
*Don't confuse with:* N5 Floating pill (always-on, no scroll behaviour). N10 is N5 plus a default-bar state that morphs *into* it.

```html
<header class="nav">
  <div class="nav__inner">
    <a class="wordmark">Marlow</a>
    <ul class="nav__links">…</ul>
  </div>
</header>
```

Follow four laws: keep the height constant, move with `transform` for offsets, cross-fade everything that changes, and use a single easing curve. Skipping them makes most attempts read as broken.

*Anti-pattern:* swapping two `<header>` elements via opacity instead of cross-fading one DOM. Doubles markup, fights focus order, desyncs content.

---

Group: Navigation. Pattern code: N10.
