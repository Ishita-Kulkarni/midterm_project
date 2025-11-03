import pytest
from app.calculator import Calculator
from app.calculation import Calculation
from app.operations import Addition

class DummyObserver:
    def __init__(self):
        self.updated = False
    def update(self, calc):
        self.updated = True
        raise Exception("fail")

def test_observer_notification():
    c = Calculator()
    obs = DummyObserver()
    c.register(obs)
    calc = Calculation(1, 2, Addition())
    calc._result = 3
    # Should not raise, but observer will set updated True
    c.notify(calc)
    assert obs.updated
