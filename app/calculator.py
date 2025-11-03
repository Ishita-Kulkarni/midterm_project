# app/calculator.py
from .operations import get_operation
from .history import LoggingObserver, AutoSaveObserver
from .logger import logger
from .calculation import Calculation
from .calculator_memento import Caretaker
from app.operations import Operation 
from .exceptions import ValidationError
from .exceptions import DivisionByZeroError
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()

MAX_HISTORY = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
PRECISION = int(os.getenv("CALCULATOR_PRECISION", 6))
AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"

class Calculator:
    def __init__(self):
        self.history = []  # list[Calculation]
        self.observers = []
        self.caretaker = Caretaker()

    def register(self, obs):
        self.observers.append(obs)

    def notify(self, calc: Calculation):
        for o in self.observers:
            try:
                o.update(calc)
            except Exception as e:
                logger.error(f"Observer failed: {e}")

    def validate(self, a, b):
        try:
            a = float(a); b = float(b)
        except Exception:
            raise ValidationError("Inputs must be numbers")
        max_val = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1e12))
        if abs(a) > max_val or abs(b) > max_val:
            raise ValidationError("Input exceeds allowed magnitude")
        return a, b

    def perform(self, op_name, a, b):
        a, b = self.validate(a, b)
        operation = get_operation(op_name)
        result = operation.execute(a, b)
        if isinstance(result, float):
            result = round(result, PRECISION)
        calc = Calculation(a, b, operation)
        calc._result = result
        # save state into memento before mutation
        self.caretaker.save(self.history)
        self.history.append(calc)
        # trim history
        if len(self.history) > MAX_HISTORY:
            self.history.pop(0)
        # notify observers
        self.notify(calc)
        return calc

    def undo(self):
        self.history = self.caretaker.undo(self.history)
        return self.history

    def redo(self):
        self.history = self.caretaker.redo(self.history)
        return self.history

    # persistence helpers
    def save_history(self, filepath=None):
        filepath = filepath or os.getenv("CALCULATOR_HISTORY_FILE", "./data/history.csv")
        df = pd.DataFrame([c.to_dict() for c in self.history])
        df.to_csv(filepath, index=False)
    def load_history(self, filepath=None):
        filepath = filepath or os.getenv("CALCULATOR_HISTORY_FILE", "./data/history.csv")
        if not os.path.exists(filepath):
            return []
        df = pd.read_csv(filepath)
        loaded = []
        for _, row in df.iterrows():
            # Use only the constructor args Calculation(a, b, operation)
            # Set _result and timestamp after creation
            calc = Calculation(row['a'], row['b'], row['operation'])
            if hasattr(calc, '_result'):
                calc._result = row['result']
            if hasattr(calc, 'timestamp') and 'timestamp' in row:
                calc.timestamp = row['timestamp']
            loaded.append(calc)
        self.history = loaded
        return self.history
    def calculate(self, a, b, operation: Operation):
        # Accepts operation as an Operation instance
        result = operation.execute(a, b)
        calc = Calculation(a, b, operation)
        calc._result = result  # Set result for compatibility
        self.history.append(calc)
        return result