import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    '''
    Main function to load an image, slice it, convert it to greyscale,
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

    zoomed = arr[height_start:slice_height, width_start:slice_width]

    # Convert to grayscale
    zoomed = zoomed.mean(axis=2).astype(int)

    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)

    plt.imshow(zoomed, cmap='gray')
    plt.title("Zoomed Image")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    plt.show()


if __name__ == "__main__":
    main()
