# Development Difficulties

## 1. Dynamic Element IDs
The dropdown menu trigger button had dynamically generated IDs (`radix-vue-dropdown-menu-trigger-v-2-0`), requiring fallback strategies with alternative locators and JavaScript clicks.

## 2. Post-Login Modal Dialog
After signing in, an OK button appeared in a modal dialog that needed to be handled before proceeding. This required waiting logic and error handling since the modal doesn't always appear.

## 3. Logout Button Element Type
The logout button was implemented as a `<p>` element instead of a standard `<button>`, requiring XPath adjustments to locate both variations.

## 4. Page Load Timing
The builder page required significant wait time after login for the "Touch Screen Mode" text to appear, necessitating extended timeouts (30 seconds).

## 5. JavaScript Click Requirement
Standard Selenium clicks failed on some elements due to page overlays or dynamic rendering, requiring JavaScript-based clicking as a fallback method.

## Solutions Applied
- Implemented multiple locator strategies with fallbacks
- Added explicit waits with proper timeout configurations
- Used JavaScript execution for problematic clicks
- Created robust error handling for optional elements
- Verified page state using text content rather than unstable element IDs
