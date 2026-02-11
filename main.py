import pygame
import os
from constants import *
from draw_board import *

def main():
    pygame.init()
    print("Welcome to mancala, how mancala are you?")

    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#e0edb7")
        draw_board(screen)

        #Loop logic here

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
