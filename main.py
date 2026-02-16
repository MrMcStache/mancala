import pygame
import os
from constants import *
from controller import *
from cpu import *

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
    cpu = CPU()
    pocket_ind = controller.initialize_board(screen, pockets, stones)

    while True:
        screen.fill(BG_C)

        if not controller.update(screen, pocket_ind):
            return False

        if controller.cpu_player:
            cpu.update(controller, screen, pocket_ind)

        for drawing in drawable:
            drawing.draw(screen)

        controller.draw(screen, pocket_ind)

        if controller.game_over and controller.restart:
            controller.game_over = False
            controller.restart = False
            controller.new_game = True
            controller.player = 1
            controller.cpu_player = False
            pygame.sprite.Group.empty(pockets)
            pygame.sprite.Group.empty(stones)
            pocket_ind = controller.initialize_board(screen, pockets, stones)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
