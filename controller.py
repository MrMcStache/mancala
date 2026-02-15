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

        self.font = pygame.font.SysFont(None, 100)
        self.player = 1

    def initialize_board(self, screen, pockets):
        board = Board()

        px = BOARD_X + 170
        py = BOARD_Y + 210

        for p in range(0, 14):
            if p >= 6:
                px = BOARD_X + 1130
                if (p + 1) % 7 == 0:
                    home = Pocket(px - (160 * (p - 6)), py - 200, p, True)
                else:
                    pocket = Pocket(px - (160 * (p - 6)), py - 200, p)
            else:
                pocket = Pocket(px + (160 * p), py, p)

        pocket_ind = []

        for pocket in pockets:
            if not pocket.is_home:
                for i in range(0, 6):
                    x = pocket.x + ((POCKET_WIDTH / 2) + random.randrange(-30, 30))
                    y = pocket.y + ((POCKET_WIDTH / 2) + random.randrange(-30, 30))

                    pocket.stones.append(Stone(x, y))

            pocket_ind.append(pocket)

        return pocket_ind

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

    def move(self, stone, pocket, next_p):
        stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
        stone.y = next_p.y + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))

        next_p.stones.append(stone)
        pocket.stones.remove(stone)

    def move_to_home(self, stone, pockets, next_p, player):
        if player:
            home = pockets[6]
            stone.x = home.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
            stone.y = home.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))
        else:
            home = pockets[13]
            stone.x = home.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
            stone.y = home.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

        home.stones.append(stone)
        next_p.stones.remove(stone)

    def is_last_stone(self, pocket):
        if len(pocket.stones) == 1:
            return True
        else:
            return False

    def take_opposite(self, pocket, next_p, pockets, player):
        if player:
            opposite = pockets[next_p.p_index + (12 - (2 * next_p.p_index))]
        elif not player:
            opposite = pockets[next_p.p_index - (12 + (2 * (next_p.p_index - 12)))]

        while opposite.stones:
            for stone in opposite.stones:
                self.move_to_home(stone, pockets, opposite, player)

    def check_empty_sides(self, pockets):
        for pocket in pockets[0:6]:
            if not pocket.stones:
                continue
            else:
                for p in pockets[7:13]:
                    if not p.stones:
                        continue
                    else:
                        return False

                if not self.player:
                    self.change_player()

                return self.check_no_more_moves(pockets, 0, 6, 1)

        if self.player:
            self.change_player()

        return self.check_no_more_moves(pockets, 7, 13, 0)

    def check_no_more_moves(self, pockets, i, j, player):
        for pocket in pockets[i:j]:
            n = pocket.get_stones()
            dist = 14 - pocket.p_index

            if n >= dist:
                #pocket.must_play = True
                return False

        for pocket in pockets[i:j]:
            while pocket.stones:
                for stone in pocket.stones:
                    self.move_to_home(stone, pockets, pocket, player)

        return True

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
            if self.check_empty_sides(pocket_ind):
                player_score = len(pocket_ind[6].stones)
                cpu_score = len(pocket_ind[13].stones)

                if player_score > cpu_score:
                    print(f"Game Over: Player Wins! | Player: {player_score} | CPU: {cpu_score} |")
                elif player_score < cpu_score:
                    print(f"Game Over: CPU Wins! | CPU: {cpu_score} | Player: {player_score} |")
                elif player_score == cpu_score:
                    print(f"Game Over: Tie Game! | Player: {player_score} = CPU: {cpu_score} |")

                return False

            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.player:
                    if event.key == pygame.K_1:
                        if pocket_ind[0].stones:
                            self.move_stones(screen, 0, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_2:
                        if pocket_ind[1].stones:
                            self.move_stones(screen, 1, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_3:
                        if pocket_ind[2].stones:
                            self.move_stones(screen, 2, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_4:
                        if pocket_ind[3].stones:
                            self.move_stones(screen, 3, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_5:
                        if pocket_ind[4].stones:
                            self.move_stones(screen, 4, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_6:
                        if pocket_ind[5].stones:
                            self.move_stones(screen, 5, pocket_ind)
                            self.change_player()

                if not self.player:
                    if event.key == pygame.K_7:
                        if pocket_ind[7].stones:
                            self.move_stones(screen, 12, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_8:
                        if pocket_ind[8].stones:
                            self.move_stones(screen, 11, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_9:
                        if pocket_ind[9].stones:
                            self.move_stones(screen, 10, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_0:
                        if pocket_ind[10].stones:
                            self.move_stones(screen, 9, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_MINUS:
                        if pocket_ind[11].stones:
                            self.move_stones(screen, 8, pocket_ind)
                            self.change_player()
                    elif event.key == pygame.K_EQUALS:
                        if pocket_ind[12].stones:
                            self.move_stones(screen, 7, pocket_ind)
                            self.change_player()
        return True

    def move_stones(self, screen, index, pockets):
        extra_turn = False
        pocket = pockets[index]
        n = 1

        while pocket.stones:
            stone = pocket.stones[0]
            next_p = pockets[(index + n) % 14]

            if next_p.is_home:
                if self.player and next_p.player:
                    stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                    stone.y = next_p.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

                    if self.is_last_stone(pocket):
                        extra_turn = True

                    next_p.stones.append(stone)
                    pocket.stones.remove(stone)

                    n += 1
                elif not self.player and not next_p.player:
                    stone.x = next_p.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                    stone.y = next_p.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

                    if self.is_last_stone(pocket):
                        extra_turn = True

                    next_p.stones.append(stone)
                    pocket.stones.remove(stone)

                    n += 1
                else:
                    n += 1
                    next_p = pockets[(index + n) % 14]

                    if (self.is_last_stone(pocket) and not next_p.stones):
                        self.move(stone, pocket, next_p)

                        if (self.player and next_p.p_index in range(0, 6)) or (not self.player and next_p.p_index in range(7, 13)):
                            self.take_opposite(pocket, next_p, pockets, self.player)

                            self.move_to_home(stone, pockets, next_p, self.player)

                    else:
                        self.move(stone, pocket, next_p)

                        n += 1
            else:
                if (self.is_last_stone(pocket) and not next_p.stones):
                    self.move(stone, pocket, next_p)

                    if (self.player and next_p.p_index in range(0, 6)) or (not self.player and next_p.p_index in range(7, 13)):
                        self.take_opposite(pocket, next_p, pockets, self.player)

                        if self.player:
                            home = pockets[6]
                            stone.x = home.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                            stone.y = home.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))
                        else:
                            home = pockets[13]
                            stone.x = home.x + ((POCKET_WIDTH / 2) + random.randrange(-STONE_RANDOM, STONE_RANDOM))
                            stone.y = home.y + ((HOME_HEIGHT / 2) + random.randrange(-125, 125))

                        home.stones.append(stone)
                        next_p.stones.remove(stone)
                else:
                    self.move(stone, pocket, next_p)

                    n += 1

        if extra_turn:
            self.change_player()
