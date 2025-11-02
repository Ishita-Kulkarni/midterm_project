# app/exceptions.py
class CalculatorError(Exception):
    pass

class OperationError(CalculatorError):
    pass

class ValidationError(CalculatorError):
    pass
