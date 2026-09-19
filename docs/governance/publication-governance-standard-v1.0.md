# Publication Governance Standard v1.0

**Status:** active public projection of Architect-approved governance control
**Control owner:** Jarvis-Nova CCO
**Decision authority:** Architect
**Repository role:** `NON_AUTHORITATIVE_GOVERNED_PROJECTION`

## Permanent publication rule

Publication is not the default merely because an artifact is safe enough to expose.

A public artifact must satisfy both tests:

```yaml
publication_gate:
  affirmative_external_value:
    require_at_least_one:
      - category_comprehension
      - interoperability
      - verification
      - external_trust

  private_risk:
    require_none_material:
      - proprietary_derivation
      - production_topology
      - operating_evidence
      - corporate_accepted_state
      - institutional_private_state
      - security_sensitive_implementation
      - provider_only_secret

  default_when_uncertain: PRIVATE
```

The absence of an obvious secret is not sufficient reason to publish.

Where a public contract, schema, synthetic proof, or sanitized explanation is
sufficient, do not publish the private implementation or operating evidence.

## Canonical boundary

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

Publication must never create a stronger authority implication than the
underlying system state supports.

## Repository roles

```text
Public
= category + doctrine + external contracts + schemas + synthetic proof
  + approved public evidence + verification

Private
= production machinery + proprietary derivation + corporate accepted state
  + operating evidence + internal CCO/GTM state

Provider-only
= secrets + live environment values + credential material
```

## Exposure classification

Every new or materially revised public artifact must be classified before merge:

- `PUBLIC`
- `PUBLIC_SANITIZED`
- `PRIVATE`
- `PROVIDER_ONLY`

`PRIVATE` and `PROVIDER_ONLY` material must not be added to the current public
repository tree.

## CCO standing responsibilities

Jarvis-Nova CCO owns coherence control across public exposure and claim scope.
The CCO is responsible for:

1. category integrity;
2. authority-boundary integrity;
3. public/private exposure classification;
4. claim-evidence discipline;
5. current-state freshness;
6. cross-surface product, GTM, pricing, monetization, and documentation coherence;
7. retail-agent and institutional plane separation;
8. coherence review for material public entry-surface, authority, production,
   payment/pricing, API/schema, memory/chronology, commercialization, and
   exposure changes;
9. drift escalation when a pattern becomes structurally relevant;
10. quiet-watch discipline for weak signals that are not accepted state.

## CCO non-authorities

The CCO does not independently own or create:

- corporate accepted-state mutation;
- chronology acceptance;
- Reflex Memory mutation;
- production deployment authority;
- secret or credential custody;
- payment or settlement authority;
- capital authority;
- legal or compliance determinations;
- institutional policy;
- final Architect authority.

The CCO may classify a change as `review_required` or recommend that a merge be
held for coherence reasons. The Architect retains final authority.

## CCO review triggers

CCO review is required before merge when a change materially affects:

- `README.md`, `CURRENT_STATE.md`, `CATEGORY.md`, or `SYSTEM_IDENTITY.md`;
- authority, approval, execution, production, or readiness semantics;
- pricing, payment, x402, marketplace, or commercialization semantics;
- institutional identity, tenancy, or plane separation;
- chronology or Reflex Memory framing;
- public API/resource contracts, schemas, proof semantics, or discovery metadata;
- adoption, buyer, pricing-power, or product-market-fit claims;
- public/private exposure classification;
- provider topology, recovery mechanics, operational controls, or secret boundaries.

Formatting-only or mechanically generated changes may be marked
`CCO_REVIEW_NOT_REQUIRED` only when meaning, exposure, and current-state
interpretation cannot change.

## Claim-state discipline

Public review must preserve these distinctions:

```text
observed != inferred != recommended != authorized != implemented != completed
validated != applicable != approved != authorized
source existence != verification
history != present authority
constraint existence != applicability
payment != authority
review context != execution permission
repository merged != production deployed
service available != institutional production activation
market signal != buyer demand
```

## Publication decision record

For each material public change, preserve at least:

```yaml
publication_decision:
  exposure_class:
  external_value:
  private_risk_reviewed:
  CCO_review:
  evidence_scope:
  current_state_effect:
  production_effect:
  accepted_state_effect:
```

The pull request may serve as this record when the change has no independent
chronology or accepted-state effect.

## Final rule

> Publish only when the external value is affirmative and the private risk is
> acceptably bounded. When uncertain, keep the machinery private and publish the
> minimum contract or proof required.

This standard creates no production, payment, settlement, capital, chronology,
Reflex Memory, legal, or accepted-state authority.
