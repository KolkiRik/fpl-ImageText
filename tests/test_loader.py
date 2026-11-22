import numpy as np
from PIL import Image

from modules.loader import load_image


def test_load_image(tmp_path):
    image_path = tmp_path / "test.png"

    image = Image.new("RGB", (20, 10), color=(255, 0, 0))
    image.save(image_path)

    result = load_image(image_path)

    assert isinstance(result, np.ndarray)
    assert result.shape == (10, 20, 3)
    assert np.all(result[0, 0] == [255, 0, 0])