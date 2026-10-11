from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
KERNEL = ROOT / "docs/governance/nova-identity-kernel-v1.yaml"


def _text(path: str) -> str:
    file_path = ROOT / path
    if not file_path.is_file():
        raise AssertionError(f"missing agent-category artifact: {path}")
    return file_path.read_text(encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []

    try:
        kernel = yaml.safe_load(KERNEL.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [str(exc)]

    llms = _text("llms.txt")
    readme = _text("README.md")
    protocol = _text(
        "docs/governance/agent-category-comprehension-protocol-v1.md"
    )
    retail_validation = _text("docs/retail-agent/external-validation-v0.1.md")

    category = kernel.get("category") or {}
    if category.get("canonical") != "pre_execution_governance_infrastructure":
        errors.append("canonical category no longer matches agent interpretation guide")
    if category.get("architectural_frame") != "pre_execution_decision_discipline_layer":
        errors.append("architectural frame no longer matches agent interpretation guide")

    boundary = kernel.get("canonical_boundary") or {}
    if boundary.get("Nova_role") != "structure_review_context":
        errors.append("Nova role changed away from structure_review_context")
    if boundary.get("decision_owner") != "local_authority":
        errors.append("local authority ownership changed")
    if boundary.get("execution_owner") != "external_system":
        errors.append("execution ownership changed")
    if boundary.get("Nova_executes") is not False:
        errors.append("Nova execution boundary changed")

    product_separation = kernel.get("product_separation") or {}
    for name, value in product_separation.items():
        if value is not False:
            errors.append(f"product surface began defining OS identity: {name}")

    llms_markers = (
        "pre-execution governance infrastructure",
        "pre-execution decision discipline layer",
        "Agent prepares an action.",
        "Nova structures review context.",
        "Local authority decides.",
        "External systems execute.",
        "Nova does not execute.",
        "Products do not define the OS.",
        "payment != authority",
        "settlement != authority",
        "Settlement evidence is not delivery evidence.",
        "payment_verified != settled",
        "settled != delivered",
        "delivered != completed",
        "docs/governance/nova-identity-kernel-v1.yaml",
        "docs/governance/agent-category-comprehension-protocol-v1.md",
    )
    for marker in llms_markers:
        if marker not in llms:
            errors.append(f"llms.txt missing category marker: {marker}")

    readme_markers = (
        "[AI-agent interpretation guide](llms.txt)",
        "Product and payment surfaces do not define the OS.",
        "docs/governance/agent-category-comprehension-protocol-v1.md",
    )
    for marker in readme_markers:
        if marker not in readme:
            errors.append(f"README missing agent-category marker: {marker}")

    protocol_markers = (
        "payment-stress test",
        "payment middleware",
        "settlement middleware",
        "pre_execution_governance_infrastructure",
        "Nova_approval_authority: false",
        "Nova_execution_authority: false",
        "payment_creates_authority: false",
        "settlement_creates_authority: false",
        "settlement_alone_proves_delivery: false",
        "delivery_requires_separate_evidence: true",
        "authority_effect: none",
    )
    for marker in protocol_markers:
        if marker not in protocol:
            errors.append(f"agent-category protocol missing: {marker}")

    retail_evidence_markers = (
        "payment_verified != settled",
        "settled != delivered",
        "delivered != completed",
        "delivery requires separate delivery evidence",
    )
    for marker in retail_evidence_markers:
        if marker not in retail_validation:
            errors.append(f"retail validation missing evidence-state marker: {marker}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("agent_category_coherence: incoherent")
        for error in errors:
            print(f"- {error}")
        return 1

    print("agent_category_coherence: coherent")
    print("primary_category: pre_execution_governance_infrastructure")
    print("product_surfaces_define_os: false")
    print("authority_effect: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
