import pygame
import os
from constants import *

def initialize_pockets():
    px = BOARD_X + 170
    py = BOARD_Y + 210

    for p in range(0, 14):
        if p >= 6:
            px = BOARD_X + 1130
            if (p + 1) % 7 == 0:
                home = Pocket(px - (160 * (p - 6)), py - 200, True)
                #print(f"Home {p}: ({home.x},{home.y})")
            else:
                pocket = Pocket(px - (160 * (p - 6)), py - 200)
                #print(f"Pocket {p}: ({pocket.x},{pocket.y})")
        else:
            pocket = Pocket(px + (160 * p), py)
            #print(f"Pocket {p}: ({pocket.x},{pocket.y})")

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
        #pygame.draw.rect(screen, BOARD_OL_C, board, width = 10, border_radius = BORDER_RADIUS)

    def update(self):
        pass

class Pocket(pygame.sprite.Sprite):
    def __init__(self, x, y, is_home=False):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.is_home = is_home
        if is_home:
            self.size = (POCKET_WIDTH, HOME_HEIGHT)
        else:
            self.size = (POCKET_WIDTH, POCKET_WIDTH)
        self.outline = OutlineRect(self.x, self.y, self.size, POCKET_OL_C)
        self.stones = []

    def draw(self, screen):
        pygame.draw.rect(screen, POCKET_C, pygame.Rect((self.x, self.y), self.size), border_radius = BORDER_RADIUS)
        self.outline.draw(screen)

    def update(self):
        pass

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

'''class Home(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.size = (POCKET_WIDTH, HOME_HEIGHT)
        self.outline = OutlineRect(self.x, self.y, self.size, POCKET_OL_C)

    def draw(self, screen):
        pygame.draw.rect(screen, POCKET_C, pygame.Rect((self.x, self.y), self.size), border_radius = BORDER_RADIUS)
        self.outline.draw(screen)

    def update(self):
        pass
'''
