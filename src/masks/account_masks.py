"""
Модуль для маскирования банковских реквизитов

Содержит функции:
- mask_card: Маскировка номера карты
- mask_account: Маскировка номера счета
"""

from typing import Optional
from ..loggers import masks_logger


def mask_card(card_number: str) -> Optional[str]:
    """
    Маскирует номер банковской карты (формат: XXXX XX** **** XXXX)

    Args:
        card_number: Номер карты (16+ цифр без пробелов)

    Returns:
        Optional[str]: Замаскированный номер или None при ошибке

    Examples:
        >>> mask_card("1234567812345678")
        "1234 56** **** 5678"
    """
    try:
        masks_logger.debug(f"Начало маскировки карты: {card_number}")

        if (not card_number or len(card_number) < 16
                or not card_number.isdigit()):
            error_msg = (
                f"Неверный номер карты: "
                f"должно быть 16+ цифр, получено: {card_number}"
            )
            masks_logger.error(error_msg)
            return None

        masked = (
            f"{card_number[:4]} {card_number[4:6]}** "
            f"**** {card_number[-4:]}"
        )
        masks_logger.info(f"Успешно замаскирована карта: {masked}")
        return masked

    except Exception as e:
        error_msg = f"Ошибка маскировки карты: {str(e)}"
        masks_logger.error(error_msg)
        return None


def mask_account(account_number: str) -> Optional[str]:
    """
    Маскирует номер счета (формат: **XXXX)

    Args:
        account_number: Номер счета (минимум 4 цифры)

    Returns:
        Optional[str]: Замаскированный номер или None при ошибке

    Examples:
        >>> mask_account("12345678")
        "**5678"
    """
    try:
        masks_logger.debug(f"Начало маскировки счета: {account_number}")

        if (not account_number or len(account_number) < 4
                or not account_number.isdigit()):
            error_msg = (
                f"Неверный номер счета: "
                f"должно быть 4+ цифр, получено: {account_number}"
            )
            masks_logger.error(error_msg)
            return None

        masked = f"**{account_number[-4:]}"
        masks_logger.info(f"Успешно замаскирован счет: {masked}")
        return masked

    except Exception as e:
        error_msg = f"Ошибка маскировки счета: {str(e)}"
        masks_logger.error(error_msg)
        return None
