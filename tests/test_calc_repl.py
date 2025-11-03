import pytest
from app import calc

def test_add():
    assert calc.add(1, 2) == 3
    assert calc.add(-1, -2) == -3
    assert calc.add(1.5, 2.5) == 4.0

def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2

def test_multiply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6

def test_divide():
    assert calc.divide(6, 2) == 3
    assert calc.divide(7.5, 2.5) == 3.0
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)

def test_print_help(capsys):
    calc.print_help()
    out, _ = capsys.readouterr()
    assert "Commands:" in out

def test_history_and_clear(monkeypatch):
    from app.operations import Addition
    c = calc.Calculator()
    c.calculate(1, 2, Addition())
    c.history.clear()
    assert c.history == []

def test_repl_exit(monkeypatch):
    # Simulate 'exit' command
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # The REPL should break and return, not raise SystemExit
    calc.repl()
