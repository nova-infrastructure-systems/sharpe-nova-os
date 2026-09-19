from scripts.validate_publication_governance import validate


def test_publication_governance_is_coherent() -> None:
    assert validate() == []
