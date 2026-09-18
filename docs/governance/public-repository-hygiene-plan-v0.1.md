# Public Repository Hygiene Plan v0.1

**Status:** bounded Pass 2 classification; no deletion authority  
**Repository:** `nova-infrastructure-systems/sharpe-nova-os`  
**Baseline:** public `main` after PR #66  
**Purpose:** reduce public-surface noise without erasing provenance or weakening the public/private boundary

## Governing principle

```text
Public = contract, doctrine, interoperability, approved proof.
Private = production machinery, proprietary derivation, corporate state, operating evidence.
Provider-only = secrets and live environment values.
```

The public repository should look like an intentional external trust and
integration surface. Historical engineering residue may remain in Git history
without remaining prominent in the current tree.

This plan is classification only. It does not authorize moving or deleting a
current public path.

## Root disposition

### Retain at repository root

These paths belong on the primary public surface because they explain Nova,
govern external use, or support normal repository operation.

| Path | Disposition | Reason |
|---|---|---|
| `README.md` | RETAIN_ROOT | primary external entry surface |
| `CURRENT_STATE.md` | RETAIN_ROOT | governed public current-state projection |
| `CATEGORY.md` | RETAIN_ROOT | category and authority boundary |
| `SYSTEM_IDENTITY.md` | RETAIN_ROOT | system identity and plane separation |
| `CHANGELOG.md` | RETAIN_ROOT | external change history |
| `CONTRIBUTING.md` | RETAIN_ROOT | contributor contract |
| `SECURITY.md` | RETAIN_ROOT | public security surface |
| `LICENSE` | RETAIN_ROOT_PENDING_LEGAL_REVIEW | current public license; separate legal decision |
| `Makefile` | RETAIN_ROOT | public verification entrypoint |
| `.gitignore` | RETAIN_ROOT | repository operation |
| `.python-version` | RETAIN_ROOT | reproducible developer environment |
| `requirements.txt` | RETAIN_ROOT | public repository dependencies |
| `requirements-dev.txt` | RETAIN_ROOT | public verification dependencies |
| `pytest.ini` | RETAIN_ROOT | public verification configuration |
| `.github/` | RETAIN_ROOT | public repository automation/governance |

### Historical or superseded root surfaces

These paths are useful as provenance but should not remain part of the eventual
top-level comprehension surface.

| Path | Target disposition | Rationale |
|---|---|---|
| `START_HERE.md` | ARCHIVE_OR_REMOVE_CURRENT_TREE | legacy redirect; README and `docs/start-here.md` now own entry |
| `PROJECT_REPORT.md` | ARCHIVE_OR_REMOVE_CURRENT_TREE | compatibility pointer to historical Legacy v1 report |
| `ROADMAP.md` | MOVE_TO_DOCS_OR_ARCHIVE | broad historical roadmap predates current private/public operating model |
| `CONSTRAINT_POLICY.md` | ARCHIVE_LEGACY | Legacy v1 admission/authority semantics |
| `NOVA_EVIDENCE_PACK_V1.md` | ARCHIVE_LEGACY | historical decision-admission evidence |
| `NOVA_PUBLIC_STATE_TEMPLATES.md` | ARCHIVE_LEGACY | historical decision-constraint publishing templates |
| `architecture-framing-sync-notes.md` | ARCHIVE_SEMANTIC_MIGRATION | prior framing pass notes |
| `developer-docs-coherence-audit.md` | ARCHIVE_SEMANTIC_MIGRATION | Month Two audit artifact |
| `doctrine-alignment-report.md` | ARCHIVE_SEMANTIC_MIGRATION | prior doctrine-alignment report |
| `repository-coherence-audit.md` | ARCHIVE_SEMANTIC_MIGRATION | repository audit artifact |
| `sovereignty-boundary-validation-notes.md` | ARCHIVE_SECURITY_OR_GOVERNANCE | historical boundary review |
| `telemetry-semantics-update-summary.md` | ARCHIVE_SEMANTIC_MIGRATION | historical terminology pass |
| `terminology-migration-summary.md` | ARCHIVE_SEMANTIC_MIGRATION | historical terminology pass |
| `semantic-change-log.md` | MOVE_TO_DOCS_HISTORY | useful chronology, not root entry material |
| `unresolved-risks-and-actions.md` | ARCHIVE_OR_RECONCILE | stale Month Two follow-up list |
| `nova_state_log.md` | ARCHIVE_LEGACY | historical runtime state snapshot |
| `sharpe-nova-os` | REMOVE_CURRENT_TREE | zero-byte residue with no external role |

### Private-target implementation residue

The following current public paths were already classified as private-target
material during the repository split. Their history is already public, but they
should not remain the future canonical implementation surface.

Representative root paths:

```text
.dockerignore
Dockerfile
app.py
runtime.txt
add_key_aliases.py
apply_key_aliases.py
export_nova_state.py
fix_key_aliases.py
fix_key_aliases_clean.py
key_manager.py
```

Representative directories:

```text
agent_files/
archive/
chronology/
config/
core/
deployment/
nova/
nova_api/
reports/
retail_context/
```

Selected public validators, schemas, synthetic fixtures, examples, and contract
tests should remain public where they improve interoperability and verifiability.

Removal or relocation of any current path in this section is deletion-bearing
public sanitization and remains blocked pending explicit Architect authority.

## Open work-item hygiene

### Pull requests

PR #8, the July NSF hardening draft, is closed unmerged as superseded by the
current public/private architecture. Its branch/history is preserved. Any future
NSF work should start from current `main`.

### Issues

Issue #56 remains open because the historical migration issue also carries the
separate public-sanitization removal gate. Current evidence shows stabilization
and CCO completion review are satisfied; explicit Architect deletion authority
remains outstanding.

Issue #65 remains open until its source-role reconciliation completion evidence
is independently verified. It must not be closed merely for appearance.

## Repository metadata target

The public repository metadata should eventually read approximately:

```text
Description:
Sharpe Nova OS is pre-execution decision-context infrastructure for
consequential machine-prepared capital actions.

Topics:
decision-context
ai-agents
agentic-finance
treasury
governance
x402
usdc
```

Empty or unused GitHub surfaces such as Wiki and Projects should be disabled if
they are not going to be maintained.

Metadata/settings changes do not change Nova authority, production state, or
corporate accepted state.

## License review

The repository is currently MIT licensed.

Because the durable architecture now separates a public contract/proof surface
from private production machinery and proprietary derivation, repository-wide
license posture should receive separate corporate/legal review before any
license change.

This plan does not recommend or authorize a license change.

## Next execution gate

Once the Architect separately authorizes deletion-bearing public sanitization,
execute against a fresh `main` with an exact path manifest.

The execution sequence should:

1. preserve required public contracts and validators;
2. relocate or remove historical root clutter;
3. remove private-target implementation from the current public tree only after
   confirming current private-source continuity;
4. update links and validation manifests;
5. run full exact-head CI;
6. inspect the rendered repository surface;
7. stop before merge if any current public contract or verification path is lost.

```yaml
current_hygiene_state:
  public_narrative_reconciled: true
  stale_NSF_PR_closed_unmerged: true
  root_classification_complete: true
  stabilization_observation: verified_complete
  CCO_completion_review: satisfied
  deletion_bearing_sanitization_authorized: false
  deletion_bearing_sanitization_started: false
```
