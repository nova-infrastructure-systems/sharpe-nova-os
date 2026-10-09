# Sharpe Nova OS — Category Definition

## Category

Sharpe Nova OS is **pre-execution governance infrastructure** for consequential
machine-prepared capital actions.

Its deeper architectural frame is a **pre-execution decision discipline layer**
that conditions capital through telemetry, Reflex Memory, and constraint logic
before execution.

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

`Local authority` is a role in the architecture, not a requirement that a human
must always occupy that role. The institution may place a human, committee,
institution-owned policy process, or separately authorized machine process in
that position.

Nova does not decide who holds that authority and does not inherit it by being
required in the workflow.

## Category boundary

Nova does not own the category of institutional intelligence.

Institutional systems may:

- assemble proprietary financial history;
- reconcile conflicting sources;
- encode accumulated firm judgment;
- make historical knowledge usable by AI;
- model how the institution typically evaluates a situation;
- recommend or inform a present decision.

Those capabilities may be valuable without being Nova.

Nova's narrower object is the governed pre-execution state around an exact
capital action:

- what information was actually available;
- which source state existed at that time;
- which institution-defined constraints were applicable;
- which conditions remained unresolved;
- which prior context was relevant without becoming present authority;
- which exact proposal version was under review;
- what local authority actually received before deciding.

```text
institutional memory
!=
bounded governed review state presented to local authority

historical similarity
!=
precedent

later knowledge
!=
information available at review time
```

## The shift

Capital workflows are becoming increasingly machine-prepared and
machine-mediated.

Agents, institutional-intelligence systems, policy systems, treasury systems,
wallets, custodians, and execution rails can each perform their own job
correctly while the institution still lacks one bounded governed review state
around the exact action before authority decides.

The missing object is not more institutional intelligence or another execution
instruction.

It is the governed relationship among evidence, source state, applicable
constraints, unresolved conditions, relevant prior context, and the exact
proposed action as they existed at the review moment.

## The problem

A transaction record can show what moved.

A policy record can show that a rule exists.

A validation can show that a test passed.

A historical record can show that an exception occurred.

None of those facts alone establishes how they related to the exact action when
local authority reviewed it.

Nova preserves those distinctions.

```text
source existence != verification
history != present authority
constraint existence != constraint applicability
field completeness != review coherence
validation passed != institutional permission
payment != authority
review context != execution permission
```

## The layer

Nova sits between prepared action and local decision authority.

```text
[ Agent / Strategy / Local System ]
                |
                v
      prepared capital action
                |
                v
[ Sharpe Nova OS ]
 governed review context + integrity
                |
                v
[ Local Authority ]
      reviews and decides
                |
                v
[ External Execution Systems ]
```

Nova can become a required input to an institution's authority process without
becoming that authority.

```text
required input to authority
!= authority
```

## Exact-action binding

Review context should remain bound to the exact proposal version that was
reviewed.

A later revision, different destination, changed amount, new counterparty,
different evidence state, or changed institutional requirement can create a
different review context even when many underlying artifacts remain the same.

This preserves reconstructability without implying that Nova decides whether the
action should proceed.

## Identity preservation rule

Identity must not be inferred where lineage can be explicitly preserved.

```text
action identity != proposal-version identity
source identity != source-version identity
review-profile identity != review-profile-version identity
context identity != context-state identity
chronology reference != chronology acceptance
```

When explicit lineage is unavailable, Nova preserves `lineage_unavailable`
rather than inferring continuity from similarity.

State Ping, Context Delta, Governed Review Context, Decision Context Packet,
x402, and the public API are product or access surfaces. Those products do not define the OS.

## What Nova preserves

Depending on the bounded workflow and supplied context, Nova can preserve:

- prepared-action and proposal-version identity;
- source provenance, source state, and observation time;
- contradiction and missing-evidence visibility;
- institution-provided constraint context;
- temporal and chronology context;
- governed Reflex Memory references;
- review completeness and unresolved conditions;
- deterministic integrity material;
- explicit authority handoff.

Reflex Memory is not merely a snapshot of what the world looked like. It
preserves accepted governance memory that may condition future review posture
without creating decision authority.

## What Nova enables

Nova is designed to support:

- reproducible pre-execution review context;
- durable separation between preparation, review, decision, signing, settlement,
  and execution;
- portable context that can survive changes in models, agents, wallets,
  custodians, and execution rails;
- institution-controlled review continuity across replaceable systems;
- machine-consumable context without transferring local authority.

## What Nova is not

Nova is not:

- a trading system;
- a signal engine;
- a prediction layer;
- a portfolio optimizer;
- an execution engine;
- a wallet, custodian, or signing system;
- an institutional approval or authorization authority;
- a policy engine that owns the institution's decision;
- an institutional-intelligence platform;
- a generic institutional-memory layer;
- a system whose moat is simply knowing what happened historically;
- a generic context warehouse or memory product.

## Category test

The category remains coherent only if this boundary survives:

> Nova may structure, preserve, and make review context portable. It does not
> convert evidence into permission, memory into policy, payment into authority,
> or context into execution.

## Final statement

Nova does not determine whether capital should move.

Nova structures governed pre-execution review state around the exact action
before local authority decides.

Authority remains local.

Execution remains external.
