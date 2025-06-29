import logging
import os


# Настройка логера
os.makedirs("logs", exist_ok=True)
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

# File handler
handler = logging.FileHandler("logs/utils.log", mode="w")
handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
))
utils_logger.addHandler(handler)


def add_numbers(a, b):
    utils_logger.debug(f"Вызов add_numbers с аргументами: {a}, {b}")
    try:
        result = a + b
        utils_logger.info(f"Успешный результат: {result}")
        return result
    except Exception as e:
        utils_logger.error(f"Ошибка в add_numbers: {e}", exc_info=True)
        raise
