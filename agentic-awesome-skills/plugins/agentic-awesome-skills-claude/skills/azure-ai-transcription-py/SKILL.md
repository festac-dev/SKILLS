---
name: agentic-awesome-azure-ai-transcription-py-70f307e0
description: Azure AI Transcription SDK for Python. Use for audio-file transcription
  with timestamps; distinguish this client from streaming and asynchronous batch Speech
  APIs.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Azure AI Speech Transcription for Python

## When to Use

- Transcribe an authorized audio file with the `azure-ai-transcription` client.
- Review timestamped output and options supported by the installed SDK version.
- For streaming or asynchronous batch jobs, select the appropriate Speech API instead.

## Prerequisites

Use a project-pinned SDK in an isolated Python environment. Confirm the Speech
resource, endpoint, permissions, audio consent, cost and retention before upload.
Do not log keys, audio contents, or full transcripts by default.

## File Example

```python
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.transcription import TranscriptionClient
from azure.ai.transcription.models import TranscriptionContent, TranscriptionOptions

client = TranscriptionClient(
    endpoint=os.environ["TRANSCRIPTION_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["TRANSCRIPTION_KEY"]),
)
with client:
    with open("audio.wav", "rb") as audio:
        result = client.transcribe(TranscriptionContent(
            definition=TranscriptionOptions(locales=["en-US"]), audio=audio,
        ))
# Inspect result locally; handle empty output and service errors explicitly.
```

## Authentication and API Boundary

`DefaultAzureCredential` is also supported when the identity has the required
resource role. The previous `begin_transcription` and `begin_stream_transcription`
examples did not match this client. Do not invent a streaming adapter.

## Example Request

“Transcribe this consented local recording; keep the transcript private.”

## Limitations

Verify installed signatures and service limits against [Microsoft's SDK guide](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-transcription-readme?view=azure-python).
This illustration has not contacted Azure; availability, accuracy and costs require
verification in the authorized environment.
