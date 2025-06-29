import logging
import os
import sys
from logging.handlers import RotatingFileHandler


class UTF8RotatingFileHandler(RotatingFileHandler):
    """Кастомный обработчик с гарантией UTF-8"""

    def __init__(self, filename, **kwargs):
        kwargs.setdefault('encoding', 'utf-8')
        super().__init__(filename, **kwargs)


def setup_logger(name, log_file, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = UTF8RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


os.makedirs("logs", exist_ok=True)
utils_logger = setup_logger("utils", "logs/utils.log")
masks_logger = setup_logger("masks", "logs/masks.log")
