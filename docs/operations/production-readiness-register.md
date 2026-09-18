# Production Readiness Register

## Purpose

This register is the public readiness view for Sharpe Nova OS.

It summarizes what the current public repository can support without exposing
private production machinery or converting bounded evidence into broader claims.
Detailed provider, custody, incident, recovery, and operating evidence remains
in the private `nova-infrastructure-systems/nova-core` operating surface.

For the compressed public system state, read [Current State](../../CURRENT_STATE.md).

## Public claim summary

```yaml
public_claim_summary:
  repository_governance: ready
  public_projection_sanitization: complete

  retail_agent_plane:
    public_machine_commerce_surface: live
    network: Base_mainnet
    payment_asset: USDC
    payment_protocol: x402_v2
    authority_effect: none
    approval_effect: none
    execution_effect: none
    access_effect: context_resource_access_only

  Legacy_v1:
    implemented_historically: true
    canonical_future_external_model: false
    canonical_runtime_in_public_tree: false

  target_v2:
    canonical_contract: design-v2.1
    Gate_3: complete
    Gate_4: complete
    private_synthetic_reference_adapter: implemented
    runtime_implemented: false
    production_active: false

  Gate_5_Entry_Design_Review:
    status: COMPLETE
    canonicality_source: authoritative_repository_main

  Gate_5_authorization_preconditions:
    status: NOT_YET_SATISFIED
    preconditions_not_yet_evidenced: 18

  Gate_5:
    status: NOT_STARTED
    authority: false
    institutional_pilot:
      authorized: false
      started: false

  institutional_pilot: not_started
  production_custody_attestation: not_complete
  system_wide_production_readiness: not_established
```

`repository_governance: ready` means the public repository has a bounded role,
current validation, and a verified public/private authority separation. It does
not mean Sharpe Nova OS is system-wide production-ready or institutionally
ready.

## Canonical boundary

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

Sharpe Nova OS is pre-execution decision-context infrastructure. It does not
approve, authorize, sign, settle, execute, custody capital, or replace local
authority.

## Repository readiness

The public repository is now a deliberately bounded external surface:

```text
Public
= category + doctrine + contracts + schemas + synthetic proof + verification

Private
= production machinery + proprietary derivation + corporate state + operating evidence
```

The authorized September 18, 2026 sanitization removed private-target runtime,
internal operating material, superseded public clutter, and the retired NSF
program package from the current public tree while preserving Git history.

Repository sanitization does not imply that historically published material has
become confidential, and it does not create standing deletion or production
authority.

## Retail agent plane

The public projection records a bounded retail machine-commerce surface on Base
mainnet using USDC and x402 v2.

The four public resources are:

| Resource | Fixed price | Access job |
|---|---:|---|
| State Ping | 0.002 USDC | What context exists? |
| Context Delta | 0.02 USDC | What materially changed? |
| Governed Review Context | 0.10 USDC | What review context belongs around this exact proposed action? |
| Decision Context Packet | 1.00 USDC | What portable integrity-bound review artifact should local authority receive? |

Payment buys bounded context access only.

```yaml
authority_effect: none
approval_effect: none
execution_effect: none
access_effect: context_resource_access_only
```

A paid resource does not establish institutional identity, workflow authority,
institutional production activation, adoption, buyer demand, or product-market
fit.

## Institutional target-v2 plane

The canonical institutional direction remains the non-authority target-v2 review
context contract.

```yaml
institutional_target_v2:
  canonical_contract: design-v2.1
  Gate_3_field_derivation_design: complete
  Gate_4_private_synthetic_adapter: complete
  Gate_5_Entry_Design_Review: COMPLETE
  Gate_5_authorization_preconditions: NOT_YET_SATISFIED
  Gate_5_bounded_institutional_pilot: NOT_STARTED
  runtime_implemented: false
  production_active: false
  implementation_authority: false
  production_activation_authority: false
```

The private synthetic adapter and completed design gates are evidence about
contract coherence. They are not evidence that an institutional runtime or
pilot exists.

## Production custody and operating evidence

The public repository is not the canonical production implementation or the
canonical corporate accepted-state store.

Detailed provider-control, credential, recovery, deployment, incident, and
production-custody evidence is intentionally private. The public projection may
state bounded reviewed outcomes, but it does not expose those operating records
as a substitute for independent production attestation.

Accordingly:

```yaml
production_evidence_boundary:
  canonical_production_implementation_repository: nova-infrastructure-systems/nova-core
  public_repository_is_production_source: false
  public_repository_is_corporate_accepted_state: false
  production_custody_attestation: not_complete
  system_wide_production_readiness: not_established
```

## Evidence distinctions

Keep these states separate:

```text
repository merged != production deployed
service available != institutional production activation
payment received != authority granted
validation passed != institutional permission
historical implementation != current public runtime
operator observation != independent provider attestation
complete context != approval
```

The public repository does not independently establish:

- institutional production activation;
- a live institutional pilot;
- independent provider-side production custody attestation;
- buyer pull or recurring institutional use;
- operator dependency;
- adoption or product-market fit;
- pricing power;
- marketplace listing or discovery unless separately verified;
- live Arc production support;
- live Circle Gateway verification or settlement through Nova;
- approval, signing, custody, settlement, execution, or capital authority.

## Product progression

```yaml
product_progression:
  Gate_1_production_custody:
    status: CONDITIONAL_PASS
    public_interpretation: historical_readiness_gate_outcome_not_full_current_attestation

  Gate_2_Legacy_v1_dependency:
    status: CONDITIONAL_PASS
    public_interpretation: historical_dependency_review_with_known_evidence_limits

  Gate_3_v2_field_derivation_design:
    status: COMPLETE
    implementation_authority: false
    production_activation_authority: false

  Gate_4_private_synthetic_adapter:
    status: COMPLETE
    scope: private_synthetic_reference_only
    runtime_effect: none
    public_endpoint_effect: none
    production_effect: none

  Gate_5_Entry_Design_Review:
    status: COMPLETE
    canonicality_source: authoritative_repository_main

  Gate_5_authorization_preconditions:
    status: NOT_YET_SATISFIED
    preconditions_not_yet_evidenced: 18
    silently_resolved: false

  Gate_5:
    status: NOT_STARTED
    authority: false
    institutional_pilot:
      authorized: false
      started: false

  Gate_6_institutional_monetization:
    status: NOT_STARTED_FOR_PILOT

  Gate_7_machine_discovery:
    status: BLOCKED_FOR_INSTITUTIONAL_TARGET_V2
```

No later gate is authorized merely because an earlier design gate is complete.

## Monetization boundary

The retail public resource ladder may charge for context access. Institutional
commercialization remains a separate future state.

Payment may buy access, coverage, retention, evidence packaging,
reproducibility, or service levels. Payment must not buy approval, authorization,
permission, execution, or a favorable outcome.

The permanent capital boundary remains:

> **NO SECOND PAYMENT without separate explicit capital authorization.**

## Update rule

Update this public register only when a verified repository or approved public
state change affects the bounded claims above.

Do not place provider secrets, detailed production topology, internal CCO state,
private accepted-state records, or operating evidence into this public register
merely to make it appear more complete.
