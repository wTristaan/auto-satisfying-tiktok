import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tiktok_uploader.upload import upload_video
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.params import YOUTUBE_EMAIL, YOUTUBE_PASSWORD, DAILYMOTION_EMAIL, DAILYMOTION_PASSWORD


class Upload():
    def __init__(self, video_to_upload_path, rich_console):
        self.video_path = video_to_upload_path
        self.title_video = self.video_path.replace("_", " ").replace(".mp4", "")
        self.tags = "#clip #twitch #funny #compilation #satisfyingvideo"
        self.full_title = f"{self.title_video} - Twitch clips compilation ! {self.tags}" 
        self.full_title_without_tags = f"{self.title_video} - Twitch clips compilation !" 
        self.rich_console = rich_console

    def tiktok(self):
        try:
            self.rich_console.log("Uploading video to tiktok.")
            upload_video(self.video_path, self.full_title, cookies='utils/cookies.txt', headless=True)
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

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://www.dailymotion.com/fr")
            time.sleep(10)

            WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='sp_message_iframe_1288283']")))
            driver.find_element(By.XPATH, "//*[@id='notice']/div[5]/button[2]").click()
            driver.switch_to.default_content()
            time.sleep(5)

            driver.find_element(By.XPATH, "//*[@id='root']/div/header/div/div[3]/div[3]/button").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='signin-form']/label[1]/input").send_keys(DAILYMOTION_EMAIL)
            time.sleep(2)

            driver.find_element(By.XPATH, " //*[@id='signin-form']/label[2]/input").send_keys(DAILYMOTION_PASSWORD)
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='portal-root']/div/div/div[2]/div[2]/div[3]/button").click()
            time.sleep(5)

            driver.find_element(By.XPATH, "//*[@id='root']/div/header/div/div[3]/div[2]/button").click()
            time.sleep(2)
            
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(10)

            driver.find_element(By.XPATH, "//*[@id='react-root']/div[2]/div/div/button[2]").click()
            time.sleep(2)
            
            inputs = driver.find_elements(By.TAG_NAME, "input")
            inputs[-1].send_keys(os.path.abspath(self.video_path))
            time.sleep(10)

            input_title = driver.find_element(By.XPATH, "//*[@id='title']")
            input_title.send_keys(Keys.CONTROL + "a")
            input_title.send_keys(Keys.DELETE)
            time.sleep(2)


            input_title.send_keys(self.full_title)
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='description']").send_keys(self.tags)
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='channel']").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[7]").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='react-root']/div[2]/div/div[3]/div/div/div[3]/div/div[3]/button").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='react-root']/div[2]/div/div[3]/div/div/div[3]/div/div[3]/button").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='react-root']/div[2]/div/div[3]/div/div/div[3]/div/div[3]/button").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='react-root']/div[2]/div/div[3]/div/div/div[3]/div/div/button").click()
            time.sleep(120)

            driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/main/div/div/div/div/div/ul/li/div/div[2]/div/div/button").click()
            time.sleep(2)

            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[1]").click()
            time.sleep(5)

            driver.find_element(By.XPATH, "//*[@id='tags']").send_keys(self.tags.replace(" ", ", "))
            time.sleep(2)

            driver.find_element(By.XPATH, "//*[@id='scrollable']/span/button").click()
            time.sleep(10)

            driver.quit()
            self.rich_console.log("Upload video to dailymotion done.")
        except Exception as e:
            self.rich_console.log(f"Upload video to dailymotion error {str(e)}.")
