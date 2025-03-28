import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def manual_transpose(array):
    """
    Manually transpose a 2D or 3D array.
    If shape is (H, W), we return (W, H).
    If shape in 3D, we transpose only the first two dimensions.
    """
    if len(array.shape) == 2:
        # array is (H, W)
        h, w = array.shape
        # Create an empty transposed array of shape (w, h)
        transposed = [[0]*h for _ in range(w)]
        for i in range(h):
            for j in range(w):
                transposed[j][i] = array[i][j]
        return transposed

    elif len(array.shape) == 3:
        h, w, c = array.shape
        # Empty transposed array of shape (w, h, c)
        transposed = [[[0]*c for _ in range(h)] for _ in range(w)]
        for i in range(h):
            for j in range(w):
                for k in range(c):
                    transposed[j][i][k] = array[i][j][k]
        return transposed
    else:
        raise ValueError("Array must be 2D or 3D to transpose manually.")


def main():
    '''
    Main function to load an image, slice it, convert it to greyscale,
    transpose it manually and plot it.
    '''
    path = "animal.jpeg"
    try:
        arr = ft_load(path)
    except Exception as e:
        print(f"Could not load image: {e}")
        return

    # Slice the image
    height, width, channels = arr.shape
    height_start = height // 5
    width_start = 2 * width // 5
    slice_height = min(height_start + 400, height)
    slice_width = min(width_start + 400, width)

    cut_image = arr[height_start:slice_height, width_start:slice_width]

    # Greyscale
    cut_image = cut_image.mean(axis=2).astype(int)

    print(f"Original shape of cut image: {cut_image.shape}")
    print(cut_image)

    # Manually transpose
    try:
        transposed = manual_transpose(cut_image)
    except ValueError as e:
        print(f"Could not transpose: {e}")
        return

    transposed_array = np.array(transposed)

    print(f"New shape after Transpose: {transposed_array.shape}")
    print(transposed_array)

    plt.imshow(transposed_array, cmap='gray')
    plt.title("Transposed")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    plt.show()


if __name__ == "__main__":
    main()
