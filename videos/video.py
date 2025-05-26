import os
import subprocess

from moviepy import VideoFileClip, concatenate_videoclips, clips_array


class Video():
    def __init__(self, rich_console):
        self.pygame_screens = os.path.join("auto_recorder", "screenshots")
        self.pygame_screen_name = "capture"
        self.rich_console = rich_console
        self.twitch_clips_path = os.path.join("twitch", "clips")
        self.pygame_video_path = os.path.join("videos", "pygame.mp4")
        self.twitch_video_path = os.path.join("videos", "clips.mp4")
        self.full_video_path = "full_video.mp4"

    def make_pygame_mp4(self):
        subprocess.run(
            ["ffmpeg", "-r", "60", "720p", "-i", os.path.join(self.pygame_screens, f"{self.pygame_screen_name}%08d.png"), "-vcodec", "mpeg4", "-q:v", "0", "-y", self.pygame_video_path], 
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

    def make_twitch_mp4(self):
        self.rich_console.log("Making twitch clips video.")
        twitch_clips = []
        for (dirpath, dirnames, filenames) in os.walk(self.twitch_clips_path):
            for filename in filenames:
                clip_path = os.path.join(dirpath, filename)
                video = VideoFileClip(clip_path)
        twitch_clips.append(video.resized((720, 400)))            
        twitch_video = concatenate_videoclips(twitch_clips, method="compose")
        twitch_video.write_videofile(filename="videos/clips.mp4", fps=60, logger=None)
        self.rich_console.log("Twitch clips video done.")

    def make_full_video(self):
        self.rich_console.log("Making full video.")
        pygame_video = VideoFileClip(self.pygame_video_path)
        twitch_video = VideoFileClip(self.twitch_video_path, has_mask=True)
        compined = clips_array([[twitch_video], [pygame_video]])
        compined.write_videofile(self.full_video_path, fps=60, logger=None)
        self.rich_console.log("Making full video done.")
