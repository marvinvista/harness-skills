---
name: capture-repo-knowledge
description: Turn external or tacit project knowledge into repository-local artifacts such as ADRs, design docs, product specs, and reference notes. Use when important decisions live in Slack, meetings, PR threads, or people’s heads and need to become legible to future agent runs.
---

# Capture Repo Knowledge

## Overview

Make project knowledge visible to future agent runs by writing it into the repository in the right format and location. Prefer durable, discoverable artifacts over chat summaries that disappear after the current thread.

## Workflow

1. Pick the right artifact type.
- Use [`references/doc-type-selector.md`](references/doc-type-selector.md) to decide between ADR, design doc, product spec, or reference note.
- Write the smallest artifact that preserves the decision and next lookup path.

2. Normalize the input material.
- Distill the external context into decisions, action items, open questions, and supporting notes.
- Use [`scripts/normalize_meeting_notes.py`](scripts/normalize_meeting_notes.py) when the raw notes are noisy.

3. Generate the repository-local document.
- Use [`scripts/new_adr.py`](scripts/new_adr.py) for architecture decisions.
- Use [`scripts/new_design_doc.py`](scripts/new_design_doc.py) for broader implementation context.
- Use the reference templates when creating product specs or long-form notes by hand.

4. Link the new artifact into the repo map.
- Add cross-links from the nearest index, plan, or owning doc.
- Mention affected code paths, services, or product areas so future searches find it.

## Quality Bar

- Preserve the decision and rationale, not the whole meeting transcript.
- Record unresolved questions explicitly.
- Prefer repo-native markdown over external references when possible.
- Write for a future run that has no access to the original conversation.

## Resources

- [`scripts/new_adr.py`](scripts/new_adr.py): Create a numbered ADR from the shared template.
- [`scripts/new_design_doc.py`](scripts/new_design_doc.py): Create a dated design doc.
- [`scripts/normalize_meeting_notes.py`](scripts/normalize_meeting_notes.py): Convert rough notes into structured markdown.
- [`references/doc-type-selector.md`](references/doc-type-selector.md): Choose the correct document type.
- [`references/adr-template.md`](references/adr-template.md): ADR structure and prompts.
- [`references/design-doc-template.md`](references/design-doc-template.md): Design doc structure.
- [`references/product-spec-template.md`](references/product-spec-template.md): Product spec structure.
- [`references/decision-capture-rubric.md`](references/decision-capture-rubric.md): What to preserve from external context.
