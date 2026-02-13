import pygame
import os
import random
from constants import *

def initialize_pockets():
    px = BOARD_X + 170
    py = BOARD_Y + 210

    for p in range(0, 14):
        if p >= 6:
            px = BOARD_X + 1130
            if (p + 1) % 7 == 0:
                home = Pocket(px - (160 * (p - 6)), py - 200, p, True)
                #print(f"Home {p}: ({home.x},{home.y})")
            else:
                pocket = Pocket(px - (160 * (p - 6)), py - 200, p)
                #print(f"Pocket {p}: ({pocket.x},{pocket.y})")
        else:
            pocket = Pocket(px + (160 * p), py, p)
            #print(f"Pocket {p}: ({pocket.x},{pocket.y})")

class Board(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.outline = OutlineRect(*BOARD_POS, BOARD_SIZE, BOARD_OL_C)
        self.remaining_stones = MAX_STONES

    def draw(self, screen):
        board = pygame.Rect(BOARD_POS, BOARD_SIZE)

        pygame.draw.rect(screen, BOARD_C, board, border_radius = BORDER_RADIUS)
        self.outline.draw(screen)

    def check_pockets(self, pockets):
        n = 0

        for pocket in pockets:
            print(f"Pocket {n}: {pocket.get_stones()} stones")
            n += 1

    def move_stones(self, screen, index, pockets, player=1): #Remember that you set this default or the turn system is screwed
        pocket = pockets[index]
        n = 1

        while pocket.stones:
            stone = pocket.stones[0]
            next_p = pockets[(index + n) % 14]

            if next_p.is_home:
                if player and next_p.player:
                    stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                    stone.y = next_p.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

                    next_p.stones.append(stone)
                    pocket.stones.pop(0)

                    #player_score += 1
                    self.remaining_stones -= 1

                    n += 1

                elif not player and not next_p.player:
                    stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                    stone.y = next_p.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

                    next_p.stones.append(stone)
                    pocket.stones.pop(0)

                    #cpu_score += 1
                    self.remaining_stones -= 1

                    n += 1
                else:
                    n += 1
                    next_p = pockets[(index + n) % 14]

                    stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                    stone.y = next_p.y + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))

                    next_p.stones.append(stone)
                    pocket.stones.pop(0)

                    n += 1
            else:
                stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                stone.y = next_p.y + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))

                next_p.stones.append(stone)
                pocket.stones.pop(0)

                n += 1

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
