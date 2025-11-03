from typing import Any
from .operations import Operation
from .exceptions import InvalidInputError, DivisionByZeroError

def validate_input(num1: float, num2: float, operation: Operation) -> None:
    """Validate calculator input values and operation."""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise InvalidInputError("Input values must be numbers")
    symbol = getattr(operation, 'symbol', None)
    if symbol == '/' and num2 == 0:
        raise DivisionByZeroError("Cannot divide by zero")

def validate_number(value):
    """Validate that the input is a number (int or float)."""
    try:
        return float(value)
    except (TypeError, ValueError):
        raise InvalidInputError(f"Invalid input: {value}")


def validate_non_negative(value):
    """Ensure the number is non-negative."""
    num = validate_number(value)
    if num < 0:
        raise InvalidInputError(f"Value must be non-negative: {value}")
    return num
