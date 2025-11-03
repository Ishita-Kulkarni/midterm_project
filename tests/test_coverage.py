import pytest
from app.calculator import Calculator
from app.operations import Addition, Subtraction, Multiplication, Division
from app.calculation import Calculation
from app.calculator_memento import Memento
from app.calculator_memento import CalculatorMemento as Memento
from app.exceptions import DivisionByZeroError, CalculatorError

def test_calculator_operations_basic():
    c = Calculator()
    # Use operation objects, not strings or direct methods
    assert c.calculate(2, 3, Addition()) == 5
    assert c.calculate(5, 3, Subtraction()) == 2
    assert c.calculate(2, 3, Multiplication()) == 6
    assert c.calculate(6, 3, Division()) == 2

def test_calculator_division_by_zero():
    c = Calculator()
    with pytest.raises(DivisionByZeroError):
        c.calculate(5, 0, Division())

def test_invalid_operation_raises():
    c = Calculator()
    with pytest.raises(AttributeError):
        c.calculate(2, 3, "nonexistent")  # still wrong type

def test_calculation_creation_and_execution():
    calc = Calculation(5, 3, Subtraction())
    assert calc.execute() == 2

def test_memento_save_and_restore():
    c = Calculator()
    calc = Calculation(2, 3, Addition())
    c.history.append(calc)  # manually add
    memento = Memento(c.history.copy())
    restored = memento.restore()
    assert restored[0].execute() == 5

def test_restore_empty_memento():
    memento = Memento([])
    restored = memento.restore()
    assert restored == []
