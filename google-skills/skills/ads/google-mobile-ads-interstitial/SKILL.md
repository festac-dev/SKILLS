---
name: google-google-mobile-ads-interstitial
description: Provides instructions for implementing, integrating, or configuring Google
  Mobile Ads (GMA) SDK interstitial ads in Android, iOS, or Unity mobile applications.
  Use when the task involves setting up interstitial ads. Don't use for "rewarded
  interstitial" ads.
metadata:
  version: 1.1.0
  category: GoogleAds
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Google Mobile Ads SDK - Interstitial Ads

Interstitial ads show full-page ads for users on mobile apps. Interstitial ads
are designed to be placed between content and are best placed at natural app
transition points.

## Workflow

1.  **Determine the user's platform**: Identify if the project is Android,
    iOS, or Unity. If unclear, ask before proceeding.

2.  **Read the platform guide** for implementation details:
    -   Android: `references/android-interstitial.md`
    -   iOS: `references/ios-interstitial.md`
    -   Unity: `references/unity-interstitial.md`

3.  **Follow these steps in order**:
    -   [ ] Load the ad
    -   [ ] Register for ad event callbacks
    -   [ ] Show the ad
    -   [ ] Verify the implementation
