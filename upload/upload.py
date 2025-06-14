from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tiktok_uploader.upload import upload_video
from utils.params import DAILYMOTION_EMAIL, DAILYMOTION_PASSWORD, DAILYMOTION_API_KEY, DAILYMOTION_API_SECRET, DAILYMOTION_ID
from dailymotion_app.api import Dailymotion
from youtube_app.api import YTApi


class Upload():
    def __init__(self, video_to_upload_path, rich_console, LANGUAGE):
        self.video_path = video_to_upload_path
        self.title_video = self.video_path.replace("_", " ").replace(".mp4", "")
        self.tags = "#clip #twitch #funny #compilation #satisfyingvideo"
        self.full_title = f"{self.title_video} - Twitch clips compilation ! {self.tags}" 
        self.full_title_without_tags = f"{self.title_video} - Twitch clips compilation !" 
        self.rich_console = rich_console
        self.LANGUAGE = LANGUAGE

    def tiktok(self):
        try:
            self.rich_console.log("Uploading video to tiktok.")
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            
            upload_video(self.video_path, self.full_title, cookies=f'utils/cookies_{self.LANGUAGE.upper()}.txt', headless=True, browser_agent=driver)
            self.rich_console.log("Upload video to tiktok done.")
        except Exception as e:
            self.rich_console.log(f"Upload video to tiktok error {str(e)}.")


    def youtube(self):
        try:
            self.rich_console.log("Uploading video to youtube.")
            youtube = YTApi()
            youtube.upload(self.video_path, self.full_title_without_tags, self.tags, 24)
            self.rich_console.log("Upload video to youtube done.")
        except Exception as e:
            self.rich_console.log(f"Upload video to youtube error {str(e)}.")


    def daylimotion(self):
        try:
            self.rich_console.log("Uploading video to dailymotion.")
            Dailymotion(
                DAILYMOTION_EMAIL, 
                DAILYMOTION_PASSWORD, 
                DAILYMOTION_API_KEY, 
                DAILYMOTION_API_SECRET, 
                DAILYMOTION_ID,
                self.video_path,
            ).upload(self.full_title)
            self.rich_console.log("Upload video to dailymotion done.")
        except Exception as e:
            self.rich_console.log(f"Upload video to dailymotion error {str(e)}.")
