from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
KERNEL = ROOT / "docs/governance/nova-identity-kernel-v1.yaml"

def _text(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        raise AssertionError(f"missing identity artifact: {path}")
    return p.read_text(encoding="utf-8")

def validate() -> list[str]:
    errors: list[str] = []
    try:
        kernel = yaml.safe_load(KERNEL.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [str(exc)]

    if kernel.get("kernel_version") != "1.0.0":
        errors.append("identity kernel version changed")
    if kernel.get("repository_role") != "NON_AUTHORITATIVE_GOVERNED_PROJECTION":
        errors.append("public repository role changed")
    if kernel.get("decision_authority") != "Architect":
        errors.append("Architect final authority changed")
    if kernel.get("accepted_state_effect") != "none":
        errors.append("public identity projection cannot mutate accepted state")

    category = kernel.get("category") or {}
    if category.get("canonical") != "pre_execution_decision_context_infrastructure":
        errors.append("canonical category changed")
    if category.get("architectural_frame") != "pre_execution_decision_discipline_layer":
        errors.append("architectural frame changed")

    boundary = kernel.get("canonical_boundary") or {}
    if boundary.get("Nova_role") != "structure_review_context":
        errors.append("Nova role changed")
    if boundary.get("decision_owner") != "local_authority":
        errors.append("local decision ownership changed")
    if boundary.get("execution_owner") != "external_system":
        errors.append("external execution ownership changed")
    if boundary.get("Nova_executes") is not False:
        errors.append("Nova execution boundary changed")

    identity = kernel.get("identity_invariants") or {}
    if identity.get("action_identity_is_proposal_version_identity") is not False:
        errors.append("action/proposal identity collapsed")
    if identity.get("lineage_may_be_inferred_from_similarity") is not False:
        errors.append("lineage inference from similarity became permitted")
    if identity.get("missing_lineage_behavior") != "lineage_unavailable":
        errors.append("missing lineage must remain lineage_unavailable")

    for name, value in (kernel.get("non_escalation_of_authority") or {}).get("invariants", {}).items():
        if value is not False:
            errors.append(f"authority escalation invariant violated: {name}")

    effects = kernel.get("authority_effects") or {}
    for name in ("approval_effect", "authorization_effect", "execution_effect", "capital_effect"):
        if effects.get(name) != "none":
            errors.append(f"{name} changed")

    system_identity = _text("SYSTEM_IDENTITY.md")
    category_doc = _text("CATEGORY.md")
    standard = _text("docs/governance/nova-identity-protection-layer-v1.md")
    protocol = _text("docs/governance/identity-change-protocol-v1.md")
    spec = _text("specs/review_context_contract_v2.json")

    for marker in (
        "Non-Escalation of Authority Principle",
        "action identity != proposal-version identity",
        "nova-identity-kernel-v1.yaml",
    ):
        if marker not in system_identity:
            errors.append(f"SYSTEM_IDENTITY missing: {marker}")

    for marker in (
        "Identity must not be inferred where lineage can be explicitly preserved.",
        "lineage_unavailable",
        "products do not define the OS",
    ):
        if marker not in category_doc:
            errors.append(f"CATEGORY missing: {marker}")

    if "stop before merge and escalate to the Architect" not in protocol:
        errors.append("identity change stop rule missing")
    if "No information transformation may increase the authority of its input" not in standard:
        errors.append("Non-Escalation principle missing")

    for marker in (
        '"action_and_proposal_identity_distinct": true',
        '"establishes_action_lineage": false',
        '"Nova_authority_effect": "none"',
    ):
        if marker not in spec:
            errors.append(f"target-v2 identity invariant missing: {marker}")

    return errors

def main() -> int:
    errors = validate()
    if errors:
        print("nova_identity_protection: incoherent")
        for error in errors:
            print(f"- {error}")
        return 1
    print("nova_identity_protection: coherent")
    print("repository_role: NON_AUTHORITATIVE_GOVERNED_PROJECTION")
    print("decision_authority: Architect")
    return 0

if __name__ == "__main__":
    sys.exit(main())
