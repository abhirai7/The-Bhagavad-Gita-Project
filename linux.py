import os
import subprocess
from generate_image import *

add_text_to_image('image.jpg', 'output_image.jpg')


def change_wallpaper(image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    absolute_path = os.path.abspath(image_path)
    file_uri = f'file://{absolute_path}'


    try:
        subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', file_uri], check=True)
        print("Wallpaper changed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Example usage
image_path = 'output_image.jpg'  # Replace with the path to your image
change_wallpaper(image_path)
