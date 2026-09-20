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
# Non-Bypass Policy

Nova is a required pre-execution checkpoint.

## Rules

- Nova must be called before any capital-moving action
- decision_status is authoritative
- DENY / DELAY / HALT / VETO cannot be bypassed
- CONSTRAIN must be applied before execution
- No retries to force ALLOW outcomes
- No execution without Nova admission

## Fail-Closed Behavior

If Nova is unavailable:

-> execution must NOT proceed
