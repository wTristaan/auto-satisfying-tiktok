import os
import emoji
import random
import requests
import subprocess

from datetime import datetime, timedelta

class TwitchAPI():
    def __init__(self, client_id, client_secret, rich_console, language):
        self.headers = None
        self.clips_path = os.path.join(os.path.abspath("."), "twitch", "clips")
        self.rich_console = rich_console
        
        self.__auth(client_id, client_secret)
        self.just_chatting_id = self.get_just_chatting_id()
        self.language = language

        try:
            os.makedirs(self.clips_path)
        except OSError:
            pass

        self.clear_clips()
        self.get_clips()

    def remove_using_emoji(self, txt):
        return emoji.replace_emoji(txt, '')
    
    def clear_clips(self):
        for (dirpath, dirnames, filenames) in os.walk(self.clips_path):
            for filename in filenames:
                if filename.__contains__(".mp4"):
                    os.remove(os.path.join(dirpath, filename))

    def __auth(self, client_id, client_secret):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'

        try:
            response = requests.post('https://id.twitch.tv/oauth2/token', headers=headers, data=data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
            
        bearer = response.json()['access_token']

        self.headers = {
            'Authorization': f'Bearer {bearer}',
            'Client-Id': client_id,
        }

    def get_just_chatting_id(self):
        url = 'https://api.twitch.tv/helix/games/top'
        response = requests.get(url, params={'first':100}, headers=self.headers)
        for game in response.json()['data']:
            if game['name'] == "Just Chatting":
                return game["id"]

        return 0
    
    def get_clips(self):
        self.rich_console.log(f"Downloading {self.language} twitch clips.")
        url = 'https://api.twitch.tv/helix/clips'
        yesterday = datetime.now() - timedelta(days=1)
        started_at = yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")
        ended_at = (yesterday + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        params = {
            "game_id": self.just_chatting_id,
            "started_at": started_at,
            "ended_at": ended_at,
            "first": 100
        }

        language_clips = []
        cursor = None

        while len(language_clips) < 100:
            if cursor:
                params['after'] = cursor
            response = requests.get(url, params=params, headers=self.headers)
            clips = response.json()['data']
            language_clips.extend(clip for clip in clips if clip.get('language') == self.language)
            cursor = response.json().get('pagination', {}).get('cursor')
            if not cursor:
                break

        if len(language_clips) < 10:
            clips = random.sample(language_clips, len(language_clips))
        else:
            clips = random.sample(language_clips, 10)
            
        all_duration = 0
        for i, clip in enumerate(clips):
            clip_title = self.remove_using_emoji(clip["title"])
            try:
                if clip_title != "":
                    clip_title.encode('utf-8')
                    clip_title = clip_title.replace(" ", "_") + ".mp4"
                else:
                    clip_title = "unknown.mp4"
            except Exception as e:
                print(e)
                clip_title = f'clip{i}.mp4'

            subprocess.run(
                ["twitch-dl", "download",
                "-q", "1080p",
                "--output", os.path.join(self.clips_path, clip_title),
                f"{clip["id"]}"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            if all_duration > 90:
                self.rich_console.log(f"Downloading {self.language} twitch clips done.")
                break
            all_duration += clip["duration"]
