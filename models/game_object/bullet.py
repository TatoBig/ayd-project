import pygame

from .game_object import GameObject


class Bullet(GameObject):
    def __init__(self, x: int, y: int, direcction: str, speed: int, damage: float):
        super().__init__(x, y, 'bullet.png')
        self.__direction: str = direcction
        self.__speed: int = speed
        self.__damage: float = damage

    @property
    def damage(self) -> float:
        return self.__damage

    def shoot(self) -> None:
        if self.__direction == 'up':
            self.move_up(self.__speed)
        if self.__direction == 'down':
            self.move_down(self.__speed)
        if self.__direction == 'left':
            self.move_left(self.__speed)
        if self.__direction == 'right':
            self.move_right(self.__speed)
