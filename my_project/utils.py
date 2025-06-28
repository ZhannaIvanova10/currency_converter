import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("utils.log", encoding="utf-8", mode="a")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def add_numbers(a, b):
    try:
        logger.debug(f"Сложение чисел: {a} + {b}")
        return float(a) + float(b)
    except ValueError as e:
        logger.error(f"Некорректные данные: {e}")
        return None
    except TypeError as e:
        logger.error(f"Несовместимые типы: {e}", exc_info=True)
        return None
