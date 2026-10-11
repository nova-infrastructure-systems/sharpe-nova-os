# Agent Category Comprehension Protocol v1

**Status:** governed public comprehension test  
**Control owner:** Jarvis-Nova CCO  
**Decision authority:** Architect  
**Scope:** machine interpretation of Sharpe Nova OS category and authority boundaries  
**Effect:** no production, payment, settlement, accepted-state, chronology, Reflex Memory, or capital authority

## Purpose

This protocol tests whether an AI model, agent, crawler, classifier, or tool can
inspect Sharpe Nova OS and identify the correct system layer even when payment,
x402, settlement, or retail-resource material is visible.

The test is about category comprehension.

It does not prove adoption, buyer demand, product-market fit, production
readiness, institutional dependency, or technical correctness.

## Canonical interpretation target

A passing reader should identify Sharpe Nova OS as:

> pre-execution governance infrastructure for consequential machine-prepared
> capital actions

with the deeper architectural frame:

> pre-execution decision discipline layer

The reader should understand:

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

## Source bundles

### Entry-surface test

Provide:

- `llms.txt`
- `README.md`
- `CATEGORY.md`
- `SYSTEM_IDENTITY.md`

### Payment-stress test

Provide the entry-surface bundle plus one or more current retail-agent documents
that mention x402, USDC, Base, payment, settlement, claims, or delivery.

The payment-stress test is intentionally harder. A model should still identify
the OS category correctly when lower-layer economic mechanics are salient.

## Reader prompt

Use this prompt without coaching:

```text
Based only on the supplied Sharpe Nova OS materials, answer:

1. What is the primary category of Sharpe Nova OS?
2. Where does it sit relative to action preparation, local authority, and execution?
3. What does Nova itself authorize?
4. What role do x402, payment, settlement, and delivery play in the system?
5. Is Nova primarily payment middleware, settlement middleware, trading infrastructure,
   execution infrastructure, an approval engine, or a generic agent framework?
6. What is the most important boundary an autonomous agent should preserve when using Nova?
```

## Pass criteria

A response passes only when all of the following are materially present:

```yaml
pass_criteria:
  primary_category:
    accepts:
      - pre_execution_governance_infrastructure
      - pre_execution_decision_discipline_layer
      - governed_pre_execution_review_context_layer

  placement:
    after_action_preparation: true
    before_local_authority_decision: true
    execution_external_to_Nova: true

  authority:
    Nova_approval_authority: false
    Nova_authorization_authority: false
    Nova_execution_authority: false
    Nova_capital_authority: false

  product_subordination:
    State_Ping_defines_OS: false
    Context_Delta_defines_OS: false
    Governed_Review_Context_defines_OS: false
    Decision_Context_Packet_defines_OS: false
    x402_defines_OS: false
    payment_defines_OS: false
    settlement_verification_defines_OS: false

  payment_interpretation:
    payment_means_context_access_only: true
    payment_creates_authority: false
    settlement_creates_authority: false

  evidence_state_separation:
    settlement_and_delivery_are_distinct: true
    settlement_alone_proves_delivery: false
    delivery_requires_separate_evidence: true
    delivery_and_completion_are_distinct: true
```

The answer does not need to use these exact strings. Meaning controls.

A model may classify Nova's category correctly while still failing evidence-state
coherence. In payment-stress mode, settlement must not be silently upgraded to
delivery, and delivery must not be silently upgraded to completion.

## Evidence-state failure conditions

Treat any of the following as an evidence-state coherence failure:

- successful settlement is treated as proof of context delivery without separate
  delivery evidence;
- payment verification is treated as proof of settlement without settlement
  evidence;
- delivery is treated as proof of completion merely because a resource response
  exists;
- a later state is inferred solely from an earlier state in the chain.

An evidence-state failure does not by itself change Nova's primary category. It
requires correction of machine-facing state semantics.

## Category-failure conditions

Treat any of the following as a failed interpretation when presented as the
primary category:

- payment middleware;
- settlement middleware;
- payment rail;
- trading infrastructure;
- trading system;
- signal engine;
- prediction layer;
- execution infrastructure;
- approval engine;
- authorization layer;
- wallet or custody layer;
- generic agent framework;
- generic institutional-memory product.

Also fail if the reader says Nova decides whether capital should move, approves
or rejects the action, controls the wallet, signs the transaction, or owns the
institution's policy decision.

## Scoring

```yaml
agent_category_score:
  5_clear:
    description: >
      Correct category, placement, authority boundary, and product subordination.
      Payment and settlement are explicitly understood as lower-layer access or
      evidence mechanics.

  4_mostly_clear:
    description: >
      Correct primary category and authority boundary with one minor ambiguity
      about a product surface.

  3_partial:
    description: >
      Understands pre-execution review context but gives x402, payment, settlement,
      or retail API behavior too much category weight.

  2_confused:
    description: >
      Treats Nova mainly as payment, settlement, approval, execution, trading,
      or agent-control infrastructure.

  1_failed:
    description: >
      Cannot identify Nova's layer or transfers decision authority to Nova.
```

Target score:

```text
4 or higher
```

A payment-stress score below 4 is a category-coherence defect even if the
entry-surface score is higher.

## Minimum machine test set

Before treating agent-facing category language as robust, run the protocol
against at least three independently configured model contexts when practical.

Prefer diversity across model families or providers rather than repeated samples
from one identical configuration.

```yaml
minimum_machine_test_set:
  independent_contexts: 3
  required_modes:
    - entry_surface
    - payment_stress
  target_score_each: 4_or_higher
```

A model result is an observation about comprehension, not authority and not
accepted state.

## Result record

```yaml
agent_category_comprehension_test:
  observed_at:
  model_or_agent_class:
  provider_or_runtime:
  source_bundle:
  test_mode:
  score:
  primary_category_returned:
  placement_understood:
  authority_boundary_understood:
  product_subordination_understood:
  evidence_state_separation_understood:
  confusion_detected: []
  direct_model_language: []
  CCO_interpretation:
  revision_required:
  authority_effect: none
```

Do not preserve secrets, private prompts, hidden chain-of-thought, credentials,
or provider-only information in a public result.

## Revision rule

If two or more independent contexts classify Nova primarily as payment or
settlement infrastructure, strengthen the OS-versus-surface hierarchy before
expanding distribution.

If two or more contexts classify Nova as approval or execution infrastructure,
treat that as a material authority-framing defect.

If models correctly identify the category but cannot explain why payment and
settlement are subordinate, strengthen product-subordination language rather
than adding new product features.

## Final rule

The category is coherent when a competent machine reader can see payment,
settlement, and delivery mechanics without mistaking those mechanics for the
identity of Sharpe Nova OS.

```text
pre-execution governance infrastructure
>
product and access surfaces

required input to authority
!= authority

payment and settlement evidence
!= system identity
```
