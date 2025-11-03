# app/exceptions.py
class CalculatorError(Exception):
    pass

class OperationError(CalculatorError):
    pass

class ValidationError(CalculatorError):
    pass

class DivisionByZeroError(OperationError):
    """Raised when a division by zero is attempted."""
    pass

class InvalidInputError(CalculatorError):
    """Raised when input validation fails."""
    pass