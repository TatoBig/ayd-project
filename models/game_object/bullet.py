import pygame

from .game_object import GameObject


class Bullet(GameObject):
    def __init__(self, x: int, y: int, direcction):
        super().__init__(x, y, 'bullet.png')
        self.__direction = direcction
        self.__speed = 3

    def shoot(self):
        if self.__direction == 'up':
            self.y -= self.__speed
        if self.__direction == 'down':
            self.y += self.__speed
        if self.__direction == 'left':
            self.x -= self.__speed
        if self.__direction == 'right':
            self.x += self.__speed


