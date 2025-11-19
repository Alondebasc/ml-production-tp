"""Unit tests for pure functions in the Flask app."""

from app import validate_item


def test_validate_item_with_valid_string():
    """Test that a valid non-empty string returns True."""
    assert validate_item("valid item") is True


def test_validate_item_with_empty_string():
    """Test that an empty string returns False."""
    assert validate_item("") is False


def test_validate_item_with_whitespace_only():
    """Test that a string with only whitespace returns False."""
    assert validate_item("   ") is False


def test_validate_item_with_none():
    """Test that None returns False."""
    assert validate_item(None) is False


def test_validate_item_with_non_string():
    """Test that non-string types return False."""
    assert validate_item(123) is False
    assert validate_item([]) is False
    assert validate_item({}) is False
