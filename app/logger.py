import logging
from datetime import datetime
from .calculator_config import config
from .calculation import Calculation

class Logger:
    def __init__(self):
        logging.basicConfig(
            filename=config.log_file_path,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('calculator')

    def log_calculation(self, calculation: Calculation):
        """Log a calculation."""
        if config.enable_logging:
            self.logger.info(
                f"Calculation: {calculation.num1} {calculation.operation.symbol} "
                f"{calculation.num2} = {calculation.result}"
            )

    def log_error(self, error_message: str):
        """Log an error."""
        if config.enable_logging:
            self.logger.error(f"Error: {error_message}")