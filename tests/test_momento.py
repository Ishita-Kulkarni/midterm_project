import pytest
from app.calculator_memento import Memento
from app.calculation import Calculation
from app.operations import Addition

def test_memento_save_and_restore_multiple():
    calc_history = [
        Calculation(1, 2, Addition()),
        Calculation(3, 4, Addition())
    ]
    memento = Memento(calc_history.copy())
    restored = memento.restore()
    assert restored == calc_history

def test_memento_empty_history():
    memento = Memento([])
    restored = memento.restore()
    assert restored == []
    
def test_memento_save_restore():
    m = Memento()
    m.save_state({"result": 42})
    state = m.restore_state()
    assert state == {"result": 42}

def test_memento_multiple_states():
    m = Memento()
    m.save_state({"result": 1})
    m.save_state({"result": 2})
    state = m.restore_state()
    assert state == {"result": 2}  # Last saved state
