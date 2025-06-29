"""
Модуль для конвертации валют в рубли

Содержит:
- Функцию convert_to_rub для пересчета сумм
- Поддержку основных валют (USD, EUR, RUB)
- Логирование операций конвертации
"""

from typing import Dict, Any
from decimal import Decimal
from src.loggers import utils_logger


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли по текущему курсу

    Args:
        transaction: Словарь с ключами:
            - amount: float - сумма
            - currency: str - код валюты (USD, EUR, RUB)

    Returns:
        float: Сумма в рублях

    Raises:
        ValueError: При неизвестной валюте или нечисловой сумме
        KeyError: Если отсутствуют обязательные поля

    Example:
        >>> convert_to_rub({"amount": 100, "currency": "USD"})
        7500.0
    """
    try:
        amount = Decimal(str(transaction["amount"]))
        currency = transaction["currency"].upper()

        utils_logger.debug(f"Конвертация: {amount} {currency} -> RUB")

        rates = {
            "USD": Decimal("75.0"),
            "EUR": Decimal("85.0"),
            "RUB": Decimal("1.0")}

        if currency not in rates:
            raise ValueError(f"Неизвестная валюта: {currency}")

        result = float(amount * rates[currency])
        utils_logger.info(
            f"Успешная конвертация: {amount} {currency} = {result} RUB")
        return result

    except (KeyError, ValueError) as e:
        utils_logger.error(f"Ошибка конвертации: {str(e)}")
        raise
    except Exception as e:
        utils_logger.critical(f"Критическая ошибка: {str(e)}")
        raise
