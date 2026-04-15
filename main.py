import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Calling log state
        log_state()

        # Checking for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Filling the screen with default color
        screen.fill('black')
        
        # Refresh screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
