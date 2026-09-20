> **Legacy v1 compatibility artifact**
>
> This document describes Legacy v1 decision-admission behavior and authority-bearing
> compatibility semantics. It is retained for implementation, replay, migration,
> and historical traceability only.
>
> It does **not** define Sharpe Nova OS's canonical current identity or target-v2
> external semantics. New integrations must not treat `decision_status`, admission
> outcomes, or non-bypass language here as Nova's current authority model.
>
> Current identity authority: `SYSTEM_IDENTITY.md` and the Nova Identity Protection
> Layer v1.
>
# Field Hierarchy

## Primary Decision Authority

- decision_status

## Proof Verification Fields

- constraint_effect
- intervention_type
- failure_class

These fields verify and explain the governed state. They do not override `decision_status`.

## Supporting Fields

- impact_on_outcomes
- adjustment
- internal constraint details

Integrations must bind execution behavior to `decision_status`.

Supporting fields may inform adjustment but must not define admission.

## Interpretation Rule

```json
{ "decision_status": "DENY" }
```

means:

> **This decision is not admissible. Execution must not proceed.**

It is not a signal to reinterpret.
