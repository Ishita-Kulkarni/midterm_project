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

class Root(Operation):
    symbol = 'root'
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Root degree cannot be zero")
        return a ** (1 / b)

class Modulus(Operation):
    symbol = '%'
    def execute(self, a, b):
        return a % b

class IntDivision(Operation):
    symbol = '//'
    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a // b

class Percentage(Operation):
    symbol = '%'
    def execute(self, a, b):
        return (a / b) * 100
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
        "root": Root(),
        "modulus": Modulus(),
        "int_divide": IntDivision(),
        "percent": Percentage(),
        "abs_diff": AbsoluteDifference(),
    }
    return operations.get(symbol)

