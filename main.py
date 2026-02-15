import pygame
import os
from constants import *
from controller import *

def main():
    pygame.init()
    pygame.key.set_repeat()

    drawable = pygame.sprite.Group()
    pockets = pygame.sprite.Group()
    stones = pygame.sprite.Group()

    Board.containers = (drawable)
    Pocket.containers = (drawable, pockets)
    Stone.containers = (drawable, stones)

    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    controller = Controller()
    pocket_ind = controller.initialize_board(screen, pockets)
    game = True

    while game:
        screen.fill(BG_C)

        if not controller.update(screen, pocket_ind):
            game = False

        for drawing in drawable:
            drawing.draw(screen)

        controller.draw(screen, pocket_ind)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
