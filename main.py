#!/usr/bin/env python3
"""
Основной модуль конвертера валют

Обеспечивает:
- Чтение транзакций из JSON-файла
- Конвертацию валют в рубли
- Логирование всех операций
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any

from src.utils import read_json_file
from src.external_api import convert_to_rub
from config import LOG_CONFIG


def setup_logging() -> None:
    """Настройка системы логирования"""
    logging.basicConfig(
        level=LOG_CONFIG['level'],
        format=LOG_CONFIG['format'],
        handlers=[
            logging.FileHandler(LOG_CONFIG['filename'], mode='a'),
            logging.StreamHandler()
        ]
    )


def process_transaction(transaction: Dict[str, Any]) -> str:
    """
    Обработка одной транзакции
    Args:
        transaction: Словарь с данными транзакции
    Returns:
        Строка с результатом конвертации
    Raises:
        ValueError: При ошибках конвертации
    """
    transaction_id = transaction.get('id', 'N/A')
    amount = transaction['amount']
    currency = transaction['currency']

    try:
        amount_rub = convert_to_rub(transaction)
        return f"Транзакция {transaction_id}: {amount:.2f} {currency} = {amount_rub:.2f} RUB"
    except ValueError as e:
        logging.error(f"Ошибка в транзакции {transaction_id}: {str(e)}")
        raise


def main() -> None:
    """Основная функция приложения"""
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        data_file = Path("data/operations.json")
        logger.info(f"Начало обработки файла: {data_file}")

        if not data_file.exists():
            raise FileNotFoundError(f"Файл не найден: {data_file}")

        transactions: List[Dict[str, Any]] = read_json_file(data_file)
        logger.info(f"Прочитано транзакций: {len(transactions)}")

        for transaction in transactions:
            try:
                result = process_transaction(transaction)
                print(result)
                logger.info(result)
            except ValueError:
                continue
            except Exception as e:
                logger.error(f"Необработанная ошибка: {str(e)}")
                continue

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка формата JSON: {str(e)}")
    except Exception as e:
        logger.critical(f"Критическая ошибка: {str(e)}", exc_info=True)
    finally:
        logger.info("Завершение работы программы")


if __name__ == "__main__":
    main()
