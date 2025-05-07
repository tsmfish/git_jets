import asyncio
import pygame
from config import WIDTH, HEIGHT, FPS, JETS, SPEED
from background import create_background, draw_background
from aircraft import create_aircraft_bitmap, draw_aircraft
from flight_path import get_jet_coordinates


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
            x, y, angle = get_jet_coordinates(t, i)

            draw_aircraft(screen, x, y, angle, aircraft_bitmaps[i])

        t += SPEED

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(1.0 / FPS)

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())