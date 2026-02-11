import pygame
import os
from constants import *

def draw_board(screen):
    board = pygame.Rect(BOARD_POS, BOARD_SIZE)

    pygame.draw.rect(screen, BOARD_C, board, border_radius = BORDER_RADIUS)
    pygame.draw.rect(screen, BOARD_OL_C, board, width = 10, border_radius = BORDER_RADIUS)

    px = BOARD_X + 10
    py = BOARD_Y + 10

    for p in range(0, 14):
        if p > 7:
            px = BOARD_X + 1130
            pygame.draw.rect(screen, POCKET_C, pygame.Rect((px - (160 * (p - 7)), py + 200), POCKET_SIZE), border_radius = P_BORDER_RADIUS)
            pygame.draw.rect(screen, POCKET_OL_C, pygame.Rect((px - (160 * (p - 7)), py + 200), POCKET_SIZE), width = 3, border_radius = P_BORDER_RADIUS)
        else:
            if p % 7 == 0:
                pygame.draw.rect(screen, POCKET_C, pygame.Rect((px + (160 * p), py), HOME_SIZE), border_radius = P_BORDER_RADIUS)
                pygame.draw.rect(screen, POCKET_OL_C, pygame.Rect((px + (160 * p), py), HOME_SIZE), width = 3, border_radius = P_BORDER_RADIUS)
            else:
                pygame.draw.rect(screen, POCKET_C, pygame.Rect((px + (160 * p), py), POCKET_SIZE), border_radius = P_BORDER_RADIUS)
                pygame.draw.rect(screen, POCKET_OL_C, pygame.Rect((px + (160 * p), py), POCKET_SIZE), width = 3, border_radius = P_BORDER_RADIUS)
