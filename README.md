
# The Bhagavad Gita Project

This project presents an interactive way to view and study the verses (shlokas) of the Bhagavad Gita. The repository contains Python scripts that extract and render the verses into images, along with support for different platforms (Linux, macOS, Windows).

## Features
- **Shloka Data**: Verses are stored in structured JSON format.
- **Image Generation**: Python script to generate images of the verses.
- **Platform-specific Setup**: Separate scripts for Linux, macOS, and Windows platforms.

## Project Structure
- `data/`: Contains JSON files with shloka data.
- `generate_image.py`: Script to generate shloka images using Pillow.
- `requirements.txt`: Dependencies for the project.
- `.gitignore`: Specifies files to be ignored by git.

## How It Works
1. **Shloka Data**: The project uses a JSON format to store Bhagavad Gita shlokas.
2. **Image Rendering**: `generate_image.py` reads the JSON file and uses the Pillow library to create and save images of the shlokas.
3. **Cross-Platform Support**: The project provides different scripts for running on Linux, macOS, and Windows systems to ensure compatibility.

## Prerequisites
- Python 3.x
- Pillow (Python Imaging Library)

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/abhirai7/The-Bhagavad-Gita-Project.git
cd The-Bhagavad-Gita-Project
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Script
To generate images for shlokas:
```bash
python generate_image.py
```

## Platform-Specific Setup

### Linux
Run the following command to start on Linux:
```bash
python platform-specific/linux.py
```

### macOS
For macOS, use the provided script:
```bash
python platform-specific/macos.py
```

### Windows
For Windows, execute:
```bash
python platform-specific/windows.py
```

## Contributing
Feel free to fork the repository, make updates, and create pull requests to improve the project!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
