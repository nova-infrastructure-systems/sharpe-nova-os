from __future__ import annotations

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "docs/governance/publication-governance-policy-v1.yaml"
STANDARD_PATH = ROOT / "docs/governance/publication-governance-standard-v1.0.md"
CHECKLIST_PATH = ROOT / "docs/governance/public-file-review-checklist.md"
VISIBILITY_PATH = ROOT / "docs/governance/public-repo-visibility-standard.md"
BOUNDARY_PATH = ROOT / "docs/governance/public-private-repository-boundary-v0.1.md"
PR_TEMPLATE_PATH = ROOT / ".github/pull_request_template.md"

EXPECTED_EXTERNAL_VALUE = {
    "category_comprehension",
    "interoperability",
    "verification",
    "external_trust",
}
EXPECTED_PRIVATE_RISK = {
    "proprietary_derivation",
    "production_topology",
    "operating_evidence",
    "corporate_accepted_state",
    "institutional_private_state",
    "security_sensitive_implementation",
    "provider_only_secret",
}
EXPECTED_EXPOSURE_CLASSES = {"PUBLIC", "PUBLIC_SANITIZED", "PRIVATE", "PROVIDER_ONLY"}
EXPECTED_ENTRY_PATHS = {"README.md", "CURRENT_STATE.md", "CATEGORY.md", "SYSTEM_IDENTITY.md"}


def _text(path: Path) -> str:
    if not path.is_file():
        raise AssertionError(f"missing required publication-governance file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []

    try:
        policy = yaml.safe_load(_text(POLICY_PATH))
    except (AssertionError, yaml.YAMLError) as exc:
        return [str(exc)]

    if policy.get("status") != "active":
        errors.append("policy.status must be active")
    if policy.get("repository_role") != "NON_AUTHORITATIVE_GOVERNED_PROJECTION":
        errors.append("policy.repository_role changed")
    if policy.get("authority") != "Architect":
        errors.append("policy.authority must remain Architect")
    if policy.get("control_owner") != "Jarvis-Nova_CCO":
        errors.append("policy.control_owner must remain Jarvis-Nova_CCO")
    if policy.get("decision_authority") != "Architect":
        errors.append("policy.decision_authority must remain Architect")
    if policy.get("default_disposition") != "PRIVATE":
        errors.append("policy.default_disposition must remain PRIVATE")

    gate = policy.get("publication_gate") or {}
    if set(gate.get("external_value_require_one") or []) != EXPECTED_EXTERNAL_VALUE:
        errors.append("publication external-value classes changed")
    if set(gate.get("private_risk_require_none_material") or []) != EXPECTED_PRIVATE_RISK:
        errors.append("publication private-risk classes changed")
    if set(policy.get("exposure_classes") or []) != EXPECTED_EXPOSURE_CLASSES:
        errors.append("exposure classes changed")

    cco = policy.get("cco_review_required_for") or {}
    if set(cco.get("public_entry_paths") or []) != EXPECTED_ENTRY_PATHS:
        errors.append("CCO public-entry review triggers changed")

    standard = _text(STANDARD_PATH)
    for marker in (
        "Publication is not the default merely because an artifact is safe enough to expose.",
        "default_when_uncertain: PRIVATE",
        "The absence of an obvious secret is not sufficient reason to publish.",
        "Jarvis-Nova CCO owns coherence control",
        "The Architect retains final authority.",
    ):
        if marker not in standard:
            errors.append(f"standard missing marker: {marker}")

    checklist = _text(CHECKLIST_PATH)
    for marker in (
        "category comprehension",
        "interoperability",
        "verification",
        "external trust",
        "default to `PRIVATE`",
        "publication-governance-standard-v1.0.md",
    ):
        if marker not in checklist:
            errors.append(f"public-file checklist missing marker: {marker}")

    visibility = _text(VISIBILITY_PATH)
    for marker in (
        "affirmative external value",
        "default to private",
        "publication-governance-standard-v1.0.md",
    ):
        if marker not in visibility.lower():
            errors.append(f"visibility standard missing marker: {marker}")

    boundary = _text(BOUNDARY_PATH)
    for marker in (
        "affirmative external value",
        "default to private",
        "publication-governance-standard-v1.0.md",
    ):
        if marker not in boundary.lower():
            errors.append(f"repository boundary missing marker: {marker}")

    template = _text(PR_TEMPLATE_PATH)
    for marker in (
        "PUBLIC",
        "PUBLIC_SANITIZED",
        "PRIVATE",
        "PROVIDER_ONLY",
        "Category comprehension",
        "Interoperability",
        "Verification",
        "External trust",
        "CCO review completed",
    ):
        if marker not in template:
            errors.append(f"PR template missing publication marker: {marker}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("publication_governance: incoherent")
        for error in errors:
            print(f"- {error}")
        return 1
    print("publication_governance: coherent")
    print("default_disposition: PRIVATE")
    print("control_owner: Jarvis-Nova_CCO")
    print("decision_authority: Architect")
    return 0


if __name__ == "__main__":
    sys.exit(main())
