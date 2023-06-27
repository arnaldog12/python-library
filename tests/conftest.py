"""Conftest.py"""

import numpy as np
import pytest
from numpy.typing import NDArray


@pytest.fixture(scope="session")
def fake_image() -> NDArray[np.uint8]:
    """Creates a fake image."""
    return np.arange(1, 10).reshape(3, 3).astype(np.uint8)  # sem astype, dá erro no mypy
