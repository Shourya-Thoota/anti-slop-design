# Developer specifications

Use for design systems, component references, token documentation, interaction contracts, accessibility notes, and handoffs. This mode incorporates Frontend Design Doc; do not load that retired skill or choose a new visual direction merely to document an existing one.

1. Establish product/version, platforms, actual framework, audience, scope, and requested format. Default to Markdown; export only when requested.
2. Materialize `frontend-design-doc` using `module-library.md`. Read its `references/source-guide.md` and `references/structure_contract.md` for the relevant scope. The current mode overrides its old Word default, numbered-heading default, judge feedback, and universal front matter.
3. Inventory actual components or label proposed behavior. For each document description, anatomy, props, variants, applicable state matrix, do/don't examples, accessibility notes, and related components. Mark irrelevant states not applicable.
4. Record token names/values/roles/units/modes; grid and content-driven breakpoints; keyboard/focus behavior; loading, errors, empty states, and reduced motion. Use developer-actionable values and links rather than aesthetic adjectives.
5. Use the project's selected Anti-Slop decisions as the source of truth. Only a specifically requested full Anti-Slop standards guide uses `document-workflow.md` and its 16-section contract.
6. For explicit Word/PDF/slides use `user:office-documents`. Read the module's `references/style_contract.md` only for a paginated specification without an existing project profile; its palette is not a new product brand.
7. Validate against the inventory and actual implementation. Do not invent props, implementation status, accessibility results, or page numbers. For Word use one native heading-driven TOC with refreshed results, not a handwritten duplicate.

Completion: a specification or requested export that distinguishes observed implementation from proposals and preserves the established visual system. If a format exporter is unavailable, deliver the content honestly without mislabeling its file type.
