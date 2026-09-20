from scripts.validate_legacy_semantic_quarantine import validate


def test_legacy_v1_semantic_quarantine_is_coherent() -> None:
    assert validate() == []
