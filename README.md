# Enhanced Calculator

A feature-rich calculator implementation in Python that demonstrates various design patterns and best practices.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Operation history tracking
- Undo/Redo functionality using the Memento pattern
- Configurable logging
- Input validation
- Exception handling
- Environment-based configuration

## Project Structure

```
project_root/
├── app/
│   ├── __init__.py           # Package initialization
│   └── calc.py               # Advanced calculator functionality
│   ├── calculator.py         # Main calculator class
│   ├── calculation.py        # Calculation class
│   ├── calculator_config.py  # Configuration management
│   ├── calculator_memento.py # State management
│   ├── exceptions.py         # Custom exceptions
│   ├── history.py           # Calculation history
│   ├── input_validators.py   # Input validation
│   ├── operations.py        # Operation classes
│   └── logger.py           # Logging functionality
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_calculation.py
│   └── test_operations.py
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The calculator can be configured using environment variables or a `.env` file:

- `CALC_DECIMAL_PRECISION`: Number of decimal places (default: 2)
- `CALC_MAX_HISTORY_SIZE`: Maximum history size (default: 100)
- `CALC_LOG_FILE_PATH`: Log file location (default: calculator.log)
- `CALC_ENABLE_LOGGING`: Enable/disable logging (default: True)

## Running Tests

```bash
pytest tests/
```

## Code Coverage

```bash
coverage run -m pytest
coverage report
```

## License

MIT License