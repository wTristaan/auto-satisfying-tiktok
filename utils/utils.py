import random

from utils.params import COLORS, NUMBERS_OF_CIRCLES, START_RADIUS, POSITION_CIRCLE_X, POSITION_CIRCLE_Y, THICKNESS
from utils.circle import Circle

def generate_circles():
    circles = []
    for i in range(NUMBERS_OF_CIRCLES):
        radius = START_RADIUS + i * 30
        start_angle = (i * 30) % 360
        rotation_speed = random.uniform(0.02, 0.03)
        circle_color = random.choice(list(COLORS.values()))
        circle = Circle(
            POSITION_CIRCLE_X,
            POSITION_CIRCLE_Y,
            radius,
            circle_color,
            THICKNESS,
            start_angle,
            gap_angle=3,
            gap_size=0.7,
        )
        circle.rotation_speed = rotation_speed
        circles.append(circle)
    return circles