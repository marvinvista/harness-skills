# Public Manifest

These are the minimum files exported for public users.

## Root Files

- `README.md`
- `PUBLIC_MANIFEST.md`
- `index.md`
- `.githooks/pre-push`
- `.github/workflows/public-repo-safety.yml`
- `scripts/check_public_repo_safety.py`
- `scripts/validate_skill_pack.py`

## capture-repo-knowledge

- `capture-repo-knowledge/SKILL.md`
- `capture-repo-knowledge/agents/openai.yaml`
- `capture-repo-knowledge/references/adr-template.md`
- `capture-repo-knowledge/references/decision-capture-rubric.md`
- `capture-repo-knowledge/references/design-doc-template.md`
- `capture-repo-knowledge/references/doc-type-selector.md`
- `capture-repo-knowledge/references/product-spec-template.md`
- `capture-repo-knowledge/scripts/new_adr.py`
- `capture-repo-knowledge/scripts/new_design_doc.py`
- `capture-repo-knowledge/scripts/normalize_meeting_notes.py`

## clean-agent-drift

- `clean-agent-drift/SKILL.md`
- `clean-agent-drift/agents/openai.yaml`
- `clean-agent-drift/references/cleanup-batch-rubric.md`
- `clean-agent-drift/references/drift-pattern-catalog.md`
- `clean-agent-drift/references/golden-principles.md`
- `clean-agent-drift/references/refactor-pr-sizing.md`
- `clean-agent-drift/scripts/find_duplicate_snippets.py`
- `clean-agent-drift/scripts/scan_drift_patterns.py`
- `clean-agent-drift/scripts/summarize_drift_findings.py`

## enforce-layered-architecture

- `enforce-layered-architecture/SKILL.md`
- `enforce-layered-architecture/agents/openai.yaml`
- `enforce-layered-architecture/references/layering-model.md`
- `enforce-layered-architecture/references/parse-at-boundary.md`
- `enforce-layered-architecture/references/rule-file-schema.md`
- `enforce-layered-architecture/references/taste-vs-boundary.md`
- `enforce-layered-architecture/scripts/check_layer_imports.py`
- `enforce-layered-architecture/scripts/scaffold_arch_rules.py`

## enforce-taste-invariants

- `enforce-taste-invariants/SKILL.md`
- `enforce-taste-invariants/agents/openai.yaml`
- `enforce-taste-invariants/references/naming-convention-guidance.md`
- `enforce-taste-invariants/references/rule-promotion-guide.md`
- `enforce-taste-invariants/references/structured-logging-guidance.md`
- `enforce-taste-invariants/references/taste-rule-schema.md`
- `enforce-taste-invariants/scripts/check_file_size_limits.py`
- `enforce-taste-invariants/scripts/check_filename_patterns.py`
- `enforce-taste-invariants/scripts/init_taste_rules.py`
- `enforce-taste-invariants/scripts/scan_taste_patterns.py`

## garden-repo-docs

- `garden-repo-docs/SKILL.md`
- `garden-repo-docs/agents/openai.yaml`
- `garden-repo-docs/references/agents-md-principles.md`
- `garden-repo-docs/references/crosslinking-rules.md`
- `garden-repo-docs/references/doc-freshness-checklist.md`
- `garden-repo-docs/references/docs-layout-contract.md`
- `garden-repo-docs/scripts/check_doc_links.py`
- `garden-repo-docs/scripts/find_unindexed_docs.py`
- `garden-repo-docs/scripts/scan_doc_freshness.py`

## manage-exec-plans

- `manage-exec-plans/SKILL.md`
- `manage-exec-plans/agents/openai.yaml`
- `manage-exec-plans/references/active-vs-completed.md`
- `manage-exec-plans/references/decision-log-rubric.md`
- `manage-exec-plans/references/plan-examples.md`
- `manage-exec-plans/references/plan-template.md`
- `manage-exec-plans/scripts/append_decision_log.py`
- `manage-exec-plans/scripts/init_exec_plan.py`
- `manage-exec-plans/scripts/move_exec_plan.py`

