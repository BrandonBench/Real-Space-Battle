import pygame
from SpaceshipAdventure import SpaceshipAdventure

def main():
    pygame.font.init()
    c = SpaceshipAdventure(2000,1200, 64)
    c.main_loop()
    return
    
if __name__ == "__main__":
    main()

