from typing import Any
from .operations import Operation
from .exceptions import InvalidInputError, DivisionByZeroError

def validate_input(num1: float, num2: float, operation: Operation) -> None:
    """Validate calculator input values and operation."""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise InvalidInputError("Input values must be numbers")

    if operation.symbol == '/' and num2 == 0:
        raise DivisionByZeroError("Cannot divide by zero")