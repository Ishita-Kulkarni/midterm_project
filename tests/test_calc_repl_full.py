import pytest
from app import calc
from app.operations import Addition, Subtraction, Multiplication, Division

def test_repl_help(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc.repl()
    out, _ = capsys.readouterr()
    assert "Commands:" in out

def test_repl_history(monkeypatch, capsys):
    c = calc.Calculator()
    c.calculate(1, 2, Addition())
    monkeypatch.setattr("app.calc.calc", c)
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc.repl()
    out, _ = capsys.readouterr()
    assert "1" in out or "Calculation" in out

def test_repl_clear(monkeypatch, capsys):
    c = calc.Calculator()
    c.calculate(1, 2, Addition())
    monkeypatch.setattr("app.calc.calc", c)
    inputs = iter(["clear", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc.repl()
    out, _ = capsys.readouterr()
    assert "History cleared" in out

def test_repl_undo_redo(monkeypatch, capsys):
    c = calc.Calculator()
    c.calculate(1, 2, Addition())
    monkeypatch.setattr("app.calc.calc", c)
    inputs = iter(["undo", "redo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc.repl()
    out, _ = capsys.readouterr()
    assert "Undo done" in out and "Redo done" in out

def test_repl_save_load(monkeypatch, capsys, tmp_path):
    c = calc.Calculator()
    c.calculate(1, 2, Addition())
    monkeypatch.setattr("app.calc.calc", c)
    savefile = tmp_path / "history.csv"
    monkeypatch.setattr("os.getenv", lambda key, default=None: str(savefile) if "HISTORY_FILE" in key else default)
    inputs = iter(["save", "clear", "load", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc.repl()
    out, _ = capsys.readouterr()
    assert "Saved" in out and "Loaded" in out

def test_repl_invalid_command(monkeypatch, capsys):
    inputs = iter(["foobar", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc.repl()
    out, _ = capsys.readouterr()
    assert "Usage:" in out or "Error:" in out

def test_repl_operation(monkeypatch, capsys):
    inputs = iter(["add 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc.repl()
    out, _ = capsys.readouterr()
    assert "= " in out
