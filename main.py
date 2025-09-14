import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign containers, disregard pyright error
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Start the game loop, yes it is infinite
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

        # Update game objects
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()

            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
