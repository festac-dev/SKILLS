---
name: microsoft-pydantic-models-py
description: Create Pydantic models following the multi-model pattern with Base, Create,
  Update, Response, and InDB variants. Use when defining API request/response schemas,
  database models, or data validation in Python applications using Pydantic v2.
license: MIT
metadata:
  author: Microsoft
  version: 1.0.0
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Pydantic Models

Create Pydantic models following the multi-model pattern for clean API contracts.

## Quick Start

Copy the template from [assets/template.py](assets/template.py) and replace placeholders:
- `{{ResourceName}}` → PascalCase name (e.g., `Project`)
- `{{resource_name}}` → snake_case name (e.g., `project`)

## Multi-Model Pattern

| Model | Purpose |
|-------|---------|
| `Base` | Common fields shared across models |
| `Create` | Request body for creation (required fields) |
| `Update` | Request body for updates (all optional) |
| `Response` | API response with all fields |
| `InDB` | Database document with `doc_type` |

## camelCase Aliases

```python
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class MyModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    workspace_id: str = Field(..., alias="workspaceId")
    created_at: datetime = Field(..., alias="createdAt")
```

## Optional Update Fields

```python
class MyUpdate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
```

## Database Document

```python
class MyInDB(MyResponse):
    doc_type: str = "my_resource"
```

## Integration Steps

1. Create models in `src/backend/app/models/`
2. Export from `src/backend/app/models/__init__.py`
3. Add corresponding TypeScript types

## Reference Files

| File | Contents |
|------|----------|
| [references/capabilities.md](references/capabilities.md) | Additional non-hero capabilities, operation-group coverage, and production checklists. |
