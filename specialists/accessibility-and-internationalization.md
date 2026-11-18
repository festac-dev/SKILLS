# Specialist: Accessibility and Internationalization

Evaluate semantic structure, keyboard operation, focus visibility, accessible names, screen-reader announcements, contrast, zoom/reflow, captions, form errors and motion sensitivity.

Support localization where required: translated content expansion, locale-aware dates, numbers, currencies, pluralization, time zones, RTL and appropriate fonts. Do not assume one locale or one device context. Use recognized standards and test actual flows; do not claim conformance based on a superficial checklist.

## Applied verification

After a validation error, follow focus and the announced message through correction and successful submission. Repeat with expanded translated labels and an RTL locale when supported; confirm dates and monetary values keep their intended meaning.

## Platform and locale checks

Check accessible authentication, unobscured focus, target-size exceptions, captions and sustained-motion controls against the applicable standard. Include the project’s screen reader, forced-color and zoom/reflow combinations; an automated score does not establish conformance. For localization, preserve grammatical messages rather than concatenated strings, test RTL with logical properties, localized numbers/dates and script coverage, and verify expansion with representative translations. Use the [localization review](../templates/LOCALIZATION_READINESS.md).
