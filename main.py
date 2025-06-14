import time
import pygame
import random
import warnings

from tqdm import tqdm
from utils.ball import Ball
from videos.video import Video
from rich.console import Console
from twitch.api import TwitchAPI
from utils.utils import generate_circles
from auto_recorder.video_recorder import VideoRecorder
from utils.params import FPS, TOTAL_FRAMES, COLORS, CLIENT_ID, CLIENT_SECRET, LANGUAGE

warnings.filterwarnings("ignore")

console = Console()
pygame.init()
console.log("Pygame initialized.")

recorder = VideoRecorder()
twitch = TwitchAPI(CLIENT_ID, CLIENT_SECRET, console, LANGUAGE)
video = Video(console, LANGUAGE)
time.sleep(1)
video.make_twitch_mp4()

screen = pygame.display.set_mode((1080, 1280), pygame.RESIZABLE)
clock = pygame.time.Clock()
ball_color = random.choice(list(COLORS.values()))
ball = Ball(color=ball_color, velocity_x=random.uniform(-5, 5), velocity_y=random.uniform(-5, 5))
all_circles = generate_circles()
circles = all_circles[:15]
next_circle_index = 20
circles_to_remove = []
base_circle = circles[0]

time.sleep(1)
console.log("Making pygame video.")
for i in tqdm(range(TOTAL_FRAMES)):
    screen.fill((0, 0, 0))
    clock.tick(FPS)

    ball.update_gravity()

    for circle in circles[:]:
        should_destroy, has_collided = circle.check_collision(ball)
        if should_destroy:
            circles.remove(circle)
            ball.circles_destroyed += 1
            ball.shake_frames = 4

            if next_circle_index < len(all_circles):
                circles.append(all_circles[next_circle_index])
                next_circle_index += 1
        elif has_collided:
            current_time = pygame.time.get_ticks()
            last_bounce_time = current_time

    if circles:
        base_circle = circles[0]
        if base_circle.radius > base_circle.min_radius:
            base_circle.radius -= base_circle.shrink_rate
            base_circle.radius = max(base_circle.radius, base_circle.min_radius)

        for idx, circle in enumerate(circles):
            circle.radius = base_circle.radius + idx * 30

    for circle in circles:
        circle.draw(screen)

    ball.draw(screen)
    ball.trail_positions.insert(0, (ball.x, ball.y))
    if len(ball.trail_positions) > ball.max_trail_length:
        ball.trail_positions.pop()

    pygame.display.update()
    recorder.make_png(screen)

pygame.quit()
video.make_pygame_mp4()
console.log("Pygame video done.")
video.make_full_video()
video.uploads()