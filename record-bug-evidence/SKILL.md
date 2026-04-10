---
name: record-bug-evidence
description: Create a before-and-after evidence bundle for a bug, including repro notes, artifact manifests, and summary markdown. Use when a fix needs reviewable proof, when a bug must be handed off with clear repro context, or when screenshots, recordings, logs, or traces should be packaged consistently.
---

# Record Bug Evidence

## Overview

Make bug evidence reviewable and reusable by packaging it the same way every time. Keep the bundle focused on the repro, the artifacts, and the before-and-after story rather than a loose pile of screenshots and logs.

## Workflow

1. Initialize the evidence bundle.
- Use [`scripts/init_evidence_bundle.py`](scripts/init_evidence_bundle.py) to create a standard bundle directory with `before/`, `after/`, `logs/`, and `notes/`.
- Use [`references/artifact-naming.md`](references/artifact-naming.md) so bundle files are sortable and obvious.

2. Capture the failure state.
- Save screenshots, videos, logs, traces, or DOM snapshots into the `before/` and `logs/` directories.
- Write the repro context with [`scripts/write_repro_note.py`](scripts/write_repro_note.py).

3. Capture the fixed state.
- Re-run the same path and collect matching `after/` artifacts.
- Check [`references/before-after-checklist.md`](references/before-after-checklist.md) so the comparison is fair.

4. Summarize the bundle.
- Use [`scripts/summarize_evidence_bundle.py`](scripts/summarize_evidence_bundle.py) to generate a markdown summary of the artifacts and notes.
- Escalate when the bundle shows ambiguity using [`references/escalation-criteria.md`](references/escalation-criteria.md).

## Quality Bar

- The bundle should make the repro and resolution legible to someone who did not watch the session live.
- Before and after artifacts should correspond to the same path or state.
- Notes should describe expected versus actual behavior, not just list files.
- Keep artifact names stable and sortable.

## Resources

- [`scripts/init_evidence_bundle.py`](scripts/init_evidence_bundle.py): Create a standard evidence bundle folder.
- [`scripts/write_repro_note.py`](scripts/write_repro_note.py): Write or update a markdown repro note.
- [`scripts/summarize_evidence_bundle.py`](scripts/summarize_evidence_bundle.py): Build a markdown summary from an evidence bundle.
- [`references/repro-note-template.md`](references/repro-note-template.md): Repro note structure.
- [`references/artifact-naming.md`](references/artifact-naming.md): Artifact naming guidance.
- [`references/before-after-checklist.md`](references/before-after-checklist.md): Checklist for fair before/after capture.
- [`references/escalation-criteria.md`](references/escalation-criteria.md): When evidence is still insufficient.
