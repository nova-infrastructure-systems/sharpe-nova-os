# Reviewer Paths

## Purpose

This repository is a governed public proof and integration surface for Sharpe Nova OS.
It is not the full operating archive or the canonical production implementation.

## Canonical boundary

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

## Ten-minute path

1. [README](../README.md)
2. [Current State](../CURRENT_STATE.md)
3. [Category Definition](../CATEGORY.md)
4. [First bounded treasury workflow](go-to-market/first-use-case-agent-prepared-treasury-action.md)
5. [Target v2](target-v2/README.md)
6. [Production Readiness](operations/production-readiness-register.md)

This path should answer what Nova is, where it sits, what exists publicly today,
and what remains outside Nova's authority.

## Treasury workflow path

1. [Where Nova Sits](go-to-market/where-nova-sits.md)
2. [First Use Case](go-to-market/first-use-case-agent-prepared-treasury-action.md)
3. [Stablecoin Treasury Integration Path](architecture/agent-prepared-stablecoin-treasury-integration-path.md)
4. [Pre-Action Context Contract](architecture/pre-action-context-contract.md)
5. [Review Completeness Standard](governance/review-completeness-standard.md)
6. [Synthetic Stablecoin Treasury Example](../examples/pre_action_context/agent_prepared_stablecoin_treasury_action.yaml)

## Contract and developer path

1. [External Review-Context Contract v2](architecture/external-review-context-contract-v2.md)
2. [Target v2](target-v2/README.md)
3. [Review Context Schema](../specs/review_context_contract_v2.json)
4. [Schemas](../schemas/)
5. [Synthetic fixtures](../fixtures/target-v2/)
6. [Pre-Action Context Examples](../examples/pre_action_context/)
7. [Public Surface Validator](../scripts/validate_public_surface_coherence.py)
8. [Target v2 Validator](../scripts/validate_target_v2_contract_revision.py)
9. [Gate 3 Field-Derivation Validator](../scripts/validate_gate3_field_derivation.py)
10. [Gate 5 Entry-Design Validator](../scripts/validate_gate5_entry_design_review.py)

The public developer surface is intentionally contract-first. Production runtime,
provider topology, settlement internals, accepted-state machinery, and proprietary
derivation remain private.

## Governance path

1. [Public / Private Repository Boundary](governance/public-private-repository-boundary-v0.1.md)
2. [Source-State Taxonomy](governance/source-state-taxonomy.md)
3. [Review Completeness Standard](governance/review-completeness-standard.md)
4. [Institution-Owned Governance Chronology](governance/institution-owned-governance-chronology.md)
5. [Reflex Memory Specification](governance/reflex-memory-specification.md)
6. [Chronology Preservation Standard](governance/chronology-preservation-standard.md)

## Reflex Memory path

1. [Reflex Memory Specification](governance/reflex-memory-specification.md)
2. [Reflex Memory vs Agent Memory](architecture/reflex-memory-vs-agent-memory.md)
3. [Reflex Memory API Context](architecture/reflex-memory-api-context.md)
4. [Temporal State Standard](governance/reflex-memory-temporal-state-standard.md)
5. [Bounded Fixture Description](governance/reflex-memory-v0-1-fixture.md)
6. [Synthetic Fixtures](../fixtures/reflex_memory/)
7. [Public Schemas](../schemas/reflex_memory/)

Reflex Memory is accepted governance memory that may condition future review posture.
It is not policy, approval, authorization, execution, or autonomous learning.

## Historical Legacy v1 path

1. [Legacy v1](legacy-v1/README.md)
2. [Historical March 2026 Project Report](legacy-v1/reports/PROJECT_REPORT-2026-03-20.md)
3. [Migration and Isolation Plan](migrations/v1-admission-isolation-plan.md)

Legacy v1 implementation history remains available in Git history. The current
public tree does not carry the canonical production runtime.

## Verification

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt -c constraints.txt
make verify
```

## Final rule

Read public evidence at the scope it proves.

```text
public artifact != corporate accepted state
passing validator != production authority
historical implementation != current public runtime
payment != authority
review context != execution permission
```
