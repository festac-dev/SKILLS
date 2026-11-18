---
name: agentic-awesome-react-flow-architect-c3a622d5
description: Build production-ready ReactFlow applications with hierarchical navigation,
  performance optimization, and advanced state management.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# ReactFlow Architect

Build production-ready ReactFlow applications with hierarchical navigation, performance optimization, and advanced state management.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## Minimal Controlled Graph Example

Target React Flow v12 (`@xyflow/react`); use matching docs for older reactflow v11 projects. This is a starting component, not an implementation of hierarchy/history/persistence.

```tsx
import { ReactFlow, useNodesState, useEdgesState, addEdge, type Connection } from '@xyflow/react';
import { useCallback } from 'react';
import '@xyflow/react/dist/style.css';

const initialNodes = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'Start' } },
  { id: '2', position: { x: 250, y: 0 }, data: { label: 'Next' } },
];
export default function InteractiveGraph() {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const onConnect = useCallback((connection: Connection) =>
    setEdges(previous => addEdge(connection, previous)), [setEdges]);
  return <div style={{ width: '100%', height: 500 }}>
    <ReactFlow nodes={nodes} edges={edges} onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange} onConnect={onConnect} fitView />
  </div>;
}
```

Install the reviewed compatible package version in the host project and run its typecheck/browser checks. Hooks such as useReactFlow need a ReactFlowProvider ancestor outside the component invoking them; the minimal example avoids that hook. No compile or browser execution is asserted here.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
