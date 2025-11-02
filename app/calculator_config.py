import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class CalculatorConfig:
    decimal_precision: int = 2
    max_history_size: int = 100
    log_file_path: str = "calculator.log"
    enable_logging: bool = True

    @classmethod
    def from_env(cls) -> 'CalculatorConfig':
        """Create configuration from environment variables."""
        return cls(
            decimal_precision=int(os.getenv('CALC_DECIMAL_PRECISION', 2)),
            max_history_size=int(os.getenv('CALC_MAX_HISTORY_SIZE', 100)),
            log_file_path=os.getenv('CALC_LOG_FILE_PATH', 'calculator.log'),
            enable_logging=bool(os.getenv('CALC_ENABLE_LOGGING', True))
        )

config = CalculatorConfig.from_env()