# app/calculator_memento.py
class CalculatorMemento:
    def __init__(self, state):
        self._state = state  # store a copy of the history or whatever state

    def restore(self):
        # Return a copy so tests can restore the calculator’s history
        return self._state.copy()

class Memento:
    def __init__(self, state=None):
        self._state = state

    def save_state(self, state):
        """Save the given state."""
        self._state = state

    def get_saved_state(self):
        """Return the saved state."""
        return self._state

    def restore_state(self):
        """Return the saved state."""
        return self._state

    def restore(self):
        """Return a copy of the stored state (for history lists)."""
        if isinstance(self._state, list):
            return self._state.copy()
        return self._state

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
        # Use restore() for compatibility
        return m.restore() if hasattr(m, 'restore') else m._state.copy()

    def redo(self, current_state):
        if not self._redo_stack:
            return current_state
        m = self._redo_stack.pop()
        self._undo_stack.append(Memento(current_state))
        return m.restore() if hasattr(m, 'restore') else m._state.copy()
