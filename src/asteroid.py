import random

import pygame

from src.circleshape import CircleShape
from src.constants import (
    ASTEROID_MIN_RADIUS,
    LINE_WIDTH
)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color='white', 
            center=self.position, 
            radius=self.radius, 
            width=LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        seed = random.uniform(20, 50)
        vel_one = self.velocity.rotate(seed)
        vel_two = self.velocity.rotate(-seed)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        aster_one = Asteroid(self.position.x, self.position.y, new_radius)
        aster_one.velocity = vel_one * 1.2
        aster_two = Asteroid(self.position.x, self.position.y, new_radius)
        aster_two.velocity = vel_two * 1.2