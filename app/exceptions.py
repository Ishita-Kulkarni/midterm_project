class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is attempted."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass

class InvalidInputError(CalculatorError):
    """Raised when invalid input is provided."""
    pass