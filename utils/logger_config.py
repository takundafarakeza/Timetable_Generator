import logging
import os
from .utils import Utils
from logging.handlers import RotatingFileHandler

PATH = Utils.get_log_path()
LOG_FILE = os.path.join(PATH, "logs.txt")
open(LOG_FILE, "w").close()

handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5_000_000,
    backupCount=5
)

log_formatter = logging.Formatter("%(asctime)s | %(levelname)s | "
                                  "%(message)s")
handler.setFormatter(log_formatter)
logging.basicConfig(level=logging.DEBUG,
                    handlers=[handler])
logger = logging.getLogger("app")
