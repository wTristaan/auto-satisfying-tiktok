import os

from dotenv import load_dotenv

load_dotenv()

FPS = 60
TOTAL_FRAMES = FPS * 61
BORDER_COLOR_BALL = (255, 255, 255)
COLORS = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "magenta": (255, 0, 255),
    "dark_gray": (169, 169, 169),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "brown": (165, 42, 42),
    "silver": (192, 192, 192),
    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "olive": (128, 128, 0),
    "maroon": (128, 0, 0),
    "sky_blue": (135, 206, 235),
    "violet": (238, 130, 238),
    "coral": (255, 127, 80),
    "salmon": (250, 128, 114),
    "turquoise": (64, 224, 208),
    "chocolate": (210, 105, 30),
    "crimson": (220, 20, 60),
    "plum": (221, 160, 221),
    "orchid": (218, 112, 214),
    "tan": (210, 180, 140),
    "goldenrod": (218, 165, 32),
}
POSITION_BALL_X = 1080 // 2
POSITION_BALL_Y = 1280 // 2
BALL_RADIUS = 30
NUMBERS_OF_CIRCLES = 65
START_RADIUS = 100
POSITION_CIRCLE_X = POSITION_BALL_X
POSITION_CIRCLE_Y = POSITION_BALL_Y
THICKNESS = 5

CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')

YOUTUBE_EMAIL=os.getenv('YOUTUBE_EMAIL')
YOUTUBE_PASSWORD=os.getenv('YOUTUBE_PASSWORD')
DAILYMOTION_EMAIL=os.getenv('DAILYMOTION_EMAIL')
DAILYMOTION_PASSWORD=os.getenv('DAILYMOTION_PASSWORD')
DAILYMOTION_API_KEY=os.getenv('DAILYMOTION_API_KEY')
DAILYMOTION_API_SECRET=os.getenv('DAILYMOTION_API_SECRET')
DAILYMOTION_ID=os.getenv('DAILYMOTION_ID')

LANGUAGE = 'fr'

ASSEMBLY_API = os.getenv("ASSEMBLY_API")

GDRIVE_FOLDER_ID = os.getenv("GDRIVE_FOLDER_ID")
