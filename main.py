import pygame
from constants import *
from logger import log_state 
pygame.init()
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        screen.fill("black")
        pygame.display.flip()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")





if __name__ == "__main__":
    main()
