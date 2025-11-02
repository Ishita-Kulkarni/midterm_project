from typing import List, Optional
from .calculation import Calculation
from .operations import Operation
from .history import History
from .calculator_memento import CalculatorMemento
from .logger import Logger
from .exceptions import CalculatorError
from .input_validators import validate_input

class Calculator:
    def __init__(self):
        self.history = History()
        self.logger = Logger()

    def calculate(self, num1: float, num2: float, operation: Operation) -> float:
        """
        Perform a calculation and store it in history.
        """
        try:
            validate_input(num1, num2, operation)
            calculation = Calculation(num1, num2, operation)
            result = calculation.execute()
            self.history.add_calculation(calculation)
            self.logger.log_calculation(calculation)
            return result
        except Exception as e:
            self.logger.log_error(str(e))
            raise CalculatorError(str(e))

    def create_memento(self) -> CalculatorMemento:
        """Create a memento of the current calculator state."""
        return CalculatorMemento(self.history.get_calculations())