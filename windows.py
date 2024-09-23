import ctypes
import os

def change_wallpaper(image_path):
    # Check if the file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    # Absolute path to the image
    absolute_path = os.path.abspath(image_path)

    # Change the wallpaper (SPI_SETDESKWALLPAPER = 20)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 3)

# Example usage
image_path = r'C:\path\to\your\image.jpg'  # Replace with the path to your image
change_wallpaper(image_path)
