"""
Tests for the calculator module.
"""

import pytest

from calculator import add, divide, multiply, print_hello_world, subtract


def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0


def test_multiply():
    """Test multiplication function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide():
    """Test division function."""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0


def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_print_hello_world():
    """Test print_hello_world function."""
    result = print_hello_world()
    assert result == "Hello, World!"
