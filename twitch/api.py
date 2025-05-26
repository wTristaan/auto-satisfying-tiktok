import os
import random
import requests
import subprocess

from datetime import datetime, timedelta

class TwitchAPI():
    def __init__(self, client_id, client_secret, rich_console):
        self.headers = None
        self.clips_path = os.path.join(os.path.abspath("."), "twitch", "clips")
        self.rich_console = rich_console
        
        self.__auth(client_id, client_secret)
        self.just_chatting_id = self.get_just_chatting_id()

        try:
            os.makedirs(self.clips_path)
        except OSError:
            pass

        self.clear_clips()
        self.get_clips()
    
    def clear_clips(self):
        for (dirpath, dirnames, filenames) in os.walk(self.clips_path):
            for filename in filenames:
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
        self.rich_console.log("Downloading twitch clips.")
        url = 'https://api.twitch.tv/helix/clips'
        yesterday = datetime.now() - timedelta(days=1)
        started_at = yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")
        ended_at = (yesterday + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        params = {
            "game_id": self.just_chatting_id,
            "started_at": started_at,
            "ended_at": ended_at
        }
        response = requests.get(url, params=params, headers=self.headers)
        clips = sorted(response.json()['data'], key=lambda x: x['view_count'], reverse=True)
        clips = random.sample(clips, 10)
        all_duration = 0
        for i, clip in enumerate(clips):
            all_duration += clip["duration"]
            clip_title = ""
            try:
                clip["title"].encode('utf-8')
                clip_title = clip["title"].replace(" ", "_") + ".mp4"
            except:
                clip_title = f'clip{i}.mp4'

            subprocess.run(
                ["twitch-dl", "download", 
                 "-q", "720p", 
                 "--output", os.path.join(self.clips_path, clip_title),
                 f"{clip["id"]}"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            if all_duration > 90:
                self.rich_console.log("Downloading twitch clips done.")
                break
