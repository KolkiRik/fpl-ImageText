import cv2
import numpy as np


def glyph_similarity(crop_gray, rendered) -> float:
    """Возвращает меру схожести нарисованного изображения и эталона."""
    c = cv2.normalize(crop_gray, None, 0, 255, cv2.NORM_MINMAX)
    c = (c > 127).astype(np.uint8)
    r = (rendered > 127).astype(np.uint8)
    try:
        inter = (c & r).sum()
        union = (c | r).sum()
        return inter / union if union else 0.0
    except ValueError:
        return 0.0  # ЗАТЫЧКА против разноразмерных вырезок, исправим позже!
