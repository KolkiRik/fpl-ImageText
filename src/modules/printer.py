import numpy as np # 2.5.4
from PIL import Image, ImageDraw, ImageFont # 13.0.0

def render_text(text: str, font_path: str, size: int, target_w: int, target_h: int)  -> np.ndarray:
    """
    Функция создаёт новое изображение текста с заданным шрифтом и возвращает его в виде массива numpy

    Args:
        text: печатаемый текст.
        font_path: путь к файлу шрифта (TTF).
        size: кегль шрифта.
        target_w: итоговая ширина изображения.
        target_h: итоговая высота изображения.

    Returns:
        numpy-массив формы (высота, ширина, 3) в формате RGB (?).
    """
    img = Image.new('RGB', (target_w * 3, target_h * 3), (255, 255, 255))
    # изменить RGB на L, когда научимся переводить распознаваемое изображение в градации серого
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, fill=255, font=ImageFont.truetype(font_path, size))
    img = img.resize((target_w, target_h))
    return np.array(img)
