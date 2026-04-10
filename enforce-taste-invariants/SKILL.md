---
name: enforce-taste-invariants
description: Enforce agreed mechanical style rules such as structured logging, file-size limits, filename conventions, and banned patterns, then summarize violations that should become lint checks. Use when review comments keep repeating taste-level issues that are not architecture boundaries but still need consistent, automated enforcement.
---

# Enforce Taste Invariants

## Overview

Treat taste rules as mechanical contracts, not preferences that should be rediscovered in review. Keep them separate from architecture boundaries and express them clearly enough that a script or linter can check them.

## Workflow

1. Start from agreed repo taste, not personal style.
- Read [`references/taste-rule-schema.md`](references/taste-rule-schema.md), [`references/structured-logging-guidance.md`](references/structured-logging-guidance.md), and [`references/naming-convention-guidance.md`](references/naming-convention-guidance.md).
- Promote only repeated, stable review feedback into taste rules.

2. Scaffold or update the rule file.
- Use [`scripts/init_taste_rules.py`](scripts/init_taste_rules.py) to create a starter rules JSON.
- Keep size limits, filename rules, and forbidden patterns explicit.

3. Run the mechanical checks.
- Use [`scripts/check_file_size_limits.py`](scripts/check_file_size_limits.py) for line-count limits.
- Use [`scripts/check_filename_patterns.py`](scripts/check_filename_patterns.py) for filename conventions.
- Use [`scripts/scan_taste_patterns.py`](scripts/scan_taste_patterns.py) for forbidden regex patterns such as stray debug logging or ignored type errors.

4. Decide what to encode next.
- If the same review comment keeps repeating, add or tighten a rule.
- If the rule is too fuzzy to automate, keep it out of this skill and treat it as guidance instead.

## Quality Bar

- Every rule should have a clear message and scope.
- Violations should point to an actionable fix, not just a complaint.
- Taste rules should stay mechanical and low-ambiguity.
- Prefer a small stable rule set over a giant preference catalog.

## Resources

- [`scripts/init_taste_rules.py`](scripts/init_taste_rules.py): Create a starter taste-rules JSON file.
- [`scripts/check_file_size_limits.py`](scripts/check_file_size_limits.py): Flag files that exceed configured line limits.
- [`scripts/check_filename_patterns.py`](scripts/check_filename_patterns.py): Flag files whose names violate configured regex rules.
- [`scripts/scan_taste_patterns.py`](scripts/scan_taste_patterns.py): Scan files for forbidden regex patterns.
- [`references/taste-rule-schema.md`](references/taste-rule-schema.md): Rule file structure.
- [`references/structured-logging-guidance.md`](references/structured-logging-guidance.md): Example mechanical logging standards.
- [`references/naming-convention-guidance.md`](references/naming-convention-guidance.md): Naming rules worth enforcing.
- [`references/rule-promotion-guide.md`](references/rule-promotion-guide.md): When to turn review feedback into a rule.
