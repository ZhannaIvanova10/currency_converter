"""
Тесты для модуля utils.file_operations
Проверяют корректность чтения JSON-файлов
"""

import pytest
import json
from pathlib import Path
from src.utils import read_json_file

class TestFileOperations:
    """Тесты для работы с файлами"""

    def test_read_valid_file(self, tmp_path):
        """Проверка чтения валидного JSON-файла"""
        test_file = tmp_path / "test.json"
        test_file.write_text('[{"id": 1, "amount": 100}]')

        result = read_json_file(test_file)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["id"] == 1

    def test_file_not_found(self):
        """Проверка обработки отсутствующего файла"""
        with pytest.raises(FileNotFoundError):
            read_json_file(Path("nonexistent.json"))

    def test_invalid_json(self, tmp_path):
        """Проверка обработки невалидного JSON"""
        test_file = tmp_path / "invalid.json"
        test_file.write_text('{"invalid": json')  # Намеренно некорректный JSON

        with pytest.raises(json.JSONDecodeError):
            read_json_file(test_file)

    def test_empty_file(self, tmp_path):
        """Проверка обработки пустого файла"""
        test_file = tmp_path / "empty.json"
        test_file.write_text('')

        with pytest.raises(json.JSONDecodeError):
            read_json_file(test_file)
