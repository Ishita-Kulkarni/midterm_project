from typing import Any
from .operations import Operation

class Calculation:
    def __init__(self, num1: float, num2: float, operation: Operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        self._result = None

    def execute(self) -> float:
        """Execute the calculation and return the result."""
        self._result = self.operation.execute(self.num1, self.num2)
        return self._result

    @property
    def result(self) -> float:
        """Get the result of the calculation."""
        if self._result is None:
            raise ValueError("Calculation has not been executed yet")
        return self._result