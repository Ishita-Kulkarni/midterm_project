from typing import List
from .calculation import Calculation

class CalculatorMemento:
    """Memento class for storing calculator state."""
    
    def __init__(self, calculations: List[Calculation]):
        self._state = calculations.copy()

    def get_state(self) -> List[Calculation]:
        """Return the stored calculator state."""
        return self._state.copy()