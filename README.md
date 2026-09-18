# Sharpe Nova OS

**Pre-execution decision-context infrastructure for consequential machine-prepared capital actions.**

Sharpe Nova OS structures governed review context before local authority decides.

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

> **Repository role:** this public repository is the governed external projection of
> Sharpe Nova OS. Canonical corporate accepted state and private production
> implementation live in the private `nova-infrastructure-systems/nova-core`
> repository. Public retained accepted-state artifacts are historical projection
> only.

## Why Nova exists

Financial systems can preserve documents, transactions, policies, model outputs,
and signatures while still losing the relationships that made those objects
relevant to the exact action under review.

For a consequential action, local authority may need to reconstruct:

- which proposal version was reviewed;
- which source supported each material claim;
- which source state was current at review time;
- which institution-defined constraints belonged to the exact action;
- what changed materially;
- what remained unresolved;
- which prior context was relevant without becoming present authority;
- what review context was actually presented before the institution decided.

Nova exists to preserve and structure that review state before execution.

## First bounded workflow

The first bounded workflow is an **agent-prepared stablecoin treasury action**.

An agent may prepare a proposal and later revise its amount, destination, timing,
counterparty, assumptions, or supporting evidence. Nova structures review
context around the exact proposal version so the institution does not have to
reconstruct the decision basis after the fact.

Nova does not decide whether capital should move.

## What Nova is

Nova is a **pre-execution decision discipline layer** that conditions capital
through telemetry, Reflex Memory, and constraint logic before execution.

Externally, that means Nova structures review context around machine-prepared
capital actions while preserving the institution's authority boundary.

Nova is designed to preserve distinctions such as:

```text
source existence != verification
history != present authority
constraint existence != constraint applicability
field completeness != review coherence
validation passed != institutional permission
payment != authority
review context != execution permission
```

## What Nova is not

Nova is not:

- a trading system;
- a signal engine;
- a prediction layer;
- a portfolio optimizer;
- an execution engine;
- a wallet or custodian;
- an institutional approval or authorization authority;
- a system that turns a payment, model output, validation result, or prior event
  into permission.

## Current state

The current public projection distinguishes two planes that must not be
collapsed.

### Retail agent plane

A separately bounded public machine-commerce surface is active for agents that
need progressively deeper decision context. Payment meters access to context
only. It does not create approval, authority, execution permission, or a
favorable answer.

### Institutional plane

The canonical target-v2 non-authority review-context contract remains the
institutional direction. The private synthetic target-v2 reference adapter is implemented.
The target v2 runtime is not implemented and target v2 is not production-active.
No institutional pilot, operator dependency, buyer validation, adoption, or
product-market fit is established by this repository.

For the current public projection, read [Current State](CURRENT_STATE.md).

## Public machine-commerce surface

The retail agent plane exposes four distinct paid context resources on Base
mainnet using USDC and x402 v2:

| Stage | Resource | Job | Fixed price |
|---|---|---|---:|
| 1 | State Ping | What context exists? | 0.002 USDC |
| 2 | Context Delta | What materially changed? | 0.02 USDC |
| 3 | Governed Review Context | What review context belongs around this exact proposed action? | 0.10 USDC |
| 4 | Decision Context Packet | What portable integrity-bound review artifact should local authority receive? | 1.00 USDC |

Each resource preserves:

```yaml
authority_effect: none
approval_effect: none
execution_effect: none
access_effect: context_resource_access_only
```

A payment for one resource does not authorize a later resource. No response
automatically purchases a deeper context stage.

The permanent capital boundary remains:

> **NO SECOND PAYMENT without separate explicit capital authorization.**

The public machine-readable service exposes discovery and API surfaces for these
resources. Public service availability does not establish institutional
production activation, institutional identity, workflow authorization, or
capital authority.

## What can be inspected here

This repository is intentionally public where publication strengthens category
comprehension, interoperability, verification, or trust.

Start with:

1. [Current State](CURRENT_STATE.md)
2. [Start Here](docs/start-here.md)
3. [Category Definition](CATEGORY.md)
4. [System Identity](SYSTEM_IDENTITY.md)
5. [First bounded workflow](docs/go-to-market/first-use-case-agent-prepared-treasury-action.md)
6. [Target v2](docs/target-v2/README.md)
7. [Production Readiness Register](docs/operations/production-readiness-register.md)

For historical product-generation and migration inspection:

- [Legacy v1](docs/legacy-v1/README.md)

The public repository no longer carries the canonical Legacy v1 runtime implementation.
Historical implementation provenance remains in Git history; current production machinery is private.

## Public / private boundary

The repository boundary is deliberate:

```text
Public
= contract, doctrine, interoperability, approved proof

Private
= production machinery, proprietary derivation, corporate state, operating evidence

Provider-only
= secret values and live environment credentials
```

The public repository is not the canonical corporate accepted-state store and
does not expose private operating evidence merely to increase transparency.

## Architecture and governance

Key public references include:

- [External review-context contract v2](docs/architecture/external-review-context-contract-v2.md)
- [Pre-action context contract](docs/architecture/pre-action-context-contract.md)
- [Governed context flow](docs/architecture/governed-context-flow.md)
- [Review-context state and portability](docs/architecture/review-context-state-and-portability-specification.md)
- [Review completeness standard](docs/governance/review-completeness-standard.md)
- [Source-state taxonomy](docs/governance/source-state-taxonomy.md)
- [Institution-owned governance chronology](docs/governance/institution-owned-governance-chronology.md)
- [Reflex Memory specification](docs/governance/reflex-memory-specification.md)
- [Public/private repository boundary](docs/governance/public-private-repository-boundary-v0.1.md)

## Evidence boundaries

Passing tests, repository artifacts, public service availability, and paid
resource access must not be collapsed into stronger claims.

This repository does not establish:

- institutional production activation;
- a live institutional pilot;
- buyer pull or recurring institutional use;
- operator dependency;
- adoption or product-market fit;
- pricing power;
- marketplace listing or discovery unless separately verified;
- approval, signing, custody, settlement, execution, or capital authority.

## Verification

Create the local development environment and run the public repository
verification chain:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
make verify
```

The verification chain includes doctrine, scenarios, tests, chronology,
whitespace, and public-surface coherence checks.

## License and security

- [Security](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
- [License](LICENSE)

Sharpe Nova OS is developed by Nova Infrastructure Systems Corporation.
