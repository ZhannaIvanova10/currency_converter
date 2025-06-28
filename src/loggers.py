import logging
import os

print("=== Инициализация логеров ===")  # Добавьте эту строку

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("logs/debug.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logger.info("Тестовое сообщение")

# Создаем папку logs при импорте
os.makedirs("logs", exist_ok=True)

# Логер для utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Настройка файлового обработчика
utils_handler = logging.FileHandler("logs/utils.log")
utils_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)

# Логер для masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
masks_handler = logging.FileHandler("logs/masks.log")
masks_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
masks_logger.addHandler(masks_handler)
