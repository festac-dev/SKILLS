---
name: google-google-mobile-ads-get-started
description: Provides instructions for integrating the Google Mobile Ads (GMA) SDK.
  Use this skill when the user wants to get started with, install, integrate, set
  up, or configure the SDK for AdMob or Ad Manager, GMA Next-Gen SDK or mobile ads
  framework in an Android, iOS, or Unity application.
metadata:
  version: 1.2.1
  category: GoogleAds
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Google Mobile Ads SDK - Install

## Workflow

1.  **Determine the user's platform**: Identify if the project is Android, iOS,
    or Unity. If unclear, ask before proceeding.

2. **Read the platform guide** for implementation details:
    - Android: `references/android-get-started.md`
    - iOS: `references/ios-get-started.md`
    - Unity: `references/unity-get-started.md`

3. **Follow these steps in order**:
   - [ ] Add the SDK dependency
   - [ ] Set the application identifier
   - [ ] Initialize the SDK
   - [ ] Verify the integration

4. After the SDK is successfully installed, ask the user to select an ad format
   to continue the integration.
