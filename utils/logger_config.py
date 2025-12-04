import logging
import os.path as path
from .utils import Utils
from logging.handlers import RotatingFileHandler

LOG_FILE = path.join(Utils.get_appdata_path(), "logs", "logs.txt")
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
