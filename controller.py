import pygame
import os
from constants import *

class Controller(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.font = pygame.font.SysFont(None, 100)
        self.player = 1

    def draw(self, screen, pockets):
        if self.player:
            p = self.player
        else:
            p = 2

        cur_player = pygame.font.Font.render(self.font, f"Player {p}'s turn", 1, TEXT_C)
        cur_player_rect = cur_player.get_rect()
        cur_player_rect.center = (MAX_WIDTH / 2, MAX_HEIGHT / 6)
        screen.blit(cur_player, cur_player_rect)

        for pocket in pockets:
            x = pocket.x + (POCKET_WIDTH / 2)

            if pocket.is_home:
                y = pocket.y + (HOME_HEIGHT / 2)
            else:
                y = pocket.y + (POCKET_WIDTH / 2)

            count = pocket.get_stones()

            score = pygame.font.Font.render(self.font, f"{count}", 1, SCORE_C)
            score_rect = score.get_rect()
            score_rect.center = (x, y)
            screen.blit(score, score_rect)

    def change_player(self):
        if self.player:
            self.player = 0
        else:
            self.player = 1
