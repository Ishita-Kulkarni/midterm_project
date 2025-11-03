import pandas as pd
from app.calculator import Calculator
from app.operations import get_operation
from app.exceptions import OperationError, DivisionByZeroError
from colorama import init, Fore, Style

init(autoreset=True)  # Automatically reset color after each print

HISTORY_FILE = "calc_history.csv"


# Dynamic Help Menu using Decorator Pattern
class HelpDecorator:
    """Generate dynamic help menu with color-coded outputs."""
    def __init__(self, operation_dict):
        self.operation_dict = operation_dict

    def show_help(self):
        print(Fore.CYAN + "\n=== Calculator Help Menu ===")
        for symbol, op in self.operation_dict.items():
            name = getattr(op, "name", None)
            display_name = name() if callable(name) else op.__class__.__name__
            symbol_display = getattr(op, "symbol", symbol)
            print(Fore.CYAN + f"- {display_name} ({symbol_display})")
        # Add other commands
        commands = ["history", "clear", "undo", "redo", "save", "load", "help", "exit"]
        for cmd in commands:
            print(Fore.CYAN + f"- {cmd} – Command")
        print(Fore.CYAN + "============================\n")


def main():
    calc = Calculator()

    # Step 1: Build operation dictionary
    operation_dict = {
        "add": get_operation("add"),
        "subtract": get_operation("subtract"),
        "multiply": get_operation("multiply"),
        "divide": get_operation("divide"),
        "power": get_operation("power"),
        "root": get_operation("root"),
        "modulus": get_operation("modulus"),
        "int_divide": get_operation("int_divide"),
        "percent": get_operation("percent"),
        "abs_diff": get_operation("abs_diff"),
    }

    # Step 2: Create dynamic help menu
    help_menu = HelpDecorator(operation_dict)

    print(Fore.YELLOW + "Welcome to the Enhanced Calculator REPL!")
    print(Fore.YELLOW + "Type 'help' for available commands.\n")

    while True:
        try:
            user_input = input(Fore.YELLOW + ">>> " + Style.RESET_ALL).strip()
            if not user_input:
                continue

            # Commands
            cmd = user_input.lower()
            if cmd == "exit":
                print(Fore.YELLOW + "Exiting calculator. Goodbye!")
                break
            elif cmd == "help":
                help_menu.show_help()
                continue
            elif cmd == "history":
                if not calc.history:
                    print(Fore.CYAN + "History is empty.")
                else:
                    for i, entry in enumerate(calc.history, 1):
                        print(Fore.CYAN + f"{i}: {entry.execute()}")
                continue
            elif cmd == "clear":
                calc.clear_history()
                print(Fore.CYAN + "History cleared.")
                continue
            elif cmd == "undo":
                calc.undo()
                print(Fore.CYAN + "Last calculation undone.")
                continue
            elif cmd == "redo":
                calc.redo()
                print(Fore.CYAN + "Last undone calculation redone.")
                continue
            elif cmd == "save":
                if calc.history:
                    data = [{"operation": type(entry.operation).__name__,
                             "a": entry.a, "b": entry.b,
                             "result": entry.execute()} for entry in calc.history]
                    df = pd.DataFrame(data)
                    df.to_csv(HISTORY_FILE, index=False)
                    print(Fore.CYAN + f"History saved to {HISTORY_FILE}")
                else:
                    print(Fore.CYAN + "No history to save.")
                continue
            elif cmd == "load":
                try:
                    df = pd.read_csv(HISTORY_FILE)
                    calc.history.clear()
                    for _, row in df.iterrows():
                        op = get_operation(row["operation"].lower())
                        if op:
                            calc.history.append(calc.create_calculation(row["a"], row["b"], op))
                    print(Fore.CYAN + f"Loaded {len(calc.history)} entries from {HISTORY_FILE}")
                except FileNotFoundError:
                    print(Fore.RED + f"No file found at {HISTORY_FILE}")
                continue

            # Handle calculations: <operation> <num1> <num2>
            parts = user_input.split()
            if len(parts) != 3:
                print(Fore.RED + "Invalid input. Format: <operation> <num1> <num2>")
                continue

            op_name, a_str, b_str = parts
            a, b = float(a_str), float(b_str)

            operation = operation_dict.get(op_name)
            if not operation:
                print(Fore.RED + f"Unknown operation '{op_name}'. Type 'help' for commands.")
                continue

            result = calc.calculate(a, b, operation)
            print(Fore.GREEN + f"Result: {result}")

        except (OperationError, DivisionByZeroError) as e:
            print(Fore.RED + f"Operation Error: {e}")
        except ValueError:
            print(Fore.RED + "Invalid numbers. Please enter numeric values.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")


if __name__ == "__main__":
    main()
