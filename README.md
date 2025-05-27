
# Auto-Satisfying-TikTok

A Python program to automatically generate satisfying videos for TikTok, YouTube Shorts, and Dailymotion.

## Description

Auto-Satisfying-TikTok is a tool that creates satisfying videos using Pygame to animate a ball trying to escape from multiple circles. The program also overlays the most viewed Twitch clip from the previous day, then generates a video in 720x1080 at 60 FPS that auto-uploads to TikTok, YouTube, and Dailymotion.

## Features

- Generate satisfying videos with Pygame
- Integrate the most viewed Twitch clip from the previous day
- Generate videos in 720x1080 at 60 FPS
- Auto-upload to TikTok, YouTube, and Dailymotion

## Requirements

- Python 3.8 or higher
- FFmpeg (required for video processing)
- Twitch account

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

### Twitch API Credentials

To interact with the Twitch API, you need to set up a `.env` file at the root of the project with your Twitch API credentials. This file should include your `CLIENT_ID` and `CLIENT_SECRET`.

1. Create a `.env` file in the root directory of the project:

   ```plaintext
   CLIENT_ID=your_client_id_here
   CLIENT_SECRET=your_client_secret_here
   ```

2. Obtain your Twitch API credentials:
   - Go to the [Twitch Developer Console](https://dev.twitch.tv/console).
   - Register a new application by clicking on "Register Your Application".
   - Fill in the required details such as the name of your application and the redirect URI (you can use `http://localhost` for local development).
   - Once registered, you will find your `CLIENT_ID` on the application's dashboard.
   - Generate a `CLIENT_SECRET` by clicking on "New Secret" and securely store it.

3. Add the credentials to your `.env` file as shown above.

Ensure that you keep your `.env` file secure and do not share it publicly, as it contains sensitive information.

### Platform Upload Credentials

#### TikTok

To upload videos to TikTok, you need to authenticate using your browser's cookies. This method is used due to TikTok's stricter stance on authentication by a Selenium-controlled browser.

1. Install the [Get cookies.txt LOCALLY](https://github.com/kairi003/Get-cookies.txt-LOCALLY) extension for your browser.

2. Navigate to [TikTok Studio](https://www.tiktok.com/tiktokstudio) and log in to your account.

3. Open the extension by clicking on its icon in the browser's extension menu.

4. Click on "Export As" and save the cookies file as `cookies.txt`.

5. Place the `cookies.txt` file in the `utils` directory of the project. This file will be used to authenticate your session.

#### YouTube and Dailymotion

To upload videos to YouTube and Dailymotion, you need to provide login credentials for each platform. The program uses Selenium for authentication, which requires a simple account with an email and password. **Note:** Two-factor authentication is not supported.

1. Create or use an existing account on each platform (YouTube, Dailymotion) with just an email and password.

2. Add the credentials to your `.env` file at the root of the project. The `.env` file should include the following variables:

   ```plaintext
   YOUTUBE_EMAIL=your_youtube_email_here
   YOUTUBE_PASSWORD=your_youtube_password_here
   DAILYMOTION_EMAIL=your_dailymotion_email_here
   DAILYMOTION_PASSWORD=your_dailymotion_password_here
   ```

3. Ensure that your `.env` file is kept secure and not shared publicly, as it contains sensitive login information.

### Important Notes

- **Security:** Avoid using accounts with sensitive information or those that have two-factor authentication enabled, as Selenium cannot handle two-factor authentication processes.
- **Account Safety:** It is recommended to use separate accounts for automation purposes to avoid potential security risks to your primary accounts.

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

## Credits

This project is inspired by and builds upon the work of [Krokmouuu](https://github.com/Krokmouuu) and their [bouncing-balls](https://github.com/Krokmouuu/bouncing-balls) project. We extend our gratitude for the foundational work that contributed to the development of Auto-Satisfying-TikTok.

Special thanks to [DubiousCode](https://pastebin.com/W5ZsTuET) providing the autorecorder setup used to record the Pygame portion of the project.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Result video 

![video generate](videos/result.gif)