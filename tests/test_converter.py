"""
Модуль конфигурации логирования

Содержит функцию setup_logging для настройки:
- Формата логов (время, уровень, сообщение)
- Обработчиков (файл + консоль)
- Уровней логирования (DEBUG, INFO и др.)
"""

# tests/test_converter.py
import unittest
from src.external_api import convert_to_rub

class TestConverter(unittest.TestCase):
    def test_usd_conversion(self):
        transaction = {'amount': 100, 'currency': 'USD'}
        self.assertEqual(convert_to_rub(transaction), 7500.0)
