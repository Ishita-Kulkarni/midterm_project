# app/calculation.py
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Calculation:
    operation: str
    a: float
    b: float
    result: float
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return asdict(self)
