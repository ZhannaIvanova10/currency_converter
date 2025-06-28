"""
Модуль utils - вспомогательные функции

Экспортирует:
- read_json_file: Чтение JSON-файлов
- utils_logger: Логгер модуля
"""

from .file_operations import read_json_file
from ..loggers import utils_logger

__all__ = ["read_json_file", "utils_logger"]

def test_logging():
    """Тестовая функция для проверки логирования"""
    from src.loggers import utils_logger
    utils_logger.debug("Тест логирования из utils")
    return "Логирование работает"
