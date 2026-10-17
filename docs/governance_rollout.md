# Governance Rollout
## Current status

**Historical Legacy v1 governance-rollout reference — not current Nova authority semantics or integration guidance.**

The statements below about an authoritative API, binding refusal states, and `decision_status` describe legacy decision-admission behavior only. They do not authorize a current Nova approval, denial, execution gate, or implementation. The approved boundary is: Agent prepares action. Nova structures review context. Local authority decides. External systems execute. Nova does not execute. `authority_effect = none`. For current identity and state, see the repository root `SYSTEM_IDENTITY.md` and `CURRENT_STATE.md`.


Sharpe Nova OS exposes governance as part of the control-plane interface.

## Rollout Logic

Governance layers may be activated in phases, but the interpretation boundary remains stable:

- Nova is still a pre-execution 
- the API remains authoritative
- refusal states remain binding

## Active-Layer Discipline

Governance profiles can expose layers such as:

- temporal governance
- loop integrity
- telemetry integrity
- system state
- permission budgeting
- halt release governance

These layers should be understood as control surfaces, not as trading features.

## Operational Reading

Use governance rollout to understand which control surfaces are active for a key or environment, not to infer a broader system identity.

Governance still resolves into the same authoritative interaction:

- submit the decision to `/v1/context`
- bind behavior to `decision_status`
- retrieve `/v1/proof/{decision_id}` for the auditable outcome
