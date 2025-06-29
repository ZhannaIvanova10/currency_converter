import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("masks.log", encoding="utf-8", mode="a")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card(card_number: str) -> str:
    try:
        logger.debug(f"Маскирование карты: {card_number}")
        return f"{card_number[:4]} **** **** {card_number[-4:]}"
    except Exception as e:
        logger.error(f"Ошибка: {e}", exc_info=True)
        return "Ошибка"
