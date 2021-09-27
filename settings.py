import math

# game settings
WINDOWS_SIZE = (1300, 600)
WIDTH, HEIGHT = WINDOWS_SIZE
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
FPS = 60

# player_settings
player_pos = HALF_WIDTH, HALF_HEIGHT
PLAYER_SPEED = 2
player_angle = 0
TILE = 100

# ray casting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 220, 0)
RED = (220, 0, 0)
DARKGREY = (40, 40, 40)
PURPLE = (120, 0, 120)
BLUE = (0, 0, 255)

# circle settings
RADIUS = 10
C_WIDTH = 10
