---
name: agentic-awesome-n8n-expression-syntax-32d9ba4d
description: Validate n8n expression syntax and fix common errors. Use when writing
  n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting
  expression errors, or working with webhook data in workflows.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-03-06'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# n8n Expression Syntax

Expert guide for writing correct n8n expressions in workflows.

## Execution and data scope

EXAMPLES.md and COMMON_MISTAKES.md referenced below/in the guide are not bundled. `$json` in expression parameters represents the current input item, not a completed current node output; inspect actual execution data and item linking before referencing another node. Code-node APIs differ between per-item and all-items modes. Use credentials for secrets: the guide's `$env` examples can expose values and may be disabled. Avoid putting secrets/personal webhook data into messages or logs. Encode URL path/query components, guard missing arrays/objects and validate untrusted values before downstream actions. Test expressions with synthetic input; preview success is not authorization to send Slack/email messages.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use
- You need to write or debug n8n expressions using `{{ ... }}` syntax.
- The task involves `$json`, `$node`, webhook payloads, or expression-related workflow errors.
- You want syntax-correct dynamic values inside n8n nodes and parameters.

---

## When NOT to Use Expressions

### ❌ Code Nodes

Code nodes use **direct JavaScript access**, NOT expressions!

```javascript
// ❌ WRONG in Code node
const email = '={{$json.email}}';
const name = '{{$json.body.name}}';

// ✅ CORRECT in Code node
const email = $json.email;
const name = $json.body.name;

// Or using Code node API
const email = $input.item.json.email;
const allItems = $input.all();
```

### ❌ Webhook Paths

```javascript
// ❌ WRONG
path: "{{$json.user_id}}/webhook"

// ✅ CORRECT
path: "user-webhook"  // Static paths only
```

### ❌ Credential Fields

```javascript
// ❌ WRONG
apiKey: "={{$env.API_KEY}}"

// ✅ CORRECT
Use n8n credential system, not expressions
```

---

## Working Examples

For real workflow examples, see EXAMPLES.md

### Example 1: Webhook to Slack

**Webhook receives**:
```json
{
  "body": {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello!"
  }
}
```

**In Slack node text field**:
```
New form submission!

Name: {{$json.body.name}}
Email: {{$json.body.email}}
Message: {{$json.body.message}}
```

### Example 2: HTTP Request to Email

**HTTP Request returns**:
```json
{
  "data": {
    "items": [
      {"name": "Product 1", "price": 29.99}
    ]
  }
}
```

**In Email node** (reference HTTP Request):
```
Product: {{$node["HTTP Request"].json.data.items[0].name}}
Price: ${{$node["HTTP Request"].json.data.items[0].price}}
```

### Example 3: Format Timestamp

```javascript
// Current date
{{$now.toFormat('yyyy-MM-dd')}}
// Result: 2025-10-20

// Time
{{$now.toFormat('HH:mm:ss')}}
// Result: 14:30:45

// Full datetime
{{$now.toFormat('yyyy-MM-dd HH:mm')}}
// Result: 2025-10-20 14:30
```

---

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
