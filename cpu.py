import pygame
import os
import random
from controller import *

class CPU():
    def __init__(self):
        self.delay = 100

    def must_play(self, controller, screen, pockets):
        for pocket in pockets[7:13]:
            if pocket.must_play:
                pocket.must_play = False

                print(f"CPU MUST PLAY pocket {pocket.p_index} with {len(pocket.stones)} stones.")
                controller.move_stones(screen, pocket.p_index, pockets)

                pygame.time.delay(self.delay)

                return True

        pygame.time.delay(self.delay)

        return False

    def is_extra_turn(self, controller, screen, pockets):
        for pocket in pockets[7:13]:
            if pocket.stones:
                dist_to_home = 13 - pocket.p_index

                if (len(pocket.stones) % 13) == dist_to_home:
                    print(f"CPU moves for extra turn from pocket {pocket.p_index} with {len(pocket.stones)} stones.")
                    controller.move_stones(screen, pocket.p_index, pockets)

                    pygame.time.delay(self.delay)

                    return True

        pygame.time.delay(self.delay)

        return False

    def can_steal(self, controller, screen, pockets):
        for pocket in pockets[7:13]:
            if pocket.stones:
                last_p = (len(pocket.stones) + pocket.p_index) % 13

                if last_p >= 7:
                    if not pockets[last_p].stones:
                        print(f"CPU steals, moving from pocket {pocket.p_index} with {len(pocket.stones)} stones to land in pocket {last_p}.")
                        controller.move_stones(screen, pocket.p_index, pockets)

                        pygame.time.delay(self.delay)

                        return True

        pygame.time.delay(self.delay)

        return False

    def can_score(self, controller, screen, pockets):
        can_play = []

        for pocket in pockets[7:13]:
            if pocket.stones:
                dist_to_home = 13 - pocket.p_index

                if len(pocket.stones) >= dist_to_home:
                    can_play.append(pocket.p_index)

        if can_play:
            choice = can_play[random.randrange(0, len(can_play))]

            print(f"CPU moves to score from pocket {pocket.p_index} with {len(pocket.stones)} stones.")
            controller.move_stones(screen, choice, pockets)

            pygame.time.delay(self.delay)

            return True

        pygame.time.delay(self.delay)

        return False

    def choose_random(self, controller, screen, pockets):
        can_play = []

        for pocket in pockets[7:13]:
            if pocket.stones:
                can_play.append(pocket.p_index)

        if can_play:
            choice = can_play[random.randrange(0, len(can_play))]

            print(f"CPU randomly chose pocket {choice} with {len(pockets[choice].stones)} stones.")
            controller.move_stones(screen, choice, pockets)

            pygame.time.delay(self.delay)

    def check_moves(self, controller, screen, pockets):
        if self.must_play(controller, screen, pockets):
            controller.change_player()
        elif self.is_extra_turn(controller, screen, pockets):
            controller.change_player()
        elif self.can_steal(controller, screen, pockets):
            controller.change_player()
        elif self.can_score(controller, screen, pockets):
            controller.change_player()
        else:
            self.choose_random(controller, screen, pockets)
            controller.change_player()

    def update(self, controller, screen, pockets):
        if not controller.player:
            self.check_moves(controller, screen, pockets)
