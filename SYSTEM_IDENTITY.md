# Sharpe Nova OS — System Identity

## Canonical identity

Sharpe Nova OS is a **pre-execution decision discipline layer** that conditions
capital through telemetry, Reflex Memory, and constraint logic before execution.

Externally, Nova is decision-context infrastructure for consequential
machine-prepared capital actions.

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

Local authority is an institution-owned role. Nova does not decide who occupies
that role and does not inherit authority by becoming a required input to the
institution's workflow.

## Repository identity

```yaml
repository:
  public_projection: nova-infrastructure-systems/sharpe-nova-os
  public_role: NON_AUTHORITATIVE_GOVERNED_PROJECTION
  canonical_corporate_accepted_state: nova-infrastructure-systems/nova-core
```

This repository publishes approved doctrine, contracts, schemas, examples, and
externally supportable state. It is not the source of current corporate
accepted-state authority.

## Identity protection layer

The governed public projection of the Nova identity kernel is:

- `docs/governance/nova-identity-kernel-v1.yaml`

Two permanent rules apply:

> **No information transformation may increase the authority of its input unless
> that authority originates from an explicitly authorized external source and
> the transformation preserves that provenance.**

> **Identity must not be inferred where lineage can be explicitly preserved.**

```text
action identity != proposal-version identity
source identity != source-version identity
review-profile identity != review-profile-version identity
context identity != context-state identity
chronology reference != chronology acceptance
```

When lineage is unavailable, preserve `lineage_unavailable` rather than infer
continuity from similarity.

Material changes to these semantics are governed by
`docs/governance/identity-change-protocol-v1.md`. Jarvis-Nova CCO owns
coherence review; the Architect retains final authority.

## Product and access planes

```yaml
system_identity:
  institutional_review_context:
    canonical_direction: target_v2_non_authority_review_context
    target_v2_runtime_implemented: false
    target_v2_production_active: false
    institutional_pilot_started: false

  retail_agent_plane:
    public_machine_commerce_surface: active
    settlement_environment: Base_mainnet
    payment_asset: USDC
    payment_protocol: x402_v2
    authority_effect: none
    approval_effect: none
    execution_effect: none
    access_effect: context_resource_access_only

  Legacy_v1:
    implemented: true
    canonical_future_external_model: false
    retained_for:
      - historical_traceability
      - migration_analysis
      - dependency_inspection
      - test_coverage
```

The retail agent plane and institutional plane are separate. Retail payment
access does not create institutional identity, workflow authorization,
institutional production activation, or capital authority.

## Public resources

The bounded retail machine-commerce surface exposes:

| Resource | Job | Fixed price |
|---|---|---:|
| State Ping | What context exists? | 0.002 USDC |
| Context Delta | What materially changed? | 0.02 USDC |
| Governed Review Context | What review context belongs around this exact proposed action? | 0.10 USDC |
| Decision Context Packet | What portable integrity-bound review artifact should local authority receive? | 1.00 USDC |

A payment for one resource does not authorize another resource.

**NO SECOND PAYMENT without separate explicit capital authorization.**

## What Nova preserves

Nova structures and preserves review context including, where available and
authorized:

- exact prepared-action and proposal-version identity;
- source provenance, authority state, and observation time;
- contradiction, missing-evidence, freshness, and limitation context;
- institution-provided constraint context;
- chronology references;
- governed Reflex Memory references;
- review completeness and unresolved conditions;
- deterministic integrity material;
- explicit authority handoff.

The existence of a record does not create the meaning of that record for the
current action.

```text
source existence != verification
history != accepted chronology
memory != policy
constraint existence != constraint applicability
complete context != approval
integrity != authenticity
payment != authority
review context != execution permission
```

## Negative classification

Sharpe Nova OS is not:

- a trading system;
- a signal engine;
- a prediction layer;
- a portfolio optimizer;
- an execution engine;
- a wallet, custodian, or signing system;
- a generic agent framework;
- a policy engine that owns institutional policy;
- an approval or authorization authority.

## Legacy v1 identity boundary

Legacy v1 contains decision-admission terminology and behavior. Those semantics
remain valid for historical implementation, replay, migration, and dependency
inspection only.

They do not define Nova's canonical future external product identity.

For current state, read [CURRENT_STATE.md](CURRENT_STATE.md).
