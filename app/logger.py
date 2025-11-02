# app/logger.py
import logging
import os
from dotenv import load_dotenv

load_dotenv()
LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "./logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, os.getenv("CALCULATOR_LOG_FILE", "calculator.log"))

logger = logging.getLogger("calc")
logger.setLevel(logging.INFO)
fh = logging.FileHandler(LOG_FILE, encoding=os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8"))
fmt = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
fh.setFormatter(fmt)
logger.addHandler(fh)