## provision-worktree-stack

- `provision-worktree-stack/SKILL.md`
- `provision-worktree-stack/agents/openai.yaml`
- `provision-worktree-stack/references/env-file-conventions.md`
- `provision-worktree-stack/references/healthcheck-rubric.md`
- `provision-worktree-stack/references/stack-layout.md`
- `provision-worktree-stack/references/teardown-checklist.md`
- `provision-worktree-stack/scripts/derive_worktree_ports.py`
- `provision-worktree-stack/scripts/render_env_file.py`
- `provision-worktree-stack/scripts/stop_background_processes.sh`
- `provision-worktree-stack/scripts/wait_for_http_health.py`

## record-bug-evidence

- `record-bug-evidence/SKILL.md`
- `record-bug-evidence/agents/openai.yaml`
- `record-bug-evidence/references/artifact-naming.md`
- `record-bug-evidence/references/before-after-checklist.md`
- `record-bug-evidence/references/escalation-criteria.md`
- `record-bug-evidence/references/repro-note-template.md`
- `record-bug-evidence/scripts/init_evidence_bundle.py`
- `record-bug-evidence/scripts/summarize_evidence_bundle.py`
- `record-bug-evidence/scripts/write_repro_note.py`

## run-pr-review-loop

- `run-pr-review-loop/SKILL.md`
- `run-pr-review-loop/agents/openai.yaml`
- `run-pr-review-loop/references/common-regression-patterns.md`
- `run-pr-review-loop/references/pr-ready-criteria.md`
- `run-pr-review-loop/references/response-style-guide.md`
- `run-pr-review-loop/references/review-checklist.md`
- `run-pr-review-loop/scripts/collect_review_feedback.sh`
- `run-pr-review-loop/scripts/rerun_validation_suite.sh`
- `run-pr-review-loop/scripts/summarize_pr_risks.py`

## scaffold-agent-repo

- `scaffold-agent-repo/SKILL.md`
- `scaffold-agent-repo/agents/openai.yaml`
- `scaffold-agent-repo/references/agents-md-guidelines.md`
- `scaffold-agent-repo/references/conversion-strategy.md`
- `scaffold-agent-repo/references/repo-layout.md`
- `scaffold-agent-repo/references/starter-file-purpose.md`
- `scaffold-agent-repo/scripts/check_agent_repo_layout.py`
- `scaffold-agent-repo/scripts/init_agent_repo.py`
- `scaffold-agent-repo/scripts/rebuild_markdown_index.py`

## triage-observability

- `triage-observability/SKILL.md`
- `triage-observability/agents/openai.yaml`
- `triage-observability/references/log-query-playbook.md`
- `triage-observability/references/observability-entrypoints.md`
- `triage-observability/references/performance-budget-rubric.md`
- `triage-observability/references/trace-triage-checklist.md`
- `triage-observability/scripts/evaluate_metrics_budget.py`
- `triage-observability/scripts/scan_json_logs.py`
- `triage-observability/scripts/summarize_trace_spans.py`

## update-quality-grades

- `update-quality-grades/SKILL.md`
- `update-quality-grades/agents/openai.yaml`
- `update-quality-grades/references/evidence-sources.md`
- `update-quality-grades/references/follow-up-prioritization.md`
- `update-quality-grades/references/quality-dimensions.md`
- `update-quality-grades/references/scoring-guidelines.md`
- `update-quality-grades/scripts/highlight_low_scores.py`
- `update-quality-grades/scripts/init_quality_rubric.py`
- `update-quality-grades/scripts/score_quality_matrix.py`

## verify-ui-journeys

- `verify-ui-journeys/SKILL.md`
- `verify-ui-journeys/agents/openai.yaml`
- `verify-ui-journeys/assets/journey-template.spec.ts`
- `verify-ui-journeys/references/known-flaky-flows.md`
- `verify-ui-journeys/references/route-map.md`
- `verify-ui-journeys/references/test-accounts.md`
- `verify-ui-journeys/references/ui-verification-checklist.md`
- `verify-ui-journeys/scripts/boot_worktree_app.sh`
