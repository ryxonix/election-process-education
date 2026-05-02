# ACCESSIBILITY_MANIFESTO: Inclusive UX Design

Civic Navigator is built to the **WCAG 2.1 AA Standard**, optimizing for visually impaired users, elderly voters, and screen readers.

## 1. High-Contrast Color Ratios
- **Primary Text:** Black `#000000` on Light Background (`#F4F6F8` / `#FFFFFF`). Contrast Ratio: **21:1** (Exceeds AAA requirement of 7:1).
- **Interactive Elements:** Navy Blue (`#003366`) buttons with White text. Contrast Ratio: **10:1**.
- **Focus States:** High-visibility Yellow (`#FFC000`) with a 4px outline.

## 2. Screen-Reader Compatibility (ARIA)
- **Decorative Elements Hidden:** All emojis (e.g., 📝, 🔍) are wrapped in `<span aria-hidden="true">` to prevent screen readers from reading them literally and breaking context.
- **Landmark Roles:** The navigation bar explicitly uses `aria-label="Main Navigation"`.
- **Live Regions:** The dynamically generated Mermaid.js SVG flowchart is contained within an `aria-live="polite"` region. When a user submits a scenario, a visually hidden (`.sr-only`) text block announces the result to the screen reader.

## 3. Keyboard Navigation Logic
- All interactive elements (links, form inputs, buttons) are reachable via `TAB`.
- The custom `.high-contrast-focus` CSS class ensures that keyboard users always know exactly where they are on the page.
- Forms are properly structured using `<fieldset>` and `<legend>` for structural context, avoiding floating unlabelled inputs.
