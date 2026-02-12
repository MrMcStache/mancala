import pygame
import os
import random
from constants import *

def initialize_stones(screen, pockets):
    for pocket in pockets:
        if not pocket.is_home:
            for i in range(0, 6):
                x = pocket.x + ((POCKET_WIDTH / 2) + random.randrange(-30, 30))
                y = pocket.y + ((POCKET_WIDTH / 2) + random.randrange(-30, 30))

                pocket.stones.append(Stone(x, y))

class Stone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.outline = OutlineCirc(self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, STONE_C, (self.x, self.y), STONE_RADIUS)
        self.outline.draw(screen)

    def update(self):
        pass

class OutlineCirc(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, STONE_OL_C, (self.x, self.y), STONE_RADIUS, width=3)

    def update(self):
        pass
