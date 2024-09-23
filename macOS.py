import subprocess
import os

def change_wallpaper(image_path):
    # Check if the file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    # Absolute path to the image
    absolute_path = os.path.abspath(image_path)

    # Command to change wallpaper
    script = f"""
    osascript -e 'tell application "System Events"
        set desktopImage to "{absolute_path}"
        set picture of every desktop to POSIX file desktopImage
    end tell'
    """
    subprocess.run(script, shell=True, check=True)

# Example usage
image_path = '/path/to/your/image.jpg'  # Replace with the path to your image
change_wallpaper(image_path)
