import pygame
import os
from constants import *
from board import *
from stone import *

def check_stones(pockets):
    n = 0

    for pocket in pockets:
        print(f"Pocket {n}: {pocket.get_stones()} stones")
        n += 1

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    pockets = pygame.sprite.Group()
    stones = pygame.sprite.Group()

    Board.containers = (updatable, drawable)
    Pocket.containers = (updatable, drawable, pockets)
    Stone.containers = (updatable, drawable, stones)

    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    board = Board()
    initialize_pockets()
    initialize_stones(screen, pockets)

    #check_stones(pockets)

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
