# Technical Evidence Map

## Status

Reviewer-facing map of the current public repository.

This document maps public claims to public artifacts. It does not expose private
production machinery or convert repository evidence into production, adoption,
buyer, or authority claims.

## Canonical boundary

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

## Evidence map

| Claim | Public evidence | Evidence class |
|---|---|---|
| Nova is pre-execution decision-context infrastructure | `README.md`, `CATEGORY.md`, `SYSTEM_IDENTITY.md` | Category / doctrine |
| Nova preserves a non-authority boundary | `CATEGORY.md`, `docs/start-here.md`, doctrine lint, public boundary tests | Public doctrine + executable validation |
| Nova defines an external review-context contract | `docs/architecture/external-review-context-contract-v2.md`, `specs/review_context_contract_v2.json` | Public contract |
| Nova defines exact-action review context for a bounded treasury workflow | `docs/go-to-market/first-use-case-agent-prepared-treasury-action.md`, `docs/architecture/agent-prepared-stablecoin-treasury-integration-path.md` | Public workflow specification |
| Nova defines review completeness without creating authority | `docs/governance/review-completeness-standard.md` | Governance standard |
| Nova distinguishes source state from unsupported certainty | `docs/governance/source-state-taxonomy.md` | Governance taxonomy |
| Nova defines field derivation and proof canonicalization for target v2 | `docs/target-v2/gate-3-field-derivation-ledger-v0.1.md`, `docs/target-v2/context-proof-canonicalization-v0.1.md`, `scripts/validate_gate3_field_derivation.py` | Design proof + validator |
| Nova preserves target-v2 non-authority semantics | `docs/target-v2/README.md`, `scripts/validate_target_v2_contract_revision.py`, `tests/test_review_context_contract_v2_spec.py` | Contract validation |
| Nova defines bounded institutional entry requirements without starting a pilot | `docs/target-v2/gate-5-entry-design-review-v0.1.md`, `docs/target-v2/institutional-exposure-contract-v0.1.md`, `scripts/validate_gate5_entry_design_review.py` | Design validation |
| Reflex Memory has a public non-authority specification | `docs/governance/reflex-memory-specification.md`, `docs/architecture/reflex-memory-vs-agent-memory.md` | Public doctrine |
| Reflex Memory has bounded synthetic public material | `fixtures/reflex_memory/`, `schemas/reflex_memory/`, `docs/governance/reflex-memory-v0-1-fixture.md` | Synthetic fixture / schema |
| Nova exposes a bounded retail machine-commerce contract | `CURRENT_STATE.md`, `docs/retail-context-network/`, `docs/retail-agent/external-validation-v0.1.md` | Public contract / bounded evidence |
| Public/private implementation separation is explicit | `docs/governance/public-private-repository-boundary-v0.1.md`, `docs/governance/public-projection-sanitization-execution-v0.1.md` | Repository governance proof |
| Legacy v1 existed as an implemented product generation | `docs/legacy-v1/README.md`, `docs/legacy-v1/reports/PROJECT_REPORT-2026-03-20.md`, Git history | Historical evidence |

## Current public evidence boundary

The current public tree intentionally does **not** contain the canonical production
server, provider configuration, settlement implementation, production control
store, private source registry, institutional accepted-state store, or internal
CCO operating evidence.

Those omissions are architectural, not missing documentation.

```text
public contract and proof
!= production implementation
!= corporate accepted state
!= execution authority
```

## Non-claims

Public repository evidence does not establish institutional adoption, recurring
paid usage, buyer pull, product-market fit, pricing power, institutional pilot
activation, Arc production support, approval, signing, custody, settlement,
execution, or capital authority.
