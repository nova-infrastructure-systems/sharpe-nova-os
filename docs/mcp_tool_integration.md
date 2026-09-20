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
# MCP Tool Integration

Nova may be exposed as external tools, but tool wrapping does not weaken Nova authority.

## Tools

- `nova_context` -> call `/v1/context` to retrieve the governed decision
- `nova_proof` -> call `/v1/proof/{decision_id}` to verify the governed decision

## Rule

All capital-moving actions must call `nova_context` before execution.

MCP clients must bind behavior to `decision_status`, not to agent reasoning or supporting fields.
