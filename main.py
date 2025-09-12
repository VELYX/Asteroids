import pygame
from constants import *
from player import Player


def main():
    # Start Asteroids
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    # Initialize configuration fields
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Group game objects for scalability
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign containers, disregard pyright error
    Player.containers = (updatable, drawable)

    # Instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Start game loop, yes it is infinite
    running = True
    while running:
        # Set game to 60 fps
        dt = clock.tick(60) / 1000

        # Until we quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set canvas
        screen.fill("black")

        # Update game objects using their respective groups
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
