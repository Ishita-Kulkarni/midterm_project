from abc import ABC, abstractmethod

class Operation(ABC):
    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

    @abstractmethod
    def execute(self, num1: float, num2: float) -> float:
        pass

class Addition(Operation):
    symbol = '+'
    
    def execute(self, num1: float, num2: float) -> float:
        return num1 + num2

class Subtraction(Operation):
    symbol = '-'
    
    def execute(self, num1: float, num2: float) -> float:
        return num1 - num2

class Multiplication(Operation):
    symbol = '*'
    
    def execute(self, num1: float, num2: float) -> float:
        return num1 * num2

class Division(Operation):
    symbol = '/'
    
    def execute(self, num1: float, num2: float) -> float:
        return num1 / num2