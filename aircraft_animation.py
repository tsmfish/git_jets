import asyncio
import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1680, 1050
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fighter Aircraft Animation")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
TRANSPARENT = (0, 0, 0, 0)

JETS = (BLUE, YELLOW)
JET_SIZE = (80,40)

SKY_TOP = (135, 206, 235)
SKY_BOTTOM = (19, 3, 202)

FPS = 90
t = 0
scale = 820
speed = 0.01
offset = 0.2

aircraft_bitmap = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def create_aircraft_bitmap(color):
    sprite = pygame.Surface((20, 11), pygame.SRCALPHA)
    for y in range(11):
        for x in range(20):
            if aircraft_bitmap[y][x] == 1:
                sprite.set_at((x, y), color)
            else:
                sprite.set_at((x, y), TRANSPARENT)
    scaled_sprite = pygame.transform.scale(sprite, JET_SIZE)
    return scaled_sprite

aircraft_bitmaps = list(create_aircraft_bitmap(jet) for jet in JETS)

def create_background():
    background = pygame.Surface((WIDTH, HEIGHT))
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(SKY_TOP[0] * (1 - t) + SKY_BOTTOM[0] * t)
        g = int(SKY_TOP[1] * (1 - t) + SKY_BOTTOM[1] * t)
        b = int(SKY_TOP[2] * (1 - t) + SKY_BOTTOM[2] * t)
        pygame.draw.line(background, (r, g, b), (0, y), (WIDTH, y))
    return background

background = create_background()


def lemniscate(t, a):
    x = a * math.cos(t) / (1 + math.sin(t) ** 2)
    y = a * math.sin(t) * math.cos(t) / (1 + math.sin(t) ** 2)
    return x, y

def draw_aircraft(screen, x, y, angle, bitmap):
    rotated_bitmap = pygame.transform.rotate(bitmap, -math.degrees(angle))
    rect = rotated_bitmap.get_rect(center=(x, y))
    screen.blit(rotated_bitmap, rect)

def setup():
    global clock
    clock = pygame.time.Clock()

async def main():
    global t
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        for i in range(len(JETS)):
            x, y = lemniscate(t - offset * i, scale)

            x, y = x + WIDTH // 2, y + HEIGHT // 2

            t_next = t - offset * i + 0.01
            x1_next, y1_next = lemniscate(t_next, scale)
            x1_next, y1_next = x1_next + WIDTH // 2, y1_next + HEIGHT // 2
            angle1 = math.atan2(y1_next - y, x1_next - x)

            draw_aircraft(screen, x, y, angle1, aircraft_bitmaps[i])

        t += speed

        pygame.display.flip()
        await asyncio.sleep(1.0 / FPS)

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())