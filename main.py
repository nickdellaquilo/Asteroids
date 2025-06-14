import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()

    Player.containers        = (updatable, drawable)
    Asteroid.containers      = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers          = (updatable, drawable, shots)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    field  = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        
        updatable.update(dt)

        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                sys.exit()
            
            for s in shots:
                if a.collision(s):
                    s.kill()
                    a.split()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(144)/1000

if __name__ == "__main__":
    main()