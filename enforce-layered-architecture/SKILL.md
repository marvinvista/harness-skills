---
name: enforce-layered-architecture
description: Check a repository for dependency-direction and layering violations, scaffold or tighten structural rules, and summarize boundary failures that should become mechanical checks. Use when a codebase needs strict domain layering, provider boundaries, parse-at-the-boundary discipline, or custom lint rules that keep agent-written code from drifting.
---

# Enforce Layered Architecture

## Overview

Keep the architecture legible by enforcing boundaries mechanically instead of relying on review memory. Tighten the rule set around dependency direction, domain layering, and boundary parsing, then turn repeated violations into automated checks.

## Workflow

1. Define the architecture shape.
- Read [`references/layering-model.md`](references/layering-model.md) and [`references/rule-file-schema.md`](references/rule-file-schema.md).
- Make the allowed layer order and path mapping explicit in a rule file.

2. Run the structural check.
- Use [`scripts/check_layer_imports.py`](scripts/check_layer_imports.py) with a rules JSON file.
- Review the emitted violations grouped by source file and edge.

3. Decide whether the fix belongs in code or in tooling.
- If the rule is already clear, fix the imports or file placement.
- If the same violation pattern keeps returning, tighten the architecture rule file or create repo-native lint coverage.

4. Keep boundary rules distinct from taste rules.
- Use [`references/taste-vs-boundary.md`](references/taste-vs-boundary.md) to separate architecture constraints from style preferences.
- Use [`references/parse-at-boundary.md`](references/parse-at-boundary.md) to keep validation rules near system edges.

## Quality Bar

- Rules should be explicit enough to automate.
- Violations should identify both the illegal edge and the allowed direction.
- Boundary checks should focus on real architecture drift, not formatting noise.
- Repeated human review comments should become rule files or lint checks.

## Resources

- [`scripts/check_layer_imports.py`](scripts/check_layer_imports.py): Scan Python and JS/TS imports against a layer rule file.
- [`scripts/scaffold_arch_rules.py`](scripts/scaffold_arch_rules.py): Create a starter rules JSON file.
- [`references/layering-model.md`](references/layering-model.md): Suggested layer model and direction rules.
- [`references/rule-file-schema.md`](references/rule-file-schema.md): Rule file structure for the checker.
- [`references/parse-at-boundary.md`](references/parse-at-boundary.md): Boundary validation guidance.
- [`references/taste-vs-boundary.md`](references/taste-vs-boundary.md): Separate structural constraints from style.
