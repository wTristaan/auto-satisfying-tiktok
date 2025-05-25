
# Auto-Satisfying-TikTok

A Python program to automatically generate satisfying videos for TikTok, YouTube Shorts, and Dailymotion.

## Description

Auto-Satisfying-TikTok is a tool that creates satisfying videos using Pygame to animate a ball trying to escape from multiple circles. The program also overlays the most viewed Twitch clip from the previous day, then generates a video in 720x1080 at 60 FPS that auto-uploads to TikTok, YouTube, and Dailymotion.

## Features

- Generate satisfying videos with Pygame
- Integrate the most viewed Twitch clip from the previous day
- Generate videos in 720x1080 at 60 FPS
- Auto-upload to TikTok, YouTube, and Dailymotion

Sure, here is the revised "Requirements" section for your README file in Markdown format:

## Requirements

- Python 3.8 or higher
- FFmpeg (required for video processing)

### Installing FFmpeg

FFmpeg is required for video processing. You can download and install it from [FFmpeg's official website](https://ffmpeg.org/download.html).

#### Windows
1. Download the FFmpeg build from [this link](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the downloaded ZIP file to a folder of your choice.
3. Add the `bin` folder to your system PATH:
   - Right-click on 'This PC' or 'Computer' on the desktop or in File Explorer.
   - Click on 'Properties' > 'Advanced system settings' > 'Environment Variables'.
   - Under 'System Variables', find the 'Path' variable, select it, and click 'Edit'.
   - Click 'New' and add the path to the `bin` folder inside the extracted FFmpeg folder.
   - Click 'OK' to close all dialog boxes.
4. Verify the installation by opening Command Prompt and typing `ffmpeg -version`.

#### Linux
1. Open a terminal.
2. Use your package manager to install FFmpeg:
   - For Debian-based distributions (e.g., Ubuntu):
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
   - For Red Hat-based distributions (e.g., Fedora):
     ```bash
     sudo dnf install ffmpeg
     ```
3. Verify the installation by typing `ffmpeg -version` in the terminal.

#### macOS
1. Open Terminal.
2. Install FFmpeg using Homebrew:
   ```bash
   brew install ffmpeg
   ```
3. Verify the installation by typing `ffmpeg -version` in the terminal.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wTristaan/auto-satisfying-tiktok.git
   ```

2. Navigate to the project directory:

   ```bash
   cd auto-satisfying-tiktok
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Configure the necessary parameters in the `config.json` file.

2. Run the main script:

   ```bash
   python main.py
   ```

3. The program will automatically generate the video and upload it to the specified platforms.

## Configuration

The `config.json` file contains the configuration parameters for the program. Here is an example configuration:

## Credits

This project is inspired by and builds upon the work of [Krokmouuu](https://github.com/Krokmouuu) and their [bouncing-balls](https://github.com/Krokmouuu/bouncing-balls) project. We extend our gratitude for the foundational work that contributed to the development of Auto-Satisfying-TikTok.

Special thanks to [DubiousCode](https://pastebin.com/W5ZsTuET) providing the autorecorder setup used to record the Pygame portion of the project.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.