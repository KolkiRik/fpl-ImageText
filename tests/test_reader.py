
import sys
from unittest.mock import Mock

# Подменяем EasyOCR
sys.modules["easyocr"] = Mock()

from modules.reader import Reader, TextBlock


def test_text_block():
    block = TextBlock(text="Привет", confidence=0.95)

    assert block.text == "Привет"
    assert block.confidence == 0.95


def test_reader_recognize():
    reader = Reader.__new__(Reader)

    fake_model = Mock()
    fake_model.readtext.return_value = [
        (None, "Привет", 0.95),
        (None, "Мир", 0.85)
    ]

    reader.model = fake_model

    result = reader.recognize(image="fake_image")

    assert len(result) == 2
    assert result[0].text == "Привет"
    assert result[0].confidence == 0.95
    assert result[1].text == "Мир"
    assert result[1].confidence == 0.85

    fake_model.readtext.assert_called_once_with("fake_image")
