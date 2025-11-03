# app/history.py 
import pandas as pd
import os
from .calculation import Calculation
from dotenv import load_dotenv
load_dotenv()

HIST_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "./data")
os.makedirs(HIST_DIR, exist_ok=True)
HIST_FILE = os.path.join(HIST_DIR, os.getenv("CALCULATOR_HISTORY_FILE", "history.csv"))

class History:
    def __init__(self):
        self.entries = []

    def add_entry(self, expression, result=None):
        self.entries.append((expression, result))

    def get_entries(self):
        return self.entries

    def get_history(self):
        """Return just the expressions for easier testing."""
        return [expr for expr, _ in self.entries]

    def clear(self):
        self.entries.clear()

    def clear_history(self):
        """Alias for clear(), for test compatibility."""
        self.clear()



class Observer:
    def update(self, calculation: Calculation):
        raise NotImplementedError

class LoggingObserver(Observer):
    def __init__(self, logger):
        self.logger = logger
    def update(self, calculation):
        self.logger.info(f"{calculation.operation} {calculation.a},{calculation.b} => {calculation.result}")

class AutoSaveObserver(Observer):
    def __init__(self, filepath=HIST_FILE):
        self.filepath = filepath
    def update(self, calculation):
        df = pd.DataFrame([calculation.to_dict()])
        # append to CSV; if file doesn't exist create header
        header = not os.path.exists(self.filepath)
        df.to_csv(self.filepath, mode='a', index=False, header=header)
