import sys
from pathlib import Path

# Добавляем текущую директорию в PYTHONPATH
sys.path.append(str(Path(__file__).parent))

try:
    from src.utils.file_operations import read_json_file
    print("Модуль успешно импортирован!")
    
    try:
        data = read_json_file('data/test.json')
        print("Данные из файла:", data)
    except Exception as e:
        print("Ошибка при чтении файла:", e)
except ImportError as e:
    print("Ошибка импорта:", e)
    print("Текущий PYTHONPATH:", sys.path)
