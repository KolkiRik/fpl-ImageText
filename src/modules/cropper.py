import numpy as np

def get_image_text_fragment(image: np.ndarray, bbox: list[list[float]]) -> np.ndarray:
    """
    Функция вырезает фрагмент из изображения по заданным угловым координатам

    Args:
        image: загруженное изображение в виде numpy-массива формы (высота, ширина, 3).
        bbox: список угловых координат в порядке ЛВ, ПВ, ПН, ЛН.

    Returns:
        numpy-массив формы (высота, ширина, 3) в формате RGB.
    """
    bbox = np.array(bbox, dtype=np.int32)

    x_min, y_min = bbox.min(axis=0)
    x_max, y_max = bbox.max(axis=0)

    return image[y_min:y_max, x_min:x_max]
