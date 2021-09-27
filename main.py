import math

import pygame
import sys

from map import world_map
from player import Player
from ray_casting import ray_casting
from settings import *

pygame.init()
screen = pygame.display.set_mode(WINDOWS_SIZE)
player = Player()
clock = pygame.time.Clock()


def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        player.movement()
        screen.fill(BLACK)

        pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(screen, DARKGREY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        ray_casting(screen, player.pos, player.angle)

        # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), RADIUS, C_WIDTH)
        # pygame.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
        #                                              player.y + WIDTH * math.sin(player.angle)))
        #
        # for x, y in world_map:
        #     pygame.draw.rect(screen, DARKGREY, (x, y, TILE, TILE), 2)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    run()
