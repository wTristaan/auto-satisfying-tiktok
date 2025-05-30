import dailymotion


class Dailymotion:
    def __init__(self, DAILYMOTION_EMAIL, DAILYMOTION_PASSWORD, DAILYMOTION_API_KEY, DAILYMOTION_API_SECRET, DAILYMOTION_ID, video_path):
        self.d = dailymotion.Dailymotion()
        self.d.set_grant_type('password', api_key=DAILYMOTION_API_KEY, api_secret=DAILYMOTION_API_SECRET, scope=['manage_videos'], 
                         info={'username': DAILYMOTION_EMAIL, 'password': DAILYMOTION_PASSWORD})
        self.video_path = video_path
        self.DAILYMOTION_ID = DAILYMOTION_ID
        self.url = self.d.upload(self.video_path)
        
    def upload(self, title):
        self.d.post(f'/user/{self.DAILYMOTION_ID}/videos', {'url': self.url, 'title': title, 'published': 'true', 'channel': 'fun', "is_created_for_kids": 'false'})