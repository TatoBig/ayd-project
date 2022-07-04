import pygame

from .game_object import GameObject
from random import random


class Bullet(GameObject):
    def __init__(self, x: int, y: int, direcction: str, speed: int, damage: float, spread: bool = False):
        super().__init__(x, y, 'bullet.png')
        self.__direction: str = direcction
        self.__speed: int = speed
        self.__damage: float = damage
        self.__spread: bool = spread

    @property
    def damage(self) -> float:
        return self.__damage

    def shoot(self) -> None:
        random_spread: float = random()

        if self.__direction == 'up':
            if self.__spread:
                if random_spread > 0.5:
                    self.move_left(self.__speed)
                else:
                    self.move_right(self.__speed)
            self.move_up(self.__speed)
        if self.__direction == 'down':
            if self.__spread:
                if random_spread > 0.5:
                    self.move_left(self.__speed)
                else:
                    self.move_right(self.__speed)
            self.move_down(self.__speed)
        if self.__direction == 'left':
            if self.__spread:
                if random_spread > 0.5:
                    self.move_up(self.__speed)
                else:
                    self.move_down(self.__speed)
            self.move_left(self.__speed)
        if self.__direction == 'right':
            if self.__spread:
                if random_spread > 0.5:
                    self.move_up(self.__speed)
                else:
                    self.move_down(self.__speed)
            self.move_right(self.__speed)
