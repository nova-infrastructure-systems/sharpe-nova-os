from pathlib import Path

import yaml


ACTIVATION_PATH = Path("docs/governance/canonical-authority-transfer-activation-2026-08-28.yaml")
PRIVATE_CANONICAL_REPOSITORY = "nova-infrastructure-systems/nova-core"
PUBLIC_PROJECTION_REPOSITORY = "nova-infrastructure-systems/sharpe-nova-os"
PRIVATE_CANONICAL_REGISTRY_PATH = "governance/accepted-state/registry.yaml"


def _activation() -> dict:
    return yaml.safe_load(ACTIVATION_PATH.read_text(encoding="utf-8"))


def test_public_projection_activation_is_effective_and_exact() -> None:
    activation = _activation()
    assert activation["status"] == "EFFECTIVE_REPOSITORY_VERIFIED"
    assert activation["authority_state"]["canonical_corporate_accepted_state_authority"] == PRIVATE_CANONICAL_REPOSITORY
    assert activation["authority_state"]["canonical_private_registry_path"] == PRIVATE_CANONICAL_REGISTRY_PATH
    assert activation["authority_state"]["public_repository"] == PUBLIC_PROJECTION_REPOSITORY
    assert activation["authority_state"]["public_repository_role"] == "NON_AUTHORITATIVE_GOVERNED_PROJECTION"


def test_activation_marker_preserves_original_non_authorizations() -> None:
    activation = _activation()
    assert activation["non_authorizations"]["production_runtime_change"] is False
    assert activation["non_authorizations"]["payment_or_settlement"] is False
    assert activation["non_authorizations"]["capital_movement"] is False
    # Historical transfer receipt remains immutable: later deletion authority is separate.
    assert activation["non_authorizations"]["public_runtime_deletion"] is False


def test_public_projection_cannot_claim_current_corporate_accepted_state() -> None:
    activation = _activation()
    authority = activation["authority_state"]
    rules = activation["projection_rules"]
    assert authority["public_current_accepted_state_claim_use"] == "prohibited"
    assert rules["private_registry_required_for_current_corporate_accepted_state"] is True
    assert rules["public_registry_may_support_current_corporate_accepted_state_claims"] is False


def test_active_public_entry_surfaces_do_not_claim_corporate_authority() -> None:
    current_state = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
    readme = Path("README.md").read_text(encoding="utf-8")
    start_here = Path("docs/start-here.md").read_text(encoding="utf-8")
    for text in (current_state, readme, start_here):
        assert PRIVATE_CANONICAL_REPOSITORY in text
        assert "governed public" in text.lower() or "governed external projection" in text.lower()
    assert "transfer_status: PENDING_ARCHITECT_ACCEPTANCE" not in current_state
