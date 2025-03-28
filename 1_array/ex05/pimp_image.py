import numpy as np
import matplotlib.pyplot as plt


def plot_image(array: np.ndarray) -> None:
    """
    Plots the image.
    """
    plt.imshow(array)
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received with: new_pixel = 255 - old_pixel.
    """
    inverted = np.copy(array)
    inverted = 255 - inverted
    plot_image(inverted)
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel.
    """
    red = np.copy(array)
    # Zero out G and B by multiplying them by 0
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    plot_image(red)
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel.
    """
    green = np.copy(array)
    # Zero out R
    green[:, :, 0] = 0
    # Zero out B
    green[:, :, 2] = 0
    plot_image(green)
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel.
    """
    blue = np.copy(array)
    # Zero out R
    blue[:, :, 0] = 0
    # Zero out G
    blue[:, :, 1] = 0
    plot_image(blue)
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    grey = np.copy(array)
    avg = grey.mean(axis=2)
    for c in range(3):
        grey[:, :, c] = avg
    plot_image(grey)
    return grey
