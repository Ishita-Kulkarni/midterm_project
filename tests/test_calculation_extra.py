import pytest
from app.calculation import Calculation
from app.operations import Addition, Subtraction
from app.exceptions import CalculatorError

def test_value_property_before_and_after_execution():
    calc = Calculation(2, 3, Addition())
    with pytest.raises(ValueError):
        _ = calc.value
    calc.execute()
    assert calc.value == 5

def test_execute_raises_calculator_error():
    class BadOp:
        def execute(self, a, b):
            raise Exception("fail")
    calc = Calculation(1, 2, BadOp())
    with pytest.raises(CalculatorError):
        calc.execute()

def test_post_init_sets_timestamp():
    c = Calculation(1, 2, Addition())
    c.__post_init__()
    assert c.timestamp is not None

def test_to_dict():
    c = Calculation(1, 2, Addition())
    c.execute()
    d = c.to_dict()
    assert isinstance(d, dict)
    assert 'a' in d and 'b' in d and 'operation' in d
