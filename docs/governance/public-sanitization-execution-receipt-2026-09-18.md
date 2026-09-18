# Public Sanitization Execution Receipt — 2026-09-18

**Status:** VERIFIED_COMPLETE — exact-head CI passed and authorized sanitization merged to public `main`
**Repository:** `nova-infrastructure-systems/sharpe-nova-os`
**Baseline public main:** `41547dea493645a07ea755273c280400db4b59cc`
**Authority:** explicit Architect authorization on September 18, 2026
**Production effect:** none

## Authorized scope

The Architect authorized deletion-bearing public sanitization according to the
merged Pass 2 hygiene plan, while preserving required public contracts,
validators, Git history, and the private/public authority boundary.

The authorization explicitly excludes production-affecting action.

The Architect also ended pursuit of the NSF path and authorized removal of the
NSF program package from the current public tree.

## Canonical boundary

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

## Executed removal scope

Relative to the authorized baseline, PR #68 removed 388 current-tree paths while
preserving Git history.

```yaml
executed_removal_scope:
  deleted_paths_total: 388
  NSF_program_docs_removed: 19
  NSF_demo_paths_removed: 18
  private_runtime_or_state_paths_removed: 80
  other_removed_material:
    - superseded_root_surfaces
    - internal_CCO_operating_material
    - internal_content_production_material
    - internal_market_watch_records
    - operating_evidence_and_private_target_tests
    - runtime_coupled_examples
  canonical_contract_files_removed: 0
```

The public tree was reduced from 648 tracked paths at the authorized baseline to
a contract/proof-oriented projection. Governance receipts added during the
operation remain part of that projection.

## Public material preserved

The merged public tree retains the surfaces required to explain, inspect, and
validate Nova without carrying the production implementation:

- `README.md`, `CURRENT_STATE.md`, `CATEGORY.md`, and `SYSTEM_IDENTITY.md`;
- public architecture and governance doctrine;
- target-v2 external contracts and specifications;
- public schemas and synthetic fixtures;
- bounded static examples;
- public retail context contracts and evidence documents;
- public/private repository boundary documentation;
- deterministic public validators and contract tests;
- historical Legacy v1 documentation needed for provenance.

The hash-bound target-v2 external review-context contract is preserved
unchanged.

## Local verification evidence

```yaml
local_repository_validation:
  doctrine_lint: PASS_with_existing_deprecation_warnings
  decision_scenarios: 70_processed
  Gate_3_field_derivation_validator: PASS
  target_v2_contract_validator: PASS
  Gate_5_entry_design_validator: PASS
  public_surface_coherence: PASS
  pytest: 127_passed
  git_diff_check: PASS
  markdown_relative_link_errors: 0
```

GitHub independently reran the public verification workflow on exact head
`a85d1e72235efaeed59fcf69621216a7d4c5c856`. Public Projection CI run #1
completed successfully with 127 tests passed and 70 decision scenarios
processed. PR #68 then merged to public `main` as
`738988184d5dcf545c66362ae402e0b604f8cf21`.

## State separation

```yaml
repository_governance_surface_changed: true
canonical_corporate_state_changed: false
cross_agent_current_use_set_changed: false
production_runtime_changed: false
production_deployment_authorized: false
payment_or_settlement_effect: none
wallet_effect: none
chronology_effect: none
Reflex_Memory_effect: none
capital_effect: none
```

Removal from the current public tree does not make previously published material
secret. Git history preserves prior disclosure and provenance.

## Completion evidence

```yaml
completion_evidence:
  PR: 68
  exact_head: a85d1e72235efaeed59fcf69621216a7d4c5c856
  exact_head_CI:
    workflow: Public_Projection_CI
    run_number: 1
    result: PASS
    pytest: 127_passed
    decision_scenarios: 70_processed
  merge_commit: 738988184d5dcf545c66362ae402e0b604f8cf21
  public_main_verified_after_merge: true
  open_PRs_after_merge: 0
  Git_history_preserved: true
  production_effect: none
```

Repository metadata remains a separate presentation setting and does not affect
the completion of deletion-bearing current-tree sanitization.
