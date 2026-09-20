# Nova Identity Protection Layer v1

**Status:** active governed public projection  
**Control owner:** Jarvis-Nova CCO  
**Decision authority:** Architect  
**Canonical authority source:** `nova-infrastructure-systems/nova-core`  
**Machine projection:** `docs/governance/nova-identity-kernel-v1.yaml`

## Purpose

Protect Sharpe Nova OS from semantic drift while keeping the public repository a
bounded external contract and proof surface.

## Canonical identity

Sharpe Nova OS is a pre-execution decision discipline layer that conditions
capital through telemetry, Reflex Memory, and constraint logic before execution.

Externally, Nova is pre-execution decision-context infrastructure for
consequential machine-prepared capital actions.

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

## Non-Escalation of Authority Principle

No information transformation may increase the authority of its input unless
that authority originates from an explicitly authorized external source and the
transformation preserves that provenance.

```text
observation != permission
history != present authority
memory != policy
review completeness != approval
validation != permission
payment != authority
model inference != institutional fact
integrity != authenticity
```

## Identity preservation

Identity must not be inferred where lineage can be explicitly preserved.

```text
action identity != proposal-version identity
source identity != source-version identity
review-profile identity != review-profile-version identity
context identity != context-state identity
chronology reference != chronology acceptance
```

When lineage is unavailable, preserve `lineage_unavailable` rather than infer
continuity from similarity.

## Product separation

State Ping, Context Delta, Governed Review Context, Decision Context Packet,
x402, and the public API are expressions of Sharpe Nova OS. They do not define
the identity of the OS.

## Negative capabilities

Nova must not, by default, decide or recommend the prepared action, infer stable
action lineage from proposal similarity, convert completeness into permission,
convert payment into authority, turn prior decisions into present policy, treat
Reflex Memory as autonomous policy, or let an execution system inherit authority
from a context packet.

## Change control

Material changes to category, authority model, identity semantics, chronology or
Reflex Memory meaning, payment/authority semantics, or the canonical kernel are
governed by `docs/governance/identity-change-protocol-v1.md`.

The public repository cannot create corporate accepted state.

This control creates no production, deployment, payment, settlement, chronology,
Reflex Memory, credential, accepted-state, or capital authority.
