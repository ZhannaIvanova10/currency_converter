from src.external_api import convert_to_rub
from src.utils import read_json_file
import logging


def test_conversion():
    """Проверка работы функции конвертации."""
    try:
        # Тестовая транзакция
        test_transaction = {
            "id": "test_1",
            "amount": 100,
            "currency": "USD"
        }

        result = convert_to_rub(test_transaction)
        logging.info(f"Тестовая конвертация: 100 USD = {result} RUB")
        print("Функция convert_to_rub работает корректно!")
        return True
    except Exception as e:
        logging.error(f"Ошибка в функции convert_to_rub: {str(e)}")
        print(f"Обнаружена ошибка: {str(e)}")
        return False


if __name__ == "__main__":
    test_conversion()