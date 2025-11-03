import pytest
from app.input_validators import validate_number
from app.exceptions import InvalidInputError

def test_validate_number_valid_and_float_conversion():
    # Valid integer input
    assert validate_number(10) == 10
    # Valid float input
    assert validate_number(10.5) == 10.5
    # Valid string numbers
    assert validate_number("42") == 42
    assert validate_number("3.1415") == 3.1415

def test_validate_number_invalid_inputs():
    invalid_values = ["abc", "", None, [], {}]
    for val in invalid_values:
        with pytest.raises(InvalidInputError):
            validate_number(val)