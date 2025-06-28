from utils import add_numbers
from masks import mask_card

add_numbers(5, 3)            # Успешный случай
add_numbers("5", 3)          # Ошибка (TypeError)

mask_card("1234567890123456")  # Успешное маскирование
mask_card(12345)              # Ошибка (AttributeError)
