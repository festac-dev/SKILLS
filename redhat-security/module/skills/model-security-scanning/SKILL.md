---
name: redhat-security-model-security-scanning
description: Scan AI models for malicious elements before loading in inference engines.
  Use when building or reviewing inference engines, model loading pipelines, or model
  distribution systems.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: inference-engine
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Model Security Scanning in Inference Engines

## Security Recommendation

Inference engines SHOULD scan models for malicious elements before loading them. This is a defense-in-depth control that complements signature verification.

## Threats Detected by Scanning

| Threat | Description |
|---|---|
| **Malicious code in weights** | Some weight formats (e.g., Python pickle) can embed arbitrary executable code |
| **Backdoored models** | Models with hidden behaviors triggered by specific inputs |
| **Embedded scripts** | Configuration files or metadata containing executable payloads |
| **Unsafe serialization formats** | Formats that execute code during deserialization |

## Unsafe Weight Formats

The inference engine SHOULD advise against or refuse to load weight formats that can include malicious code:

| Format | Risk Level | Recommendation |
|---|---|---|
| **Python pickle** (`.pkl`, `.pickle`) | High | Avoid; can execute arbitrary Python code on load |
| **PyTorch legacy** (`.pt`, `.pth` using pickle) | High | Prefer SafeTensors format instead |
| **SafeTensors** (`.safetensors`) | Low | Preferred; no code execution during deserialization |
| **GGUF** | Low | Safe format for quantized models |
| **ONNX** | Medium | Generally safe but verify custom operators |

## Implementation Checklist

- [ ] Implement model scanning in the model loading pipeline
- [ ] Detect and flag unsafe serialization formats (pickle-based weights)
- [ ] Prefer SafeTensors or other safe formats; warn or block unsafe formats
- [ ] Scan model metadata and configuration files for embedded scripts
- [ ] Log scanning results as security events
- [ ] Allow security teams to configure scanning policies (warn vs. block)
- [ ] Integrate with model registry scanning if available
