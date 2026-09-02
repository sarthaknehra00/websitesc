---
name: Serene Growth
colors:
  surface: '#faf8ff'
  surface-dim: '#ced9ff'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2ff'
  on-surface: '#0b1a3b'
  on-surface-variant: '#434654'
  inverse-surface: '#212f52'
  inverse-on-surface: '#eef0ff'
  outline: '#747685'
  outline-variant: '#c3c5d6'
  surface-tint: '#1f54d1'
  primary: '#003fb3'
  on-primary: '#ffffff'
  primary-container: '#2558d5'
  on-primary-container: '#d6ddff'
  inverse-primary: '#b5c4ff'
  secondary: '#a63a20'
  on-secondary: '#ffffff'
  secondary-container: '#fd795a'
  on-secondary-container: '#6e1400'
  tertiary: '#755b00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cfa621'
  on-tertiary-container: '#4f3d00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b5c4ff'
  on-primary-fixed: '#00174d'
  on-primary-fixed-variant: '#003cac'
  secondary-fixed: '#ffdad2'
  secondary-fixed-dim: '#ffb4a3'
  on-secondary-fixed: '#3d0700'
  on-secondary-fixed-variant: '#86230a'
  tertiary-fixed: '#ffe08e'
  tertiary-fixed-dim: '#edc13e'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#584400'
  background: '#faf8ff'
  on-background: '#0b1a3b'
  surface-variant: '#dae2ff'
  surface-cream: '#FCF9F4'
  surface-teal: '#00817D'
  accent-coral-pale: '#F9B8A9'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 56px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.7'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  section-desktop: 120px
  section-mobile: 64px
  gutter: 32px
  margin-desktop: 48px
  margin-mobile: 20px
  container-max: 1280px
---

## Brand & Style

The design system is defined by a "Professional Warmth" philosophy, specifically engineered for neurodivergent-friendly educational environments. The visual direction balances the high-trust requirements of an institutional service with a child-friendly, optimistic atmosphere.

The style is **Modern Corporate Minimalism** with **Soft Geometric** influences. Key visual characteristics include:
- **Ample Breathing Room:** Extreme whitespace to prevent cognitive overload.
- **Organic Geometry:** A preference for ultra-rounded corners and pill shapes that eliminate visual "sharpness."
- **Institutional Vibrancy:** A sophisticated palette that uses professional blues as a foundation, accented by warm, joyful tones.
- **Human-Centric High-Fidelity:** Premium UI patterns like floating pill-shaped navigation bars and soft-elevation cards that feel modern and accessible.

## Colors

The palette is strategically designed to be "Calmly Vibrant," prioritizing high contrast for accessibility while maintaining a soft visual footprint.

- **Primary (Royal Blue):** The anchor of the system. Used for headers, primary actions, and brand identification to signal trust and authority.
- **Secondary (Coral):** Used for highlights and "active" emotional touchpoints. It provides a warm contrast to the blue without being aggressive.
- **Tertiary (Sunny Yellow):** Reserved for special CTAs (like "Donate") and joyful decorative accents.
- **Backgrounds:** The interface avoids clinical whites. **Surface Cream (#FCF9F4)** is the default page background to reduce eye strain. Pure White is reserved for elevated containers like cards or floating nav bars.
- **Neutral:** A deep navy is used for typography instead of black to maintain a softer, more sophisticated look while ensuring AAA legibility.

## Typography

This design system utilizes **Plus Jakarta Sans** for its friendly, rounded terminals and exceptional legibility at all scales.

- **Weight Strategy:** Headlines use Extra Bold or Bold weights to create a clear visual map. Body text never drops below Medium (500) to ensure accessibility for users with visual processing differences.
- **Clarity & Space:** Line heights are intentionally generous (1.6x+) to provide "air" between lines, aiding in tracking and reading comprehension.
- **Mixed Color Headlines:** Use Primary Blue for the main headline, but occasionally highlight key words in Secondary Coral to drive focus and warmth.

## Layout & Spacing

The layout philosophy prioritizes **Spacious Breathing Room** to reduce sensory overwhelm.

- **Grid Model:** A 12-column fixed grid for desktop (centered) and a 4-column fluid grid for mobile. 
- **The "Section Gap":** Generous vertical spacing (120px on desktop) is used between content blocks to signal a clear shift in topic, allowing the user to process one piece of information at a time.
- **Floating Navigation:** The header is a pill-shaped floating container with 24px of clearance from the top of the viewport, emphasizing the "modern/light" aesthetic.
- **Reflow:** On mobile, margins reduce to 20px, and section gaps tighten to 64px, but internal component padding remains high to maintain the "pillowy" feel.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Soft Ambient Shadows**.

- **Surface Tiers:**
    - **Base:** Surface Cream (#FCF9F4).
    - **Containers:** Pure White (#FFFFFF) for cards and floating bars.
- **Shadow Profile:** Shadows are extremely diffused and tinted with the Primary Blue. Avoid grey/black shadows. Use: `box-shadow: 0 12px 40px rgba(29, 43, 77, 0.06);`.
- **Micro-Depth:** Small elements like buttons or input fields use a subtle 1px border in a lightened version of the Primary Blue instead of shadows to keep the UI feeling crisp and light.

## Shapes

The shape language is **Organic and Fully Rounded**. Sharp edges are avoided to maintain a sense of safety and friendliness.

- **Base Corner Radius:** 0.5rem (8px) for small interactive components.
- **Large Container Radius:** 2rem (32px) for cards and section containers.
- **Pill Shape:** Used for all buttons, the global navigation bar, and decorative tags.
- **Image Treatment:** Images must use large organic clipping paths (e.g., asymmetrical rounded corners or "blob" masks) to integrate them into the soft aesthetic of the brand.

## Components

### Buttons
- **Primary CTA:** Pill-shaped, Primary Blue background with White text. Includes a subtle "lift" on hover (slight shadow increase and 1.02x scale).
- **Secondary/Alt:** Pill-shaped, Tertiary Yellow with Navy text. Used for critical "conversion" actions like "Donate" or "Enquire."
- **Ghost:** Pill-shaped, Primary Blue outline (2px) with Primary Blue text.

### Navigation
- **The "Floating Pill":** A white container with a 999px corner radius. Sits at the top of the screen with a subtle ambient shadow.

### Cards
- **High-Fidelity Cards:** Pure white background, 32px corner radius, and a soft primary-tinted shadow. Padding should be generous (minimum 40px).

### Input Fields
- **Soft Fields:** 12px corner radius, white background with a 2px light-blue border. Labels are always persistent above the field in Navy Bold.

### Accordions & Lists
- **Icon-Lead Accordions:** Use pill-shaped blue circles for "+" or "expand" icons.
- **Bullet Points:** Use Secondary Coral small circles instead of standard dots.

### Functional Accents
- **Progress Bars & Indicators:** Always use fully rounded (pill) caps and the Primary Blue for active states.