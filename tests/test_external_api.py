"""
Тесты для модуля external_api
Проверяют корректность конвертации валют
"""

import pytest
from decimal import Decimal
from src.external_api import convert_to_rub

class TestCurrencyConversion:
    """Тесты конвертации валют"""

    def test_usd_conversion(self):
        """Проверка конвертации USD в RUB"""
        assert convert_to_rub({"amount": 100, "currency": "USD"}) == 7500.0

    def test_eur_conversion(self):
        """Проверка конвертации EUR в RUB"""
        assert convert_to_rub({"amount": 50, "currency": "EUR"}) == 4250.0

    def test_rub_conversion(self):
        """Проверка конвертации RUB в RUB"""
        assert convert_to_rub({"amount": 1000, "currency": "RUB"}) == 1000.0

    def test_invalid_currency(self):
        """Проверка обработки неизвестной валюты"""
        with pytest.raises(ValueError):
            convert_to_rub({"amount": 100, "currency": "GBP"})

    def test_missing_fields(self):
        """Проверка обработки отсутствующих полей"""
        with pytest.raises(KeyError):
            convert_to_rub({"amount": 100})  # Нет currency
        with pytest.raises(KeyError):
            convert_to_rub({"currency": "USD"})  # Нет amount

    def test_decimal_precision(self):
        """Проверка точности вычислений с Decimal"""
        result = convert_to_rub({"amount": 100.123, "currency": "USD"})
        assert result == 7509.225
