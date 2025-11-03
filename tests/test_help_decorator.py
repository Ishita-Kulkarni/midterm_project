import pytest
from app.help_decorator import HelpDecorator
from app.operations import get_operation
from colorama import Fore, Style

@pytest.fixture
def operation_dict():
    return {
        "add": get_operation("add"),
        "subtract": get_operation("subtract"),
        "multiply": get_operation("multiply"),
        "divide": get_operation("divide"),
        "power": get_operation("power"),
    }

def test_show_help_output(capsys, operation_dict):
    """Test that HelpDecorator prints all operations and commands."""
    help_menu = HelpDecorator(operation_dict)
    help_menu.show_help()

    captured = capsys.readouterr().out

    # Check that all operations are printed
    for key, op in operation_dict.items():
        class_name = op.__class__.__name__
        symbol = getattr(op, "symbol", key)
        assert f"{class_name} ({symbol})" in captured

    # Check that commands are printed correctly
    commands = [
        "history – Display calculation history",
        "clear – Clear calculation history",
        "undo – Undo the last calculation",
        "redo – Redo the last undone calculation",
        "save – Manually save calculation history to file",
        "load – Load calculation history from file",
        "help – Display this help message",
        "exit – Exit the application"
    ]

    for cmd_text in commands:
        assert cmd_text in captured

    # Optional: Check that color codes are present
    assert Fore.CYAN in captured
