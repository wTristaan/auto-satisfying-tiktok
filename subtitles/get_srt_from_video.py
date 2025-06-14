import pysrt
import assemblyai as aai

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy import TextClip

class Subtitle:
    def __init__(self, api_key, language):
        self.api_key = api_key
        self.language = language

    @staticmethod
    def time_to_seconds(time_obj):
        return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000

    @staticmethod
    def create_subtitle_clips(subtitles, fontsize=24, color='yellow'):
        subtitle_clips = []

        for subtitle in subtitles:
            start_time = int(Subtitle.time_to_seconds(subtitle.start))
            end_time = int(Subtitle.time_to_seconds(subtitle.end))
            duration = end_time - start_time

            text_clip = TextClip(
                text=subtitle.text,
                font_size=fontsize,
                font="subtitles/Poppins-Medium.ttf",
                color=color,
                bg_color='black',
                transparent=True,
                method="caption",
                size=(500, 100),
                interline=4
            ).with_start(start_time).with_duration(duration)

            text_position = ('center', 640)
            subtitle_clips.append(text_clip.with_position(text_position))

        return subtitle_clips

    def get_srt_from_video(self, video_path):
        srt_path = f"{video_path}.srt"
        aai.settings.api_key = self.api_key
        config = aai.TranscriptionConfig(language_code=self.language)
        transcriber = aai.Transcriber(config=config)
        transcript = transcriber.transcribe(video_path)
        srt = transcript.export_subtitles_srt()

        with open(srt_path, "w", encoding='utf-8') as file:
            file.write(srt)

        self.add_subtitles(video_path, srt_path)

    def add_subtitles(self, video_path, srt_path):
        video = VideoFileClip(video_path)
        subtitles = pysrt.open(srt_path, encoding='utf-8')

        output_video_file = video_path.replace("_2_.mp4", ".mp4")

        subtitle_clips = self.create_subtitle_clips(subtitles)
        final_video = CompositeVideoClip([video] + subtitle_clips)
        final_video.write_videofile(output_video_file, fps=60, logger=None)