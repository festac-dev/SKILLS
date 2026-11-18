---
name: microsoft-azure-communication-callingserver-java
description: Azure Communication Services CallingServer (legacy) Java SDK. Note -
  This SDK is deprecated. Use azure-communication-callautomation instead for new projects.
  Only use this skill when maintaining legacy code.
license: MIT
metadata:
  author: Microsoft
  version: 1.0.0
  package: com.azure:azure-communication-callingserver
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Azure Communication CallingServer (Java) - DEPRECATED

> **⚠️ DEPRECATED**: This SDK has been renamed to **Call Automation**. For new projects, use `azure-communication-callautomation` instead. This skill is for maintaining legacy code only.

## Migration to Call Automation

```xml
<!-- OLD (deprecated) -->
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-communication-callingserver</artifactId>
    <version>1.0.0-beta.5</version>
</dependency>

<!-- NEW (use this instead) -->
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-communication-callautomation</artifactId>
    <version>1.6.0</version>
</dependency>
```

## Class Name Changes

| CallingServer (Old) | Call Automation (New) |
|---------------------|----------------------|
| `CallingServerClient` | `CallAutomationClient` |
| `CallingServerClientBuilder` | `CallAutomationClientBuilder` |
| `CallConnection` | `CallConnection` (same) |
| `ServerCall` | Removed - use `CallConnection` |

## Legacy Client Creation

```java
// OLD WAY (deprecated)
import com.azure.communication.callingserver.CallingServerClient;
import com.azure.communication.callingserver.CallingServerClientBuilder;

CallingServerClient client = new CallingServerClientBuilder()
    .connectionString("<connection-string>")
    .buildClient();

// NEW WAY
import com.azure.communication.callautomation.CallAutomationClient;
import com.azure.communication.callautomation.CallAutomationClientBuilder;

CallAutomationClient client = new CallAutomationClientBuilder()
    .connectionString("<connection-string>")
    .buildClient();
```

## Legacy Recording

```java
// OLD WAY
StartRecordingOptions options = new StartRecordingOptions(serverCallId)
    .setRecordingStateCallbackUri(callbackUri);

StartCallRecordingResult result = client.startRecording(options);
String recordingId = result.getRecordingId();

client.pauseRecording(recordingId);
client.resumeRecording(recordingId);
client.stopRecording(recordingId);

// NEW WAY - see azure-communication-callautomation skill
```

## For New Development

**Do not use this SDK for new projects.** 

See the `azure-communication-callautomation-java` skill for:
- Making outbound calls
- Answering incoming calls
- Call recording
- DTMF recognition
- Text-to-speech / speech-to-text
- Adding/removing participants
- Call transfer

## Trigger Phrases

- "callingserver legacy", "deprecated calling SDK"
- "migrate callingserver to callautomation"
