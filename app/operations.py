from app.exceptions import OperationError, DivisionByZeroError


class Operation:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement execute method")


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Subtraction(Operation):
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    symbol = '/'
    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a / b

class Power(Operation):
    def execute(self, a, b):
        return a ** b


class AbsoluteDifference(Operation):
    def execute(self, a, b):
        return abs(a - b)


def get_operation(symbol):
    operations = {
        "add": Addition(),
        "subtract": Subtraction(),
        "multiply": Multiplication(),
        "divide": Division(),
        "power": Power(),
        "abs_diff": AbsoluteDifference(),
    }
    return operations.get(symbol)

