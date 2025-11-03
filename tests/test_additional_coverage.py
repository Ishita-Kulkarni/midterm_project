import pytest
from app import calc
from app.calculator_config import CalculatorConfig
from app.calculator_memento import Memento
from app.input_validators import validate_number
from app.history import History
from app.exceptions import InvalidInputError




def test_calc_basic_ops():
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 2) == 3
    assert calc.multiply(3, 4) == 12
    assert calc.divide(8, 2) == 4


def test_calculator_config_defaults():
    config = CalculatorConfig()
    assert hasattr(config, "HISTORY_LIMIT")
    assert config.HISTORY_LIMIT > 0


def test_memento_save_and_restore():
    memento = Memento()
    memento.save_state({"result": 10})
    assert memento.restore_state() == {"result": 10}


def test_input_validators_accepts_numbers():
    assert validate_number(5) == 5
    assert validate_number("10") == 10
    with pytest.raises(InvalidInputError):  
        validate_number("abc")


def test_history_store_and_clear():
    history = History()
    history.add_entry("2 + 2 = 4")
    assert "2 + 2 = 4" in history.get_history()
    history.clear_history()
    assert history.get_history() == []
