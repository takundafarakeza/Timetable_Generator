import logging
import os
from logging.handlers import RotatingFileHandler
from .utils import Utils


def get_logger() -> logging.Logger:
    path = Utils.get_log_path()
    os.makedirs(path, exist_ok=True)

    log_file = os.path.join(path, "logs.txt")

    logger_ = logging.getLogger("app")
    logger_.setLevel(logging.DEBUG)

    if not logger_.handlers:
        handler = RotatingFileHandler(
            log_file,
            maxBytes=5_000_000,
            backupCount=5,
            encoding="utf-8"
        )
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger_.addHandler(handler)
        logger_.propagate = False

    return logger_


logger = get_logger()
