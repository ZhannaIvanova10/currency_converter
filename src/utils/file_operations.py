"""
Модуль для работы с файлами

Содержит функцию read_json_file для:
- Чтения JSON-файлов
- Валидации структуры данных
- Логирования операций
"""

import json
from pathlib import Path
from typing import Any, Dict, List
from ..loggers import utils_logger


def read_json_file(file_path: Path) -> List[Dict[str, Any]]:
    """
    Читает и валидирует JSON-файл

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        List[Dict[str, Any]]: Список словарей с данными

    Raises:
        FileNotFoundError: Если файл не существует
        json.JSONDecodeError: При ошибках формата JSON
        ValueError: Если данные не соответствуют ожидаемой структуре
    """
    try:
        utils_logger.debug(f"Попытка чтения файла: {file_path}")

        if not file_path.exists():
            error_msg = f"Файл не найден: {file_path}"
            utils_logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                raise json.JSONDecodeError("Файл пуст", doc=content, pos=0)
            data = json.loads(content)

        if not isinstance(data, list):
            error_msg = f"Ожидался список, получен {type(data)}"
            utils_logger.error(error_msg)
            raise ValueError(error_msg)

        utils_logger.info(
            f"Успешно прочитано {
                len(data)} записей из {file_path}")
        return data

    except json.JSONDecodeError as e:
        error_msg = f"Ошибка формата JSON в файле {file_path}: {str(e)}"
        utils_logger.error(error_msg)
        raise
    except Exception as e:
        error_msg = f"Неожиданная ошибка при чтении {file_path}: {str(e)}"
        utils_logger.error(error_msg)
        raise
