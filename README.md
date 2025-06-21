
# Auto-Satisfying-TikTok

A Python program to automatically generate satisfying videos for TikTok, YouTube Shorts, and Dailymotion.

## Description

Auto-Satisfying-TikTok is a tool that creates satisfying videos using Pygame to animate a ball trying to escape from multiple circles. The program also overlays the most viewed Twitch clip from the previous day, then generates a video in 1080x1920 at 60 FPS that auto-uploads to TikTok, YouTube, and Dailymotion.

## Features

- Generate satisfying videos with Pygame
- Integrate the most viewed Twitch clip from the previous day
- Generate videos in 1080x1920 at 60 FPS
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

### TikTok

To upload videos to TikTok, you need to authenticate using your browser's cookies. This method is used due to TikTok's stricter stance on authentication by a Selenium-controlled browser.

1. Install the [Get cookies.txt LOCALLY](https://github.com/kairi003/Get-cookies.txt-LOCALLY) extension for your browser.

2. Navigate to [TikTok Studio](https://www.tiktok.com/tiktokstudio) and log in to your account.

3. Open the extension by clicking on its icon in the browser's extension menu.

4. Click on "Export As" and save the cookies file as `cookies_EN.txt`.

5. Place the `cookies.txt` file in the `utils` directory of the project. This file will be used to authenticate your session.


### YouTube API Credentials

To upload videos to YouTube using the YouTube Data API v3, you need to set up API credentials and authenticate with Google. Follow these steps to set up your project and obtain the necessary credentials:

1. **Go to the Google Developers Console:**
   - Navigate to the [Google Developers Console](https://console.cloud.google.com/).

2. **Create a New Project:**
   - Click on the project dropdown near the top left of the page.
   - Select "New Project" and follow the prompts to create a new project.

3. **Enable the YouTube Data API v3:**
   - In the Google Developers Console, go to the "Library" section.
   - Search for "YouTube Data API v3" and select it.
   - Click on the "Enable" button to enable the API for your project.

4. **Create OAuth 2.0 Credentials:**
   - Go to the "Credentials" section in the Google Developers Console.
   - Click on "Create Credentials" and select "OAuth client ID."
   - Choose "Desktop app" as the application type.
   - Provide a name for your OAuth 2.0 client and click "Create."

5. **Download the Credentials File:**
   - After creating the OAuth 2.0 credentials, click on the download button to download the credentials as a JSON file.
   - Rename the downloaded JSON file to `yt_api.json`.
   - Place the `yt_api.json` file in the `utils` directory of the project.

6. **Authenticate and Obtain the Token:**
   - When you run the program for the first time, it will prompt you to authenticate with your Google account.
   - Follow the authentication link provided in the console and log in with your Google account.
   - After successful authentication, you will receive an authentication token. This token will be saved for future use, so you won't need to authenticate again for subsequent runs.

Ensure that you keep your `yt_api.json` file secure and do not share it publicly, as it contains sensitive information.

For more detailed instructions, you can refer to the [YouTube Data API v3 documentation](https://developers.google.com/youtube/v3/getting-started).

### Dailymotion API Credentials

To upload videos to Dailymotion using their API, you need to set up a `.env` file at the root of the project with your Dailymotion API credentials. This file should include your `DAILYMOTION_EMAIL`, `DAILYMOTION_PASSWORD`, `DAILYMOTION_API_KEY`, `DAILYMOTION_API_SECRET`, and `DAILYMOTION_ID`.

1. Create a `.env` file in the root directory of the project:

   ```plaintext
   DAILYMOTION_EMAIL=your_dailymotion_email_here
   DAILYMOTION_PASSWORD=your_dailymotion_password_here
   DAILYMOTION_API_KEY=your_dailymotion_api_key_here
   DAILYMOTION_API_SECRET=your_dailymotion_api_secret_here
   DAILYMOTION_ID=your_dailymotion_id_here
   ```

2. Obtain your Dailymotion API credentials:
   - Go to the [Dailymotion Partner Portal](https://www.dailymotion.com/partner/).
   - You need to be a partner to create an API key. If you are not already a partner, you will need to apply for the partnership.
   - Once you are a partner, navigate to the API section to create a new API key.
   - Generate your `DAILYMOTION_API_KEY` and `DAILYMOTION_API_SECRET` and securely store them.

3. Obtain your `DAILYMOTION_ID`:
   - Log in to the [Dailymotion Partner Portal](https://www.dailymotion.com/partner/).
   - The `DAILYMOTION_ID` can be found in the URL when you are logged in. It is typically a part of the URL path after logging in.

4. Add the credentials to your `.env` file as shown above.

Ensure that you keep your `.env` file secure and do not share it publicly, as it contains sensitive information.

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

1. Configure the necessary parameters in the `.env` file.

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

## Google Drive Branch

In an effort to automate the video generation and upload process, I initially attempted to run the script on a server. However, TikTok detected the change in IP address associated with my account, which resulted in the videos no longer being promoted effectively. This led to a shadow ban, reducing the visibility of the uploaded content.

To address this issue, I created the `google-drive` branch. This branch modifies the script to upload the generated videos to a specified Google Drive folder instead of directly uploading them to TikTok, YouTube, and Dailymotion. By doing so, users can manually upload the videos from Google Drive to the respective platforms, thereby avoiding potential shadow bans due to IP changes.

### Setup Instructions for Google Drive

1. **Activate Google Drive API:**
   - Users need to activate the Google Drive API in the Google Cloud Console. This can be done using the same project setup for the YouTube API, simplifying the process.

2. **Configure `.env` File:**
   - Add the ID of your base Google Drive folder to the `.env` file. This folder will be used to store the generated videos.
   - Example entry in `.env`:
     ```plaintext
     GDRIVE_FOLDER_ID=your_google_drive_folder_id_here
     ```

3. **Use Existing Credentials:**
   - If you have already set up credentials for the YouTube API, you can use the same `credentials.json` file for Google Drive API access. Ensure that the Google Drive API is enabled under the same project in the Google Cloud Console.

By following these steps, users can generate and store videos in their Google Drive, allowing for manual uploads to social media platforms and avoiding the issues associated with automated server uploads.

## Result video 

![video generate](exemple/exemple.mp4)