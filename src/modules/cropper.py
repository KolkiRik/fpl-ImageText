import numpy as np

def get_image_text_fragment(image, bbox):
    bbox = np.array(bbox, dtype=np.int32)

    x_min, y_min = bbox.min(axis=0)
    x_max, y_max = bbox.max(axis=0)

    return image[y_min:y_max, x_min:x_max]
