# Identity Change Protocol v1

**Status:** active governed projection  
**Control owner:** Jarvis-Nova CCO  
**Final authority:** Architect

Treat a proposed change as `IDENTITY_CHANGE` when it materially changes Nova's
category, canonical boundary, authority model, action/proposal identity
semantics, review-completeness meaning, chronology or Reflex Memory semantics,
payment/authority semantics, execution boundary, canonical identity kernel, or
the relationship between product surfaces and the OS.

Before merge, an `IDENTITY_CHANGE` requires:

```yaml
identity_change_review:
  CCO_review: required
  architecture_impact_analysis: required
  GTM_impact_analysis: required
  monetization_impact_analysis: required
  migration_analysis: required
  backward_semantic_compatibility_review: required
  explicit_Architect_approval: required
```

A reconciliation that only restores stale artifacts to the already-authorized
identity may be classified `IDENTITY_PRESERVATION`.

If review reveals a substantive authority-model change rather than preservation,
stop before merge and escalate to the Architect.

This protocol creates no production, deployment, payment, settlement, capital,
chronology, Reflex Memory, credential, legal, or accepted-state authority.
