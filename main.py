import pygame
from constants import *
from logger import log_state
from player import Player 
pygame.init()
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dt = clock.tick(60) / 1000
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        log_state()
        pygame.display.flip()
    
    

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")





if __name__ == "__main__":
    main()
