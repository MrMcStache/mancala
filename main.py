import pygame
import os
from constants import *
from board import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    pockets = pygame.sprite.Group()
    stones = pygame.sprite.Group()

    Board.containers = (updatable, drawable)
    Pocket.containers = (updatable, drawable, pockets)
    Home.containers = (updatable, drawable, pockets)
    #Stone.containers = (updatable, drawable, stones)

    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    board = Board()
    initialize_pockets()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BG_C)

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
