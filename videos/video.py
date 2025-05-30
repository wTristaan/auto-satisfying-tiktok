import os
import random
import subprocess

from upload.upload import Upload
from moviepy import VideoFileClip, concatenate_videoclips, clips_array


class Video():
    def __init__(self, rich_console, LANGUAGE):
        self.pygame_screens = os.path.join("auto_recorder", "screenshots")
        self.pygame_screen_name = "capture"
        self.rich_console = rich_console
        self.twitch_clips_path = os.path.join("twitch", "clips")
        self.pygame_video_path = os.path.join(os.path.abspath("."), "videos", "pygame.mp4")
        self.twitch_video_path = ""
        self.full_video_path = ""
        self.LANGUAGE = LANGUAGE

    def make_pygame_mp4(self):
        subprocess.run([
            "ffmpeg",
            "-r", "60",
            "-i", os.path.join(self.pygame_screens, f"{self.pygame_screen_name}%08d.png"),
            "-vcodec", "mpeg4",
            "-q:v", "0",
            "-y",
            self.pygame_video_path
        ],  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def make_twitch_mp4(self):
        self.rich_console.log("Making twitch clips video.")
        twitch_clips = []
        video_title = ""
        for dirpath, dirnames, filenames in os.walk(self.twitch_clips_path):
            for filename in filenames:
                if filename.endswith(".mp4"):
                    if len(filename) > len(video_title):
                        video_title = filename
                        
                    clip_path = os.path.join(dirpath, filename)
                    video = VideoFileClip(clip_path)
                    twitch_clips.append(video.resized((720, 400)))            

        self.twitch_video_path = f"videos/{video_title}"
        self.full_video_path = video_title

        twitch_video = concatenate_videoclips(twitch_clips, method="compose")
        twitch_video.write_videofile(filename= self.twitch_video_path, fps=60, logger=None)
        self.rich_console.log("Twitch clips video done.")

    def make_full_video(self):
        self.rich_console.log("Making full video.")
        pygame_video = VideoFileClip(self.pygame_video_path)
        twitch_video = VideoFileClip(self.twitch_video_path, has_mask=True)
        if twitch_video.duration > pygame_video.duration:
            twitch_video = twitch_video.with_duration(pygame_video.duration)
        compined = clips_array([[twitch_video], [pygame_video]])
        compined.write_videofile(self.full_video_path.replace(".mp4", "_1_.mp4"), fps=60, logger=None)

        self.rich_console.log("Adding hook on full video.")
        number_hook = random.randint(1, 17)
        video = VideoFileClip(self.full_video_path.replace(".mp4", "_1_.mp4"))
        hook = VideoFileClip(f"videos/hooks/{number_hook}.mp4") 
        hook = hook.resized((720, 1080))             
        video = concatenate_videoclips([hook, video], method="compose")
        video.write_videofile(self.full_video_path, fps=60, logger=None)
        self.rich_console.log("Making full video done.")

    def uploads(self):
        up = Upload(self.full_video_path, self.rich_console, self.LANGUAGE)
        up.tiktok()
        up.youtube()
        up.daylimotion()
