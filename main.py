import sys

import pygame

from src.asteroid import Asteroid
from src.asteroidfield import AsteroidField
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from src.player import Player
from src.shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initializing Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 # Delta Time

    # Setting up groups
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    # Creating a player
    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Creating Shot
    Shot.containers = (shots, drawable, updatable)

    # Creating Asteroids
    Asteroid.containers = (asteroids, drawable, updatable)

    # Creating Asteroid Field
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Checking for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Filling the screen with default color
        screen.fill('black')
        
        # Updating Sprites
        updatable.update(dt=dt)

        # Drawing Sprites
        for obj in drawable:
            obj.draw(screen)

        # Checking for player collisions
        for obj in asteroids:
            if obj.collides_with(player):
                print("Game Over!")
                sys.exit()
        
        # Checking for shot collision
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot):
                    obj.split()
                    shot.kill()

        # Refresh screen
        pygame.display.flip()

        # Refreshing Clock & Setting delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
