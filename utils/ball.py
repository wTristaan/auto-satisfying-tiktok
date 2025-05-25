import pygame
from utils.params import POSITION_BALL_X, POSITION_BALL_Y, BALL_RADIUS, BORDER_COLOR_BALL

class Ball:
    def __init__(
        self,
        color,
        velocity_x,
        velocity_y,
        x=POSITION_BALL_X,
        y=POSITION_BALL_Y,
        radius=BALL_RADIUS,
        border_color=BORDER_COLOR_BALL,
        border_radius=BALL_RADIUS + 2,
    ):
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.radius = radius
        self.color = color
        self.border_color = border_color
        self.border_radius = border_radius
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.gravity = 0.5
        self.bounce_factor = 1.1
        self.max_speed = 10
        self.trail_positions = []
        self.max_trail_length = 15
        self.circles_destroyed = 0
        self.shake_frames = 0

    def update(self, screen_width, screen_height):
        self.velocity_y += self.gravity
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.x - self.radius < 0:
            self.x = self.radius
            self.velocity_x = -self.velocity_x * self.bounce_factor
        elif self.x + self.radius > screen_width:
            self.x = screen_width - self.radius
            self.velocity_x = -self.velocity_x * self.bounce_factor

        if self.y - self.radius < 0:
            self.y = self.radius
            self.velocity_y = -self.velocity_y * self.bounce_factor
        elif self.y + self.radius > screen_height:
            self.y = screen_height - self.radius
            self.velocity_y = -self.velocity_y * self.bounce_factor

    def draw(self, screen):
        for i, (pos_x, pos_y) in enumerate(self.trail_positions):
            alpha = int(
                150 * (1 - i / len(self.trail_positions))
            )
            trail_color = (
                *self.color[:3],
                alpha,
            ) 

            trail_radius = max(
                1, int(self.radius * (1 - i / len(self.trail_positions) * 0.5))
            )

            trail_surface = pygame.Surface(
                (trail_radius * 2, trail_radius * 2), pygame.SRCALPHA
            )
            pygame.draw.circle(
                trail_surface, trail_color, (trail_radius, trail_radius), trail_radius
            )
            screen.blit(
                trail_surface, (int(pos_x - trail_radius), int(pos_y - trail_radius))
            )

        if self.border_color and self.border_radius:
            pygame.draw.circle(
                screen,
                self.border_color,
                [int(self.x), int(self.y)],
                self.border_radius,
            )

        pygame.draw.circle(
            screen, self.color, [int(self.x), int(self.y)], self.radius
        )

    def update_gravity(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.velocity_y += self.gravity
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.x - self.radius < 0 or self.x + self.radius > 720:
            self.velocity_x = -self.velocity_x
            self.x = max(self.radius, min(720 - self.radius, self.x))

        if self.y - self.radius < 0 or self.y + self.radius > 680:
            self.velocity_y = -self.velocity_y
            self.y = max(self.radius, min(680 - self.radius, self.y))

        if self.x - self.radius < 0 or self.x + self.radius > 720:
            self.velocity_x = -self.velocity_x
            self.x = max(self.radius, min(720 - self.radius, self.x))

        if self.y - self.radius < 0 or self.y + self.radius > 680:
            self.velocity_y = -self.velocity_y
            self.y = max(self.radius, min(680 - self.radius, self.y))
