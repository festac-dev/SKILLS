---
name: google-accidental-data-loss-prevention
description: '**STOP AND VERIFY**: Before running any command or tool that results
  in irreversible data loss, you MUST obtain explicit user consent.

  When in doubt, ask. It is better to wait for confirmation than to accidentally delete
  production data or critical project assets.

  Use this for:

  - SQL: DROP TABLE/VIEW/SCHEMA/DATABASE, TRUNCATE, or broad DELETE (missing WHERE
  or using 1=1).

  - Cloud Storage: gsutil rm or gcloud storage rm targeting production data or critical
  buckets.

  - Infrastructure: gcloud projects delete, deleting Spanner/BigQuery/Dataproc resources,
  deleting secrets, or KMS key destruction.

  '
license: Apache-2.0
metadata:
  version: v1
  publisher: google
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Accidental Data Loss Prevention

> [!CAUTION]
>
> **STOP AND VERIFY**: Before running any command or tool that results in
> irreversible data loss, you **MUST** obtain explicit user consent.

## Mandatory Procedure

1.  **Halt Execution**: Do **not** execute the command.
2.  **Request Consent**: Explain clearly to the user:
    -   The **impact** of this deletion.
    -   **Why** you believe this is necessary.
    -   A request for their **explicit approval** to proceed.
3.  **Wait**: Only proceed if the user provides clear, affirmative consent in
    the conversation.
