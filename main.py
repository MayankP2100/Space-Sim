import pygame
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50
OBJ_SIZE = 5
VEL_SCALE = 100
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)
BG = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("assets/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

# Set window size and title
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Sim")

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
