import math
import pygame

from settings import *


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        cos_a = math.cos(self.angle)
        sin_a = math.sin(self.angle)
        if keys[pygame.K_z]:
            self.x += PLAYER_SPEED * cos_a
            self.y += PLAYER_SPEED * sin_a
        elif keys[pygame.K_q]:
            self.x += -PLAYER_SPEED * cos_a
            self.y += -PLAYER_SPEED * sin_a
        elif keys[pygame.K_s]:
            self.x += PLAYER_SPEED * cos_a
            self.y += -PLAYER_SPEED * sin_a
        elif keys[pygame.K_d]:
            self.x += -PLAYER_SPEED * cos_a
            self.y += PLAYER_SPEED * sin_a

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        elif keys[pygame.K_RIGHT]:
            self.angle += 0.02
