"""Test Operations."""

import numpy as np
import pytest
from numpy.typing import NDArray

from my_library.cv.operations import bright

im_test = np.array([[1, 2], [3, 4]])


@pytest.mark.parametrize(
    "image, value, expected",
    [
        (im_test, 10, np.array([[11, 12], [13, 14]])),
        (im_test, 100, np.array([[101, 102], [103, 104]])),
        (im_test, 300, np.array([[255, 255], [255, 255]])),
        (im_test, -300, np.array([[0, 0], [0, 0]])),
        (im_test, -1, np.array([[0, 1], [2, 3]])),
    ],
)
def test_bright(image: NDArray[np.uint8], value: int, expected: NDArray[np.uint8]) -> None:
    """Test bright with parameters."""
    assert np.allclose(bright(image, value), expected)


def test_bright_with_fake_image(fake_image: NDArray[np.uint8]) -> None:
    """Test bright with fake image."""
    res = bright(fake_image, 250)

    assert np.min(res) == 251
    assert np.max(res) == 255
