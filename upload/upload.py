import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tiktok_uploader.upload import upload_video
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.params import YOUTUBE_EMAIL, YOUTUBE_PASSWORD, DAILYMOTION_EMAIL, DAILYMOTION_PASSWORD, DAILYMOTION_API_KEY, DAILYMOTION_API_SECRET, DAILYMOTION_ID
from dailymotion_app.api import Dailymotion


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
            upload_video(self.video_path, self.full_title, cookies=f'utils/cookies_{self.LANGUAGE.upper()}.txt', headless=True)
            self.rich_console.log("Upload video to tiktok done.")
        except Exception as e:
            self.rich_console.log(f"Upload video to tiktok error {str(e)}.")


    def youtube(self):
        try:
            self.rich_console.log("Uploading video to youtube.")
            
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://studio.youtube.com")
            time.sleep(10)

            driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys(YOUTUBE_EMAIL)
            driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys(YOUTUBE_PASSWORD)
            driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='create-icon']/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]").click()
            driver.find_element(By.XPATH, "//*[@id='text-item-0']").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='content']/input").send_keys(os.path.abspath(self.video_path))
            time.sleep(10)

            input_title = driver.find_element(By.XPATH, "//*[@id='textbox']")
            input_title.clear()
            if len(self.full_title_without_tags) > 100:
                self.full_title_without_tags = self.full_title_without_tags[0: 90]
            input_title.send_keys(self.full_title_without_tags)
            time.sleep(2)

            driver.find_elements(By.XPATH, "//*[@id='radioContainer']")[1].click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='toggle-button']/ytcp-button-shape/button").click()
            time.sleep(10)

            driver.find_element(By.XPATH, "//*[@id='text-input']").send_keys(self.tags.replace(" ", ", "))
            time.sleep(10)

            driver.find_element(By.XPATH, "//*[@id='next-button']/ytcp-button-shape/button").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id='next-button']/ytcp-button-shape/button").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id='next-button']/ytcp-button-shape/button").click()
            time.sleep(2)
            
            driver.find_elements(By.XPATH, "//*[@id='radioContainer']")[2].click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='done-button']/ytcp-button-shape/button").click()
            time.sleep(10)

            driver.quit()
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
