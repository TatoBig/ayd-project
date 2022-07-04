import pygame

from .game_object import GameObject
from .character import Character
from .character import Sniper, Fish, Robot
from .item import Item


class Player(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'intro_ball.gif')
        self.__character: Character = Fish()
        self.__items: list[Item] = []

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, character: Character):
        self.__character = character

    def shoot(self, direction: str):
        return self.__character.try_shoot(direction, self)

    def upgrade_character(self, item: Item):
        self.__character = item.activate(self.__character)

    def draw_cooldown(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         [self.x, self.y - 25, ((self.__character.current_counter + 1) /
                                                self.__character.cooldown * 100), 10], 0)
        pygame.draw.rect(screen, (255, 255, 0),
                         [self.x, self.y - 25, 100, 10], 2)

    def add_item(self, item: Item):
        self.__items.append(item)
