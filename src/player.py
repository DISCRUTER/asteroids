import pygame

from src.circleshape import CircleShape
from src.constants import (
    LINE_WIDTH, 
    PLAYER_RADIUS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS, 
    PLAYER_SPEED,
    PLAYER_TURN_SPEED, 
    SHOT_RADIUS,
)
from src.shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
    
    # Provided by BootDev
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen,
            color="white",
            points=self.triangle(),
            width=LINE_WIDTH
        )
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt, fwd = True)
        if keys[pygame.K_s]:
            self.move(dt, fwd = False)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shoot_cooldown -= dt
    
    def move(self, dt, fwd):
        unit_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        speed_vector = unit_vector * PLAYER_SPEED * dt
        if fwd:
            self.position += speed_vector
        else:
            self.position -= speed_vector

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS