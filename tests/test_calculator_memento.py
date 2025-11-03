import pytest
from app.calculator_memento import Memento, Caretaker

def test_memento_restore_and_state():
    m = Memento([1, 2, 3])
    assert m.restore() == [1, 2, 3]
    m.save_state([4, 5])
    assert m.restore_state() == [4, 5]
    assert m.get_saved_state() == [4, 5]

def test_caretaker_undo_redo():
    c = Caretaker()
    state1 = [1]
    state2 = [1, 2]
    state3 = [1, 2, 3]
    c.save(state1)
    c.save(state2)
    c.save(state3)
    # After saves, can_undo should be True, can_redo should be False
    assert c.can_undo() is True
    assert c.can_redo() is False
    # Undo should return the last state (state3)
    undo1 = c.undo(state3)
    assert undo1 == state3
    # After undo, can_redo should be True
    assert c.can_redo() is True
    # Redo should return the state we just undid
    redo1 = c.redo(state3)
    assert redo1 == state3
