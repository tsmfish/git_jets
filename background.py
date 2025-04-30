import pygame
from config import WIDTH, HEIGHT, SKY_TOP, SKY_BOTTOM

def create_background():
    background = pygame.Surface((WIDTH, HEIGHT))
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(SKY_TOP[0] * (1 - t) + SKY_BOTTOM[0] * t)
        g = int(SKY_TOP[1] * (1 - t) + SKY_BOTTOM[1] * t)
        b = int(SKY_TOP[2] * (1 - t) + SKY_BOTTOM[2] * t)
        pygame.draw.line(background, (r, g, b), (0, y), (WIDTH, y))
    return background

def draw_background(screen, background):
    screen.blit(background, (0, 0))