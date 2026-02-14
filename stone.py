import pygame
import os
import random
from constants import *

class Stone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.outline = OutlineCirc()

    def draw(self, screen):
        pygame.draw.circle(screen, STONE_C, (self.x, self.y), STONE_RADIUS)
        self.outline.draw(screen, self.x, self.y)

class OutlineCirc(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, STONE_OL_C, (x, y), STONE_RADIUS, width=3)
