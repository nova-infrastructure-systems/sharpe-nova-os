# Public Sanitization Execution Receipt — 2026-09-18

**Status:** authorized deletion-bearing repository sanitization; candidate prepared pending exact-head CI and merge
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

## Candidate removal scope

Relative to the authorized baseline, the candidate removes 388 current-tree
paths while preserving Git history.

```yaml
candidate_removal_scope:
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

The current public tree is reduced from 648 tracked paths at baseline to a
contract/proof-oriented projection. The final tracked-path count may differ by
one or more governance receipt files added to document the sanitization itself.

## Public material preserved

The candidate retains the public surfaces required to explain, inspect, and
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

This is local repository evidence. Exact-head GitHub CI remains required before
merge.

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

## Completion condition

The sanitization becomes repository-complete only after:

1. the exact candidate head passes GitHub CI;
2. the changed-file scope is reviewed against this receipt;
3. the PR is merged to public `main`;
4. public `main` and open-PR state are freshly reverified;
5. repository metadata is reconciled separately where supported.
