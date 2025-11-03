# app/calculation.py
from dataclasses import dataclass, asdict
from datetime import datetime
from app.exceptions import CalculatorError

@dataclass
class Calculation:
    operation: str
    a: float
    b: float
    result: float
    timestamp: str = None
    
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
        self._result = None
    def __str__(self):
        op_symbol = getattr(self.operation, 'symbol', str(self.operation))
        try:
            res = self._result if self._result is not None else self.result
        except Exception:
            res = '?'
        return f"Calculation: {self.a} {op_symbol} {self.b} = {res}"

    @property
    def result(self):
        if self._result is None:
            raise ValueError("Result not available before execution")
        return self._result

    def execute(self):
        try:
            self._result = self.operation.execute(self.a, self.b)
            return self._result
        except CalculatorError as e:
            raise e
        except Exception as e:
            raise CalculatorError(str(e))

    @property
    def value(self):
        """Return result if available, otherwise raise ValueError."""
        if self.result is None:
            raise ValueError("Result not computed yet")
        return self.result


    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return asdict(self)
