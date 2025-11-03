from app.calculator_memento import Caretaker

def test_caretaker_undo_redo_empty():
    c = Caretaker()
    # Undo/redo on empty stacks should return the current state
    state = [1, 2, 3]
    assert c.undo(state) == state
    assert c.redo(state) == state
