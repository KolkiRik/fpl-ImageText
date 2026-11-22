import easyocr # 1.7.2
from pydantic import BaseModel


class TextBlock(BaseModel):
    """
    Класс одного распознонного текста
    
    Аттрибуты:
        box_coords: координаты фрагмента, в котором был найден текст (левая верхняя, правая верхняя, правая нижняя, левая нижняя)
        text: распознанный текст (строка)
        confidence: уверенность модели в правильности прочитанного текста (от 0 до 1)
    """
    box_coords: list[list[float]]
    text: str
    confidence: float


class Reader:
    """
    Класс модели EasyOCR - считывание текста
    """
    def __init__(self):
        # Загрузка модели один раз в конструкторе, сэкономить время и память.
        self.model = easyocr.Reader(["en", "ru"], gpu=False) # gpu=False - будем работать на CPU

    def recognize(self, image) -> list[TextBlock]:
        """
        Функция распознования текста на изображении.

        Параметры:
            image: numpy-массив RGB, полученный из load_image().

        Возвращает:
            Список TextBlock — по одному на каждый найденный фрагмент.
        """
        raw_text = self.model.readtext(image)
        return [TextBlock(box_coords = raw_b, text=raw_t, confidence=float(raw_c)) for raw_b, raw_t, raw_c in raw_text]