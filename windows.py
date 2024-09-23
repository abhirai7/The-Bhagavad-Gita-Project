import ctypes
import os
from generate_image import *

add_text_to_image('image.jpg', 'output_image.jpg')

def change_wallpaper(image_path):
    # Check if the file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    # Absolute path to the image
    absolute_path = os.path.abspath(image_path)

    # Change the wallpaper (SPI_SETDESKWALLPAPER = 20)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 3)

# Example usage
image_path = r'output_image.jpg'  # Replace with the path to your image
change_wallpaper(image_path)
