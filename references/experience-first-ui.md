# Experience-First UI

Issueflow must protect proof without letting proof become the product UI.

For user-facing product work, default to experience-first delivery:

- build the screen, flow, or product moment the user is meant to use
- keep QA, debug, raw payloads, and proof metadata out of the default visual surface
- expose diagnostics through stable attributes, tests, dev inspectors, or collapsed details
- inspect the first viewport as a product surface, not only as a test target
- judge the in-app screen as a designed object: composition, spacing, hierarchy, asset quality, motion, and copy must feel intentional to a human viewer

## Anti-dashboard default

Do not create a dashboard, card grid, admin console, status board, or proof panel as the first product UI unless the product is actually an operational dashboard.

For consumer apps, creative tools, landing experiences, and polished product flows, the first screen should communicate the product promise through the primary interaction, scene, object, or workflow. Debug and QA affordances should support that experience from behind the scenes.

## Issue shaping

For UI issues, require a compact UX direction:

- audience and use context
- primary user action or first-read object
- desired feel, visual language, or reference direction
- first-viewport priority
- explicit anti-goals such as "not a dashboard" or "no visible QA copy"

Acceptance criteria should include at least one user-facing design outcome, not only a proof command.

## Aesthetic and native-language bar

For screen judgment, implementation correctness is only one part of readiness. The reviewer must also decide whether the in-app surface is aesthetically good enough for a person to want to keep looking at it.

Check:

- the screen looks visually intentional, balanced, and polished rather than merely functional
- the main object or action is where a person's eye naturally lands
- typography, spacing, contrast, imagery, and motion support the product mood
- generated or imported assets are recognizable, relevant, and not broken-looking
- no UI element feels like temporary scaffolding unless the product is explicitly an internal tool
- user-facing copy reads like a fluent native speaker wrote it for this product
- localized or narrative text uses common, natural phrasing rather than translated, stiff, or uncommon constructions
- choice labels, button labels, errors, empty states, and story sentences sound like things real users or characters would actually say

If the screen passes tests but looks ugly, amateur, visually confusing, or linguistically awkward, the issue is not done. Keep iterating or mark the QA/merge gate as blocked.

## Implementation guidance

Start from the user's product moment:

- identify what should be visually dominant
- choose layout density for the domain
- use domain-specific components and controls instead of generic cards
- use current, polished visual conventions without chasing trends blindly
- prefer visual assets, real product imagery, rich state, motion, or tactile interaction when the domain calls for it
- keep copy short and user-facing
- rewrite awkward copy until it sounds natural in the product's target language, especially for story, onboarding, choices, errors, and calls to action

For SaaS, CRM, admin, or operational tools, a restrained dashboard may be correct. For consumer products and creative tools, a dashboard is usually a failure of first framing.

## Polished first-pass defaults

When the issue does not provide a detailed design system, choose a compact design direction before coding:

- audience and setting
- product object or scene that should own the first viewport
- primary action and secondary actions
- visual references or genre conventions
- layout rhythm, typography scale, palette, motion, and asset plan
- empty, loading, error, and success states that feel native to the product

Avoid generic proof-first UI patterns:

- card soup where every concept becomes a bordered panel
- visible debug IDs, raw payload strings, or QA labels
- explanatory text that describes features instead of making the controls obvious
- one-note dark dashboard palettes unless the domain asks for them
- placeholder gradients or abstract blobs where real product objects, scenes, screenshots, or generated bitmap assets would communicate better

Use familiar controls: icons for tools, segmented controls for modes, toggles for binary settings, sliders or steppers for numeric values, tabs for views, menus for option sets, and concise labels only where they improve clarity.

## Proof guidance

Proof should verify the product experience:

- screenshots should show the actual user-facing surface
- browser or golden assertions should protect visual hierarchy, first action, and responsive layout
- raw debug values should be asserted through data attributes or test helpers
- a green test is not enough if the screenshot still reads as QA scaffolding
- a green test is not enough if the screenshot is aesthetically poor or the visible copy sounds unnatural to a native speaker

If the proof needs extra controls, keep them hidden, collapsed, test-only, or clearly outside the default user path.
