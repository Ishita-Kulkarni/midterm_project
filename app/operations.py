# app/operations.py
from abc import ABC, abstractmethod
from math import pow, isclose
from typing import Callable
from .exceptions import OperationError
import math

class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

class Add(Operation):
    def execute(self, a, b): return a + b

class Subtract(Operation):
    def execute(self, a, b): return a - b

class Multiply(Operation):
    def execute(self, a, b): return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Division by zero")
        return a / b

class Power(Operation):
    def execute(self, a, b): return pow(a, b)

class Root(Operation):
    def execute(self, a, b):
        # nth root: a ** (1/b) where b is n
        if b == 0:
            raise OperationError("Zero root")
        return a ** (1.0 / b)

class Modulus(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Modulus by zero")
        return a % b

class IntDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Integer division by zero")
        return a // b

class Percent(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Percent base cannot be zero")
        return (a / b) * 100

class AbsDiff(Operation):
    def execute(self, a, b):
        return abs(a - b)

# factory
def get_operation(name: str) -> Operation:
    ops = {
        "add": Add, "subtract": Subtract, "multiply": Multiply,
        "divide": Divide, "power": Power, "root": Root,
        "modulus": Modulus, "int_divide": IntDivide,
        "percent": Percent, "abs_diff": AbsDiff
    }
    try:
        return ops[name.lower()]()
    except KeyError:
        raise OperationError(f"Unknown operation {name}")
