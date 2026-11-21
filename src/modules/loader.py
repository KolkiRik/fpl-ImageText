import numpy as np # 2.5.4
from PIL import Image # 13.0.0

def load_image(path: str) -> np.ndarray:
    """
    Функция открывает изображение по заданному пути и превращает его в массив который numpy может считать

    Параметры:
        path: путь к файлу изображения (PNG, JPG и т.п.).

    Возвращает:
        numpy-массив формы (высота, ширина, 3) в формате RGB.
    """
    image = Image.open(path).convert("RGB")
    return np.array(image)