import pygame

from map import world_map
from settings import *


def ray_casting(screen, player_pos, player_angle):
    # The angle where the ray casting will be drawn
    cur_angle = player_angle - HALF_FOV

    # The player x and y
    xo, yo = player_pos

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            pygame.draw.line(screen, DARKGREY, player_pos, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                if depth == 0:
                    depth = MAX_DEPTH
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c // 2, c, c // 3)
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE
