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
    # Lock FPS for every computer
    clock = pygame.time.Clock()

    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                temp_obj_pos = mouse_pos

        # Add background
        window.blit(BG, (0, 0))

        # Draw circle where mouse is
        if temp_obj_pos:
            pygame.draw.circle(window, RED, temp_obj_pos, OBJ_SIZE)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
