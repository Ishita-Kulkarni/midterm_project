# app/calculator_memento.py
class Memento:
    def __init__(self, state):
        self.state = state.copy()

class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(Memento(state))
        self._redo_stack.clear()

    def can_undo(self): return bool(self._undo_stack)
    def can_redo(self): return bool(self._redo_stack)

    def undo(self, current_state):
        if not self._undo_stack:
            return current_state
        m = self._undo_stack.pop()
        self._redo_stack.append(Memento(current_state))
        return m.state.copy()

    def redo(self, current_state):
        if not self._redo_stack:
            return current_state
        m = self._redo_stack.pop()
        self._undo_stack.append(Memento(current_state))
        return m.state.copy()
