from __future__ import annotations

import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/governance/legacy-v1-semantic-quarantine-v1.yaml"


def _read(path: Path) -> str:
    if not path.is_file():
        raise AssertionError(f"missing quarantine artifact: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []

    try:
        manifest = yaml.safe_load(_read(MANIFEST))
    except (AssertionError, yaml.YAMLError) as exc:
        return [str(exc)]

    if manifest.get("required_classification") != "Legacy_v1_compatibility_only":
        errors.append("Legacy quarantine classification changed")
    if manifest.get("canonical_current_identity") is not False:
        errors.append("Legacy quarantine cannot become canonical current identity")
    if manifest.get("new_external_integrations_permitted") is not False:
        errors.append("Legacy quarantine cannot permit new external integrations")

    for relative in manifest.get("markdown_compatibility_artifacts") or []:
        path = ROOT / relative
        try:
            text = _read(path)
        except AssertionError as exc:
            errors.append(str(exc))
            continue
        if "**Legacy v1 compatibility artifact**" not in text:
            errors.append(f"Legacy markdown artifact missing quarantine notice: {relative}")
        if "does **not** define Sharpe Nova OS's canonical current identity" not in text:
            errors.append(f"Legacy markdown artifact missing canonical-identity boundary: {relative}")

    for relative in manifest.get("structured_compatibility_artifacts") or []:
        path = ROOT / relative
        try:
            obj = json.loads(_read(path))
        except (AssertionError, json.JSONDecodeError) as exc:
            errors.append(f"Legacy structured artifact invalid: {relative}: {exc}")
            continue
        classification = obj.get("_identity_classification") or {}
        if classification.get("scope") != "Legacy_v1_compatibility_only":
            errors.append(f"Legacy structured artifact missing quarantine classification: {relative}")
        if classification.get("canonical_current_identity") is not False:
            errors.append(f"Legacy structured artifact became canonical current identity: {relative}")
        if classification.get("new_external_integrations_permitted") is not False:
            errors.append(f"Legacy structured artifact permits new external integrations: {relative}")
        if classification.get("authority_model_applies_only_to") != "Legacy_v1_implemented_behavior":
            errors.append(f"Legacy structured artifact authority scope changed: {relative}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("legacy_v1_semantic_quarantine: incoherent")
        for error in errors:
            print(f"- {error}")
        return 1
    print("legacy_v1_semantic_quarantine: coherent")
    print("classification: Legacy_v1_compatibility_only")
    print("canonical_current_identity: false")
    print("new_external_integrations_permitted: false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
