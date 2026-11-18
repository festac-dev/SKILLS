---
name: agentic-awesome-aws-serverless-dfae9431
description: Specialized skill for building production-ready serverless applications
  on AWS. Covers Lambda functions, API Gateway, DynamoDB, SQS/SNS event-driven patterns,
  SAM/CDK deployment, and cold start optimization.
metadata:
  upstream_headers:
    risk: critical
    source: vibeship-spawner-skills (Apache 2.0)
    date_added: 2026-02-27
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# AWS Serverless

Specialized skill for building production-ready serverless applications on AWS.
Covers Lambda functions, API Gateway, DynamoDB, SQS/SNS event-driven patterns,
SAM/CDK deployment, and cold start optimization.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## Scope and validation

Before deployment confirm account/region, IAM scope, resource changes, data retention and budget. Review the synthesized template/change set and verify in a scoped development environment. Bundled material is documentation only; helper handlers and deployment files shown in snippets are not present or runtime-tested here. Secrets need approved managed storage and least-privilege roles; do not paste credentials into logs.

## Monitor memory usage

```javascript
exports.handler = async (event, context) => {
  const used = process.memoryUsage();
  console.log('Memory:', {
    heapUsed: Math.round(used.heapUsed / 1024 / 1024) + 'MB',
    heapTotal: Math.round(used.heapTotal / 1024 / 1024) + 'MB'
  });
  // ...
};
```

## When to Use
Use this skill when the request clearly matches the capabilities and patterns described above.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
