from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    "masks.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8"
)

def setup_logger(name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Использование:
logger = setup_logger(__name__, "utils.log")