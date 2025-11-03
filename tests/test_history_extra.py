import pytest
from app.history import History, LoggingObserver, AutoSaveObserver
from app.calculation import Calculation
from app.operations import Addition
import os

def test_history_add_and_clear():
    h = History()
    h.add_entry("1+1", 2)
    assert h.get_entries() == [("1+1", 2)]
    h.clear()
    assert h.get_entries() == []
    h.add_entry("2+2", 4)
    h.clear_history()
    assert h.get_entries() == []

def test_history_get_history():
    h = History()
    h.add_entry("1+1", 2)
    h.add_entry("2+2", 4)
    assert h.get_history() == ["1+1", "2+2"]

def test_logging_observer(tmp_path):
    class DummyLogger:
        def __init__(self):
            self.logged = []
        def info(self, msg):
            self.logged.append(msg)
    logger = DummyLogger()
    obs = LoggingObserver(logger)
    calc = Calculation(1, 2, Addition())
    calc._result = 3
    obs.update(calc)
    assert any("1" in m for m in logger.logged)

def test_auto_save_observer(tmp_path):
    file_path = tmp_path / "history.csv"
    obs = AutoSaveObserver(str(file_path))
    calc = Calculation(1, 2, Addition())
    calc._result = 3
    obs.update(calc)
    assert os.path.exists(file_path)
