"""
Модуль конфигурации логирования

Содержит функцию setup_logging для настройки:
- Формата логов (время, уровень, сообщение)
- Обработчиков (файл + консоль)
- Уровней логирования (DEBUG, INFO и др.)
"""

import logging
from pathlib import Path


def setup_logging(logger_name: str, log_file: str) -> logging.Logger:
    """Настройка логгера с записью в файл"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(
        filename=log_dir / log_file, mode="w", encoding="utf-8"
    )
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
