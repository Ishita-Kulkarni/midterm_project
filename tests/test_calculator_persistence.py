import os
import tempfile
from app.calculator import Calculator
from app.operations import Addition

def test_save_and_load_history():
    c = Calculator()
    c.calculate(1, 2, Addition())
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
        c.save_history(tmp.name)
        c.history.clear()
        assert c.history == []
        c.load_history(tmp.name)
        assert len(c.history) == 1
        assert c.history[0].a == 1
        assert c.history[0].b == 2
    os.remove(tmp.name)
