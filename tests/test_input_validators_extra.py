import pytest
from app.input_validators import validate_non_negative, validate_input
from app.operations import Addition, Division
from app.exceptions import InvalidInputError, DivisionByZeroError

def test_validate_non_negative():
    assert validate_non_negative(5) == 5
    assert validate_non_negative("10") == 10.0
    with pytest.raises(InvalidInputError):
        validate_non_negative(-1)
    with pytest.raises(InvalidInputError):
        validate_non_negative("-2")

def test_validate_input():
    validate_input(1, 2, Addition())  # Should not raise
    with pytest.raises(InvalidInputError):
        validate_input("a", 2, Addition())
    with pytest.raises(DivisionByZeroError):
        validate_input(1, 0, Division())
