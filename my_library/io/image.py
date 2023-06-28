"""Load module"""

import numpy as np
from numpy.typing import NDArray
from PIL import Image


def load_image(path: str) -> NDArray[np.uint8]:
    """Loag image as grayscale

    Args:
        path (str): image path

    Returns:
        NDArray[np.uint8]: image as numpy array
    """
    image = Image.open(path)
    image = image.convert("L")
    return np.asarray(image, dtype=np.uint8)


def save_image(np_array: NDArray[np.uint8], path: str) -> None:
    """Save np_array as image file

    Args:
        np_array (NDArray[np.uint8]): image as numpy array
        path (str): image path
    """
    image = Image.fromarray(np_array)
    image.save(path)
