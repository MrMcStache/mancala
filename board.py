import pygame
import os
import random
from constants import *

class Board(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.outline = OutlineRect(*BOARD_POS, BOARD_SIZE, BOARD_OL_C)

    def draw(self, screen):
        board = pygame.Rect(BOARD_POS, BOARD_SIZE)

        pygame.draw.rect(screen, BOARD_C, board, border_radius = BORDER_RADIUS)
        self.outline.draw(screen)

class Pocket(pygame.sprite.Sprite):
    def __init__(self, x, y, index, is_home=False):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.p_index = index
        self.is_home = is_home
        #self.must_play = False

        if self.is_home:
            self.size = (POCKET_WIDTH, HOME_HEIGHT)

            if self.p_index == 6:
                self.player = 1
            else:
                self.player = 0
        else:
            self.size = (POCKET_WIDTH, POCKET_WIDTH)

        self.outline = OutlineRect(self.x, self.y, self.size, POCKET_OL_C)
        self.stones = []

    def draw(self, screen):
        pygame.draw.rect(screen, POCKET_C, pygame.Rect((self.x, self.y), self.size), border_radius = BORDER_RADIUS)
        self.outline.draw(screen)

    def get_stones(self):
        return len(self.stones)

class OutlineRect(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect((self.x, self.y), self.size), width = 3, border_radius = BORDER_RADIUS)

    def update(self):
        pass
