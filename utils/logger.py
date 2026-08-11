import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "api_test.log")


def get_logger(name):

    logger = logging.getLogger(name)

    if not logger.handlers:

        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
