# Canonical Terminology Registry

This registry is the current public language surface for Sharpe Nova OS. It exists
to preserve the approved pre-execution governance category, the non-authority
boundary, decision-state precision, chronology integrity, and semantic
compatibility across public documentation, examples, and governance artifacts.

Corporate commercial and external-narrative authority is governed in
`nova-infrastructure-systems/nova-infrastructure-corporate`. Sharpe Nova OS
technical accepted state remains governed in `nova-infrastructure-systems/nova-core`.
This public registry is a non-authoritative projection of those approved boundaries.

## Product-Generation Terminology Scope

```yaml
terminology_scope:
  canonical_future_external_terms:
    - review_context
    - prepared_action
    - source_state
    - contradiction_context
    - constraint_context
    - temporal_context
    - review_completeness
    - chronology_context
    - authority_handoff
    - context_integrity_proof

  Legacy_v1_terms:
    - decision_admission
    - decision_status
    - permission_budget
    - ALLOW
    - CONSTRAIN
    - VETO
    - DENY
    - HALT
```

Legacy v1 terms may remain in implementation, migration, replay, and historical
documentation. They must not be used as the canonical description of Nova’s
future external product.

## Canonical Positioning

Sharpe Nova OS is a pre-execution decision discipline layer that conditions
capital through telemetry, Reflex Memory, and constraint logic before execution.

Nova structures review context for agent-prepared capital actions before local
institutional authority decides.

Canonical operating boundary:

```text
Agent prepares action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

Nova is not:

- a trading system;
- a signal engine;
- a prediction layer;
- a portfolio optimizer;
- an execution layer;
- an institutional approval or authorization authority.

The implemented Legacy v1 runtime contains decision-admission terminology and
behavior. Those terms remain valid for implementation, replay, migration, and
historical reference, but they are not the canonical future external product
language.

## Approved Canonical Phrases

- pre-execution governance infrastructure
- consequential machine-prepared capital actions
- pre-execution decision discipline layer
- governed pre-execution review state
- bounded governed pre-execution review state presented to local authority
- local authority
- exact-action review context
- decision-state preservation
- source provenance
- source state
- constraint applicability
- unresolved-state preservation
- temporal integrity
- proposal-version identity
- material change
- reconsideration condition
- explicit authority handoff
- Reflex Memory
- chronology integrity
- context integrity proof
- authority_effect = none

## Current Definitions

- Pre-execution governance infrastructure: Infrastructure that structures and
  preserves bounded governed review state before local authority decides and
  external systems execute.
- Governed review state: The relationship among the exact proposed action,
  relevant evidence and source state, applicable constraints, unresolved
  conditions, relevant prior context, material changes, and authority handoff at
  the review moment.
- Decision-state preservation: Preserving what local authority actually received
  and what remained applicable or unresolved before deciding.
- Temporal integrity: Keeping what was known and applicable at decision time
  distinct from information or resolution that arrived later.
- Reconsideration condition: A material change that may require local authority
  to re-evaluate the governed basis on which an operating mandate or prior review
  was relying.
- Reflex Memory: Governed prior context that may condition review without
  becoming present policy or authority.

## Deprecated Phrases

Use these only inside explicit migration, audit, or boundary-validation artifacts.

- payment-permission layer
- execution permission
- decision approval
- trading-signal system
- prediction system
- optimization engine
- execution middleware
- AI signal infrastructure
- alpha generation
- trading optimization
- recommendation engine
- dashboard tooling

## Migration Mappings

- payment-permission layer -> governed pre-execution review state
- execution permission -> local authority decision outside Nova
- decision approval -> bounded review context presented to local authority
- trading-signal system -> pre-execution governance infrastructure
- prediction system -> source-aware review context
- optimization engine -> outside Nova's category
- execution middleware -> external execution system
- AI signal infrastructure -> pre-execution governance infrastructure
- alpha generation -> outside Nova's category
- trading optimization -> outside Nova's category
- telemetry dashboard tooling -> bounded review-context / chronology surface

## Prohibited Execution-Authority Wording

The following wording is prohibited outside this registry and explicit test fixtures:

- must execute
- binding authorization
- decision approval
- execute if admitted
- execute only if admitted
- Nova grants authority
- retry until ALLOW
- if decision_status == ALLOW
- block execution

## Boundary Language

Boundary language may name execution authority only when it clearly negates that role, for example:

- Nova does not grant execution authority.
- Nova structures governed review context; local authority decides and external systems retain execution responsibility.
- Proof artifacts verify chronology and context integrity; they are not permission grants.

## Governance Rule

Doctrinal changes should be recorded chronologically in semantic migration logs
or governance epoch records. Current public category language must preserve
pre-execution governance framing and avoid converting Nova into execution
software, an approval authority, an interoperability/connective-tissue layer, a
treasury optimizer, or a prediction-centric system.

Historical environmental-governance terminology may remain inside clearly
historical or superseded artifacts. It is not the current external category.
