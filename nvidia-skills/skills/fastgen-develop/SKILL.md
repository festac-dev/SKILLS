---
name: nvidia-fastgen-develop
description: Implement, refactor or review NVIDIA FastGen library code using its shared
  design, formatting, documentation and testing conventions. Use for source changes
  and code reviews; configuring or running an existing workflow alone does not need
  this skill.
license: Apache-2.0
metadata:
  author: Julius Berner <jberner@nvidia.com>
  domain: ml
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Develop FastGen

Resolve the user's FastGen checkout separately from the installed skill. Use the requested
revision, or the current checkout, as the authority for linked policies and interfaces. Read
[Design and Maintenance](https://github.com/NVlabs/FastGen/blob/main/CONTRIBUTING.md#design-and-maintenance)
for the shared coding rules and the owning component's README and interface docstrings.
Use the requested scope and information already provided before asking for missing inputs.
For review-only requests, inspect and verify within scope, then report findings without editing.

1. **Trace.** Follow the affected callers and consumers before editing. For changes across
   data and model boundaries, inspect loader decoding in
   [datasets](https://github.com/NVlabs/FastGen/blob/main/fastgen/datasets/README.md),
   `FastGenModel.prepare_batch` in [model.py](https://github.com/NVlabs/FastGen/blob/main/fastgen/methods/model.py),
   `FastGenNetwork.build_conditioning` in [network.py](https://github.com/NVlabs/FastGen/blob/main/fastgen/networks/network.py)
   and `Trainer.train_step` in [trainer.py](https://github.com/NVlabs/FastGen/blob/main/fastgen/trainer.py)
   as relevant; place the change with the component that owns the behavior.
2. **Change.** Apply the shared rules to the implementation and affected callers, tests
   and documentation together. For new capabilities, also use
   [fastgen-add-network](https://github.com/NVlabs/FastGen/blob/main/skills/fastgen-add-network/SKILL.md),
   [fastgen-add-method](https://github.com/NVlabs/FastGen/blob/main/skills/fastgen-add-method/SKILL.md) or
   [fastgen-add-modality](https://github.com/NVlabs/FastGen/blob/main/skills/fastgen-add-modality/SKILL.md).
3. **Verify.** Follow the contributor guide's
   [formatting](https://github.com/NVlabs/FastGen/blob/main/CONTRIBUTING.md#code-style-and-formatting)
   and [checks](https://github.com/NVlabs/FastGen/blob/main/CONTRIBUTING.md#continuous-integration).
   Exercise changed behavior and requested boundary cases through real FastGen components
   and affected call sites; distinguish static checks from runtime tests. For patch
   deliverables, generate the diff from complete target files and check it against clean
   files at the selected revision. If a failure crosses interfaces, trace the producer
   and consumer contracts before adding another check or workaround.

Report source-backed findings or changed behavior, affected interfaces and documentation,
checks actually run and any unverified paths.
