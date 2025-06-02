import os
import pickle

from utils.params import LANGUAGE
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

class YTApi:
    def __init__(self):
        self.creds = None
        self.token_file = os.path.join("utils", f"token_{LANGUAGE.upper()}.pickle")

        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'utils/yt_api.json',
                    scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
                )
                self.creds = flow.run_local_server()               
                

            with open(self.token_file, 'wb') as token:
                pickle.dump(self.creds, token)


    def upload(self, file_path, title, description, category_id, privacy_status='public'):
        youtube = build('youtube', 'v3', credentials=self.creds)
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'categoryId': category_id
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }

        media = MediaFileUpload(file_path, resumable=True)

        request = youtube.videos().insert(
            part='snippet,status',
            body=body,
            media_body=media
        )

        request.execute()