import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #set screen size
    game_clock = pygame.time.Clock() #instantiate timekeeper object. measures in millisec
    dt = 0

    updatable = pygame.sprite.Group() #empty group (container) for all objects that can be updated
    drawable = pygame.sprite.Group() #empty group (container) for all objects that can be drawn
    asteroids = pygame.sprite.Group() #empty group to put all the asteroids
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (drawable, updatable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #actions
        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for roid in asteroids:
            for shot in shots:
                if shot.collides_with(roid):
                    log_event("asteroid_shot")
                    shot.kill()
                    roid.split()


        #rendering (drawing the code)
        screen.fill('black') #make background screen
        for i in drawable: #loop through the drawable container and draw all of them
            i.draw(screen)

        dt = (game_clock.tick(60) / 1000) #tick returns milliseconds since last call. divide by 1000 to get seconds. store as dt (delta time)

        pygame.display.flip()



if __name__ == "__main__":
    main()
