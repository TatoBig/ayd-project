from typing import Union

import pygame
from pygame.surface import Surface, SurfaceType


class GameObject:
    def __init__(self, x: int, y: int, image_name: str):
        self.__x = x
        self.__y = y
        self.__image = pygame.image.load(image_name)

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def image(self) -> Union[Surface, SurfaceType]:
        return self.__image

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y



