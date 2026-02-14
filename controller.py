import pygame
import os
from constants import *
from board import *
from stone import *

class Controller(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.remaining_stones = MAX_STONES
        self.font = pygame.font.SysFont(None, 100)
        self.player = 1
        self.player_score = 0
        self.cpu_score = 0

    def initialize_board(self, screen, pockets):
        board = Board()

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

        pocket_ind = []

        for pocket in pockets:
            if not pocket.is_home:
                for i in range(0, 6):
                    x = pocket.x + ((POCKET_WIDTH / 2) + random.randrange(-30, 30))
                    y = pocket.y + ((POCKET_WIDTH / 2) + random.randrange(-30, 30))

                    pocket.stones.append(Stone(x, y))

            pocket_ind.append(pocket)

        return pocket_ind

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

    def update(self, screen, pocket_ind):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.player:
                    if event.key == pygame.K_1:
                        #print("Key 1 pressed")
                        if pocket_ind[0].stones:
                            self.move_stones(screen, 0, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_2:
                        #print("Key 2 pressed")
                        if pocket_ind[1].stones:
                            self.move_stones(screen, 1, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_3:
                        #print("Key 3 pressed")
                        if pocket_ind[2].stones:
                            self.move_stones(screen, 2, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_4:
                        #print("Key 4 pressed")
                        if pocket_ind[3].stones:
                            self.move_stones(screen, 3, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_5:
                        #print("Key 5 pressed")
                        if pocket_ind[4].stones:
                            self.move_stones(screen, 4, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_6:
                        #print("Key 6 pressed")
                        if pocket_ind[5].stones:
                            self.move_stones(screen, 5, pocket_ind)
                            self.change_player()

                if not self.player:
                    if event.key == pygame.K_7:
                        #print("Key 7 pressed")
                        if pocket_ind[7].stones:
                            self.move_stones(screen, 7, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_8:
                        #print("Key 8 pressed")
                        if pocket_ind[8].stones:
                            self.move_stones(screen, 8, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_9:
                        #print("Key 9 pressed")
                        if pocket_ind[9].stones:
                            self.move_stones(screen, 9, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_0:
                        #print("Key 0 pressed")
                        if pocket_ind[10].stones:
                            self.move_stones(screen, 10, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_MINUS:
                        #print("Key Minus pressed")
                        if pocket_ind[11].stones:
                            self.move_stones(screen, 11, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_EQUALS:
                        #print("Key Equals pressed")
                        if pocket_ind[12].stones:
                            self.move_stones(screen, 12, pocket_ind)
                            self.change_player()
        return True


    def move_stones(self, screen, index, pockets):
        pocket = pockets[index]
        n = 1

        while pocket.stones:
            stone = pocket.stones[0]
            next_p = pockets[(index + n) % 14]

            if next_p.is_home:
                if self.player and next_p.player:
                    stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                    stone.y = next_p.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

                    next_p.stones.append(stone)
                    pocket.stones.pop(0)

                    self.player_score += 1
                    self.remaining_stones -= 1

                    n += 1

                elif not self.player and not next_p.player:
                    stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                    stone.y = next_p.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

                    next_p.stones.append(stone)
                    pocket.stones.pop(0)

                    self.cpu_score += 1
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

    def check_pockets(self, pockets):
        n = 0

        for pocket in pockets:
            print(f"Pocket {n}: {pocket.get_stones()} stones")
            n += 1

    def change_player(self):
        if self.player:
            self.player = 0
        else:
            self.player = 1
