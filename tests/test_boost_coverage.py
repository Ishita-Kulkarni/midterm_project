import pytest
from app.calculator import Calculator
from app.input_validators import validate_number
from app.calculator_memento import Memento
from app.exceptions import InvalidInputError


def test_calculator_addition():
    calc = Calculator()
    from app.operations import Addition
    result = calc.calculate(3, 4, Addition())
    assert result == 7

def test_calculator_subtraction():
    calc = Calculator()
    from app.operations import Subtraction
    result = calc.calculate(10, 3, Subtraction())
    assert result == 7

def test_validate_number_invalid():
    with pytest.raises(InvalidInputError): 
        validate_number("not_a_number")

def test_validate_number_valid():
    assert validate_number(10) == 10
    assert validate_number("3.14") == 3.14

def test_memento_save_and_restore():
    m = Memento()
    m.save_state({"x": 5})
    assert m.restore_state() == {"x": 5}
