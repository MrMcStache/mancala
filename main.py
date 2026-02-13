import pygame
import os
from constants import *
from controller import *
from board import *
from stone import *

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
    board = Board()
    initialize_pockets()
    pocket_ind = initialize_stones(screen, pockets)
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if controller.player:
                    if event.key == pygame.K_1:
                        #print("Key 1 pressed")
                        board.move_stones(screen, 0, pocket_ind)
                        controller.change_player()
                    elif event.key == pygame.K_2:
                        #print("Key 2 pressed")
                        board.move_stones(screen, 1, pocket_ind)
                        controller.change_player()
                    elif event.key == pygame.K_3:
                        #print("Key 3 pressed")
                        board.move_stones(screen, 2, pocket_ind)
                        controller.change_player()
                    elif event.key == pygame.K_4:
                        #print("Key 4 pressed")
                        board.move_stones(screen, 3, pocket_ind)
                        controller.change_player()
                    elif event.key == pygame.K_5:
                        #print("Key 5 pressed")
                        board.move_stones(screen, 4, pocket_ind)
                        controller.change_player()
                    elif event.key == pygame.K_6:
                        #print("Key 6 pressed")
                        board.move_stones(screen, 5, pocket_ind)
                        controller.change_player()

                if not controller.player:
                    if event.key == pygame.K_7:
                        #print("Key 7 pressed")
                        board.move_stones(screen, 7, pocket_ind, 0)
                        controller.change_player()
                    elif event.key == pygame.K_8:
                        #print("Key 8 pressed")
                        board.move_stones(screen, 8, pocket_ind, 0)
                        controller.change_player()
                    elif event.key == pygame.K_9:
                        #print("Key 9 pressed")
                        board.move_stones(screen, 9, pocket_ind, 0)
                        controller.change_player()
                    elif event.key == pygame.K_0:
                        #print("Key 0 pressed")
                        board.move_stones(screen, 10, pocket_ind, 0)
                        controller.change_player()
                    elif event.key == pygame.K_EQUALS:
                        #print("Key Equals pressed")
                        board.move_stones(screen, 12, pocket_ind, 0)
                        controller.change_player()
                    elif event.key == pygame.K_MINUS:
                        #print("Key Minus pressed")
                        board.move_stones(screen, 11, pocket_ind, 0)
                        controller.change_player()

                if event.key == pygame.K_SPACE:
                    #print("Space Key pressed")
                    board.check_pockets(pockets)

        if board.remaining_stones == 0:
            print("GAME OVER: No stones left")
            #game = False

        screen.fill(BG_C)

        for drawing in drawable:
            drawing.draw(screen)

        controller.draw(screen, pockets)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
