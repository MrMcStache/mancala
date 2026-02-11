import pygame
import os
from constants import *

def draw_board(screen):
    board = pygame.Rect(MAX_WIDTH / 6, MAX_HEIGHT / 6, MAX_WIDTH / 1.5, MAX_HEIGHT / 1.5)

    pygame.draw.rect(screen, "#8a7b4a", board, width = 0, border_radius = BORDER_RADIUS)
