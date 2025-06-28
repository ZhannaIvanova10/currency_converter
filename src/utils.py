import logging

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Уровень DEBUG или выше

# Создаём FileHandler (пишет логи в файл)
file_handler = logging.FileHandler("utils.log", mode="a")  # 'a' - дозапись
file_handler.setLevel(logging.DEBUG)

# Форматирование логов
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

# Пример функции с логированием
def add_numbers(a, b):
    try:
        logger.debug(f"Сложение чисел: {a} + {b}")
        result = a + b
        logger.info(f"Результат: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка: {e}", exc_info=True)
        return None
