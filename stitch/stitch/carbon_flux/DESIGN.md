# Design System Strategy: The Cinematic Engine

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Cinematic Engine."** 

Unlike traditional SaaS platforms that feel like static spreadsheets, this system is designed to feel like a high-end film editing suite fused with a futuristic AI terminal. We are moving away from the "flat web" and toward an "immersive environment." The goal is to make the user feel like they are "directing" an AI, with a UI that is fast, powerful, and pulse-driven.

To break the "template" look, we employ **Intentional Asymmetry**. Larger display elements are offset against dense, high-utility control panels. We utilize high-contrast typography scales and overlapping "glass" containers to create a sense of depth and motion, mirroring the high-energy nature of YouTube content creation.

---

## 2. Color Architecture
Our palette is rooted in the high-contrast tension between `surface_container_lowest` (#000000) and the aggressive vitality of `primary_dim` (#eb0000).

### The "No-Line" Rule
**Standard 1px solid borders are strictly prohibited for sectioning.** 
Boundaries must be defined solely through background shifts. For example, a sidebar using `surface_container_low` sits against a `surface` background. To separate content within a feed, use a transition from `surface_container` to `surface_container_high`. If a container feels "lost," do not add a stroke; instead, increase the tonal contrast of the background container.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of darkened glass.
*   **Base Layer:** `surface` (#0e0e0e) for the primary application background.
*   **Secondary Layer:** `surface_container` (#1a1919) for main content areas.
*   **Active Layer:** `surface_container_highest` (#262626) for active modals or focused input cards.

### The "Glass & Gradient" Rule
Floating elements (modals, tooltips, navigation) must utilize **Glassmorphism**. Apply `surface_variant` at 60% opacity with a `20px` backdrop-blur. 
Main CTAs should never be flat. Use a linear gradient from `primary` (#ff8e7d) to `primary_dim` (#eb0000) at a 135-degree angle to provide a luminous, "backlit" quality reminiscent of a recording light.

---

## 3. Typography: The Editorial Voice
We utilize a pairing of **Space Grotesk** for high-impact display and **Inter** for precision utility.

*   **Display (Space Grotesk):** These are your "headlines." Use `display-lg` for hero statements. The wide aperture of Space Grotesk feels technical and "New Space," signaling the AI’s intelligence.
*   **Body & Utility (Inter):** All functional data, script previews, and settings use Inter. It provides the neutral, professional "editor" feel required for long-form reading.
*   **Visual Hierarchy:** Use `label-sm` in `tertiary` (#81ecff) for "AI-Generated" tags to create a high-contrast cyan glow against the deep blacks, making the AI's "thoughts" instantly scannable.

---

## 4. Elevation & Depth
In "The Cinematic Engine," we do not use drop shadows to mimic office paper. We use light to mimic a screen.

*   **The Layering Principle:** Depth is achieved by "stacking." A `surface_container_highest` card placed on a `surface_dim` background creates a natural lift.
*   **Ambient Shadows:** If a floating element requires a shadow, it must be an "Ambient Glow." Use a large blur (32px+) with 8% opacity, tinted with the `surface_tint` (#ff8e7d) color. This makes the component look like it is emitting light rather than casting a shadow.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility, use the `outline_variant` token at **15% opacity**. It should be felt, not seen.
*   **AI Processing Glow:** Elements currently being processed by the AI should use a subtle outer glow of `tertiary` (#81ecff) to signify "activity" without using a heavy loading bar.

---

## 5. Components

### Buttons (The "Actuators")
*   **Primary:** Gradient of `primary` to `primary_dim`. High-contrast `on_primary_fixed` text. Radius: `md` (0.375rem).
*   **Secondary:** Glassmorphism style. `surface_variant` at 40% opacity with a `Ghost Border`.
*   **Tertiary:** Pure text using `secondary_fixed_dim` (#ffb19b) with a `0.5` spacing underline on hover.

### Cards & Script Lists
*   **Rule:** Forbid the use of divider lines.
*   **Implementation:** Use a `1.5` (0.3rem) vertical gap between items. Separate list items by alternating between `surface_container_low` and `surface_container`.
*   **Hover State:** On hover, a card should shift to `surface_bright` and scale by 1.02% to feel "responsive."

### Input Fields
*   **Style:** `surface_container_lowest` backgrounds with no top/left/right borders. Only a 2px bottom "underline" in `outline_variant`.
*   **Focus:** The bottom underline transitions to `tertiary` (#81ecff) with a subtle cyan neon glow.

### New Component: The "Timeline Scrubber"
For YouTube script editing, use a custom scrubber component. The track uses `outline_variant` at 20% opacity. The "playhead" is a 2px vertical line of `primary_dim` with a `primary_fixed` glow at the tip.

---

## 6. Do's and Don'ts

### Do
*   **Do** use extreme whitespace (Spacing `16` or `20`) to separate major functional groups.
*   **Do** use `tertiary` (Cyan) exclusively for AI-related feedback and system status.
*   **Do** lean into "Deep Black" (#000000) for the most important data containers to make text "pop."

### Don't
*   **Don't** use 100% opaque white for body text. Use `on_surface_variant` (#adaaaa) to reduce eye strain in dark mode.
*   **Don't** use rounded corners larger than `xl` (0.75rem). This system is "High-Tech," not "Playful." Keep edges sharp and intentional.
*   **Don't** ever use a solid gray border to separate the sidebar from the main stage. Use a tonal shift.