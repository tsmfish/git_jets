import math

from config import OFFSET, LISSAJOUS_SCALE, HEIGHT, WIDTH, LISSAJOUS_A, LISSAJOUS_B, LISSAJOUS_DELTA, SCALE

def lemniscate(time: float, amplitude: float) -> tuple[float, float]:
    x = amplitude * math.cos(time) / (1 + math.sin(time) ** 2)
    y = amplitude * math.sin(time) * math.cos(time) / (1 + math.sin(time) ** 2)
    return x, y

def lissajous(time: float, amplitude: float) -> tuple[float, float]:
    x = amplitude * math.sin(LISSAJOUS_A * time + LISSAJOUS_DELTA)
    y = amplitude * math.sin(LISSAJOUS_B * time)
    return x, y

def get_lemniscate_coordinates(time:float, shift: int) -> tuple[float, float, float]:
    x, y = lemniscate(time - OFFSET * shift, SCALE)
    x, y = x + WIDTH // 2, y + HEIGHT // 2

    t_next = time - OFFSET * shift + 0.01
    x1_next, y1_next = lemniscate(t_next, SCALE)
    x1_next, y1_next = x1_next + WIDTH // 2, y1_next + HEIGHT // 2
    angle = math.atan2(y1_next - y, x1_next - x)

    return x, y, angle

def get_lissajous_coordinate(time: float, shift: int) -> tuple[float, float, float]:
    x, y = lissajous(time - OFFSET * shift, LISSAJOUS_SCALE)
    x, y = x + WIDTH // 2, y + HEIGHT // 2

    t_next = time - OFFSET * shift + 0.01
    x1_next, y1_next = lissajous(t_next, LISSAJOUS_SCALE)
    x1_next, y1_next = x1_next + WIDTH // 2, y1_next + HEIGHT // 2
    angle = math.atan2(y1_next - y, x1_next - x)

    return x, y, angle

get_jet_coordinates = get_lemniscate_coordinates
# get_jet_coordinates = get_lissajous_coordinate