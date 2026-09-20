from scripts.validate_identity_protection import validate

def test_nova_identity_protection_is_coherent() -> None:
    assert validate() == []
