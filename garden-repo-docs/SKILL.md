---
name: garden-repo-docs
description: Audit repository documentation for staleness, broken cross-links, missing indexes, and mismatches with current code behavior, then apply or propose targeted fixes. Use when docs may have drifted after refactors, when AGENTS.md or index files feel stale, or when the repo treats docs as the system of record.
---

# Garden Repo Docs

## Overview

Treat repository docs as code that can drift, break, and silently mislead future runs. Look for small, high-leverage fixes that restore discoverability and accuracy without turning the task into a full rewrite.

## Workflow

1. Start with structure.
- Read [`references/docs-layout-contract.md`](references/docs-layout-contract.md).
- Confirm the repo has a clear entry point, index files, and canonical locations for plans, specs, and references.

2. Scan for mechanical issues first.
- Run [`scripts/check_doc_links.py`](scripts/check_doc_links.py) to find broken relative links.
- Run [`scripts/find_unindexed_docs.py`](scripts/find_unindexed_docs.py) to find docs that are not discoverable from index files.
- Run [`scripts/scan_doc_freshness.py`](scripts/scan_doc_freshness.py) to find files that are missing freshness metadata or review signals.

3. Fix the highest-value drift.
- Prefer repairing docs that influence agent navigation: `AGENTS.md`, architecture maps, design indexes, and execution-plan indexes.
- Update the smallest source of truth that restores correctness.
- Add or repair cross-links while you are in the file.

4. Leave the docs more legible than you found them.
- Keep indexes current.
- Keep guidance short and specific.
- Remove or rewrite stale claims instead of layering on caveats.

## Quality Bar

- Prefer targeted doc PRs over bulk “cleanup” rewrites.
- Make the entry path discoverable from one or two stable files.
- Align docs with actual code, not intent or memory.
- Keep agent-facing docs concise and structured for navigation.

## Resources

- [`scripts/check_doc_links.py`](scripts/check_doc_links.py): Validate relative markdown links.
- [`scripts/find_unindexed_docs.py`](scripts/find_unindexed_docs.py): Report docs that no index points to.
- [`scripts/scan_doc_freshness.py`](scripts/scan_doc_freshness.py): Surface stale or unreviewed files.
- [`references/docs-layout-contract.md`](references/docs-layout-contract.md): What “system of record” layout should feel like.
- [`references/doc-freshness-checklist.md`](references/doc-freshness-checklist.md): Quick audit prompts.
- [`references/agents-md-principles.md`](references/agents-md-principles.md): Keep `AGENTS.md` short and navigational.
- [`references/crosslinking-rules.md`](references/crosslinking-rules.md): Cross-linking norms for doc discoverability.
