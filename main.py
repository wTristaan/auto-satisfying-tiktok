import pygame
import random

from utils.ball import Ball
from utils.utils import generate_circles
from utils.params import FPS, TOTAL_FRAMES, COLORS
from auto_recorder.video_recorder import VideoRecorder

pygame.init()
recorder = VideoRecorder()

screen = pygame.display.set_mode((720, 680))
clock = pygame.time.Clock()
ball_color = random.choice(list(COLORS.values()))
ball = Ball(color=ball_color, velocity_x=random.uniform(-5, 5), velocity_y=random.uniform(-5, 5))
all_circles = generate_circles()
circles = all_circles[:15]
next_circle_index = 20
circles_to_remove = []
base_circle = circles[0]


for i in range(TOTAL_FRAMES):
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
recorder.make_mp4()