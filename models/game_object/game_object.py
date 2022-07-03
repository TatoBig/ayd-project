from typing import Union, Optional

import pygame
from pygame.rect import Rect, RectType
from pygame.surface import Surface, SurfaceType


class GameObject:
    def __init__(self, x: int, y: int, image_name: str):
        self.__x: int = x
        self.__y: int = y
        self.__image: Union[Surface, SurfaceType] = pygame.image.load(image_name)
        self.__hitbox: Union[Rect, RectType] = self.__image.get_rect()

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def image(self) -> Union[Surface, SurfaceType]:
        return self.__image

    @property
    def hitbox(self) -> Union[Rect, RectType]:
        return self.__hitbox

    def move_up(self, movement: Optional[int] = 1):
        self.__y -= movement

    def move_down(self, movement: Optional[int] = 1):
        self.__y += movement

    def move_left(self, movement: Optional[int] = 1):
        self.__x -= movement

    def move_right(self, movement: Optional[int] = 1):
        self.__x += movement
