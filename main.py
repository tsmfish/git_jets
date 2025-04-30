import asyncio
import pygame
import math
from config import WIDTH, HEIGHT, FPS, JETS, SCALE, SPEED, OFFSET
from background import create_background, draw_background
from aircraft import create_aircraft_bitmap, draw_aircraft

def lemniscate(t, a):
    x = a * math.cos(t) / (1 + math.sin(t) ** 2)
    y = a * math.sin(t) * math.cos(t) / (1 + math.sin(t) ** 2)
    return x, y

def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Fighter Aircraft Animation")
    clock = pygame.time.Clock()
    background = create_background()
    aircraft_bitmaps = [create_aircraft_bitmap(jet) for jet in JETS]
    return screen, clock, background, aircraft_bitmaps

async def main():
    screen, clock, background, aircraft_bitmaps = setup()
    t = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_background(screen, background)

        for i in range(len(JETS)):
            x, y = lemniscate(t - OFFSET * i, SCALE)
            x, y = x + WIDTH // 2, y + HEIGHT // 2

            t_next = t - OFFSET * i + 0.01
            x1_next, y1_next = lemniscate(t_next, SCALE)
            x1_next, y1_next = x1_next + WIDTH // 2, y1_next + HEIGHT // 2
            angle = math.atan2(y1_next - y, x1_next - x)

            draw_aircraft(screen, x, y, angle, aircraft_bitmaps[i])

        t += SPEED

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(1.0 / FPS)

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())