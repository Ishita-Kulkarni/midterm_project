from typing import List, Optional
from .calculation import Calculation
from .calculator_config import config

class History:
    def __init__(self):
        self._calculations: List[Calculation] = []

    def add_calculation(self, calculation: Calculation):
        """Add a calculation to history."""
        self._calculations.append(calculation)
        if len(self._calculations) > config.max_history_size:
            self._calculations.pop(0)

    def get_calculations(self) -> List[Calculation]:
        """Get all calculations from history."""
        return self._calculations.copy()

    def clear(self):
        """Clear the history."""
        self._calculations.clear()

    def get_last_calculation(self) -> Optional[Calculation]:
        """Get the most recent calculation."""
        return self._calculations[-1] if self._calculations else None