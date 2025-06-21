import os
from utils.params import GDRIVE_FOLDER_ID
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, MediaFileUpload


class Gdrive:
    def __init__(self, console):
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.parent_folder_id = GDRIVE_FOLDER_ID
        self.service = self.get_authenticated_service()
        self.last_folder_number = self.get_last_folder_number()
        self.new_folder_number = self.last_folder_number + 1
        self.new_folder_name = str(self.new_folder_number)
        self.new_folder_id = self.create_folder()
        self.rich_console = console


    def get_authenticated_service(self):
        creds = None

        if os.path.exists('utils/token.json'):
            creds = Credentials.from_authorized_user_file('utils/token.json', self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'utils/yt_api.json', self.SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return build('drive', 'v3', credentials=creds)
    
    def get_last_folder_number(self):
        results = self.service.files().list(
            q=f"'{self.parent_folder_id}' in parents and mimeType='application/vnd.google-apps.folder'",
            fields="files(id, name)").execute()
        folders = results.get('files', [])

        if not folders:
            return -1

        last_folder_number = max(int(folder['name']) for folder in folders)
        return last_folder_number
    
    def create_folder(self):
        folder_metadata = {
            'name': self.new_folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [self.parent_folder_id]
        }
        folder = self.service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')
    
    def upload(self, file_path):
        self.service = self.get_authenticated_service()
        self.rich_console.log(f"Uploading video '{file_path}'")
        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [self.new_folder_id]
        }
        media = MediaFileUpload(file_path, mimetype='video/mp4')
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id').execute()
        self.rich_console.log(f"Uploaded video '{file_path}' with ID: {file.get('id')}")