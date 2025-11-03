from colorama import Fore, Style

class HelpDecorator:
    """Generate dynamic help menu from available operations."""
    def __init__(self, operation_dict):
        self.operation_dict = operation_dict

    def show_help(self):
        print("\n=== Calculator Help Menu ===")
        for symbol, op in self.operation_dict.items():
            name = getattr(op, "name", None)
            display_name = name() if callable(name) else op.__class__.__name__
            symbol_display = getattr(op, "symbol", symbol)
            print(f"- {display_name} ({symbol_display})")
        print("- history – Display calculation history")
        print("- clear – Clear calculation history")
        print("- undo – Undo the last calculation")
        print("- redo – Redo the last undone calculation")
        print("- save – Manually save calculation history to file")
        print("- load – Load calculation history from file")
        print("- help – Display this help message")
        print("- exit – Exit the application")
        print("============================\n")
        print(Fore.CYAN + "\n=== Calculator Help Menu ===")
        for symbol, op in self.operation_dict.items():
            name = getattr(op, "name", None)
            display_name = name() if callable(name) else op.__class__.__name__
            symbol_display = getattr(op, "symbol", symbol)
            print(Fore.CYAN + f"- {display_name} ({symbol_display})")
        # Add commands
        commands = ["history", "clear", "undo", "redo", "save", "load", "help", "exit"]
        for cmd in commands:
            print(Fore.CYAN + f"- {cmd} – Command")
        print(Fore.CYAN + "============================\n")