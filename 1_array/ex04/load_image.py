import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path, prints its shape, prints its pixels,
    and returns the pixel data as a NumPy array.
    Only JPG/JPEG are supported by default.

    :param path: path to the image
    :return: NumPy array of shape (height, width, channels)
    :raises ValueError: if file format is not .jpg or .jpeg
    :raises FileNotFoundError: if the file does not exist
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File '{path}' does not exist.")

    # Check extension
    _, ext = os.path.splitext(path)
    ext = ext.lower()
    if ext not in [".jpg", ".jpeg"]:
        raise ValueError(f"Unsupported file format '{ext}'. ")

    # Load the image using PIL
    with Image.open(path) as img:
        # Convert to RGB if needed
        img = img.convert("RGB")
        arr = np.array(img)

    print(f"The shape of image is: {arr.shape}")
    print(arr)
    return arr
