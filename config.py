# Window settings
import math

WIDTH, HEIGHT = 1680, 1050
FPS = 90

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
TRANSPARENT = (0, 0, 0, 0)

# Aircraft settings
JETS = (BLUE, YELLOW)
JET_SIZE = (80, 40)

# Background colors
SKY_TOP = (135, 206, 235)
SKY_BOTTOM = (19, 3, 202)

# Animation parameters
SCALE = 820
SPEED = 0.01
OFFSET = 0.2

# Lissajous curve parameters
LISSAJOUS_SCALE = 400  # Reduced scale for Lissajous curve to fit screen
LISSAJOUS_A = 3  # Frequency for x
LISSAJOUS_B = 2  # Frequency for y
LISSAJOUS_DELTA = math.pi / 2  # Phase shift
