from app import validate_item


def test_validate_item_with_valid_string():
    assert validate_item("valid item") is True

def test_validate_item_with_empty_string():
    assert validate_item("") is False

def test_validate_item_with_whitespace_only():
    assert validate_item("   ") is False

def test_validate_item_with_none():
    assert validate_item(None) is False

def test_validate_item_with_non_string():
    assert validate_item(123) is False
    assert validate_item([]) is False
    assert validate_item({}) is False
