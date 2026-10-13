# Non-Bypass Policy

## Current status

**Historical Legacy v1 control-policy artifact — not current canonical authority semantics.**

This document is retained for provenance, replay, migration, negative testing, and
historical dependency inspection. It must not be used as current product identity,
external contract authority, or a claim that Nova itself approves, denies, blocks,
or authorizes capital movement.

Current canonical boundary:

```text
Agent prepares action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

`authority_effect = none`

## Historical Legacy v1 rules

The following rules describe the historical decision-admission model only:

- Nova must be called before any capital-moving action
- `decision_status` is authoritative
- DENY / DELAY / HALT / VETO cannot be bypassed
- CONSTRAIN must be applied before execution
- No retries to force ALLOW outcomes
- No execution without Nova admission

## Historical fail-closed behavior

The Legacy v1 policy stated:

```text
If Nova is unavailable:
execution must NOT proceed
```

That behavior is historical implementation context. It is not the current canonical
statement of Nova's authority role.
