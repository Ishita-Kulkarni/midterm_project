# run_calc.py (in project root)
from app.calculator import Calculator
from app.history import LoggingObserver, AutoSaveObserver
from app.logger import logger
import os

calc = Calculator()
calc.register(LoggingObserver(logger))
if os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true":
    calc.register(AutoSaveObserver())

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def print_help():
    print("Commands: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff, history, clear, undo, redo, save, load, help, exit")

def repl():
    print("Advanced Calculator REPL. Type 'help'.")
    while True:
        try:
            raw = input(">>> ").strip()
            if not raw:
                continue
            parts = raw.split()
            cmd = parts[0].lower()
            if cmd in ("exit", "quit"):
                break
            if cmd == "help":
                print_help(); continue
            if cmd == "history":
                for i, h in enumerate(calc.history):
                    print(i, h)
                continue
            if cmd == "clear":
                calc.history = []; print("History cleared"); continue
            if cmd == "undo":
                calc.undo(); print("Undo done"); continue
            if cmd == "redo":
                calc.redo(); print("Redo done"); continue
            if cmd == "save":
                calc.save_history(); print("Saved"); continue
            if cmd == "load":
                calc.load_history(); print("Loaded"); continue
            # else assume operation
            if len(parts) < 3:
                print("Usage: <operation> <a> <b>"); continue
            a, b = parts[1], parts[2]
            try:
                res = calc.perform(cmd, a, b)
                print(f"= {res.result}")
            except Exception as e:
                print("Error:", e)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
