from time import sleep
from threading import Thread
from .. import Player, GameObject
from random import random, randint
from .enemy import Enemy

import pygame


class Crazy(Enemy):
    def __init__(self, x: int, y: int, speed: int, player: Player, health: float):
        super().__init__(x, y, speed, player, health)

    def _keep_tracking(self):
        while True:
            if random() > 0.4:
                sleep(self.speed / 1000)
                if self.y > self.track_player.y + self.track_player.hitbox.centery:
                    self.move_up(2)
                else:
                    self.move_down(4)
                if self.x > self.track_player.x + self.track_player.hitbox.centerx:
                    self.move_left(3)
                else:
                    self.move_right(1)
            else:
                random_movement = randint(1, 4)
                if random_movement == 1:
                    self.move_up(8)
                if random_movement == 2:
                    self.move_down(8)
                if random_movement == 3:
                    self.move_left(8)
                if random_movement == 4:
                    self.move_right(8)





