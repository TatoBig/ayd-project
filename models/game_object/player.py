import pygame

from .game_object import GameObject
from .character import Character
from .character import Sniper, Fish, Robot
from .item.item import Item


class Player(GameObject):
    def __init__(self, x: int, y: int, character: Character):
        super().__init__(x, y, 'intro_ball.gif')
        self.__character: Character = character
        self.__items: list[Item] = []
        self.__health: int = 3

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, character: Character):
        self.__character = character

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health: int):
        self.__health = health

    def shoot(self, direction: str):
        return self.__character.try_shoot(direction, self)

    def upgrade_character(self, item: Item):
        self.__character = item.activate(self.__character)

    def draw_cooldown(self, screen):
        print(self.__character.current_counter)
        print(self.__character.cooldown)
        pygame.draw.rect(screen, (200, 200, 200),
                         [self.x, self.y - 25, (self.__character.current_counter /
                                                self.__character.cooldown * 100), 4], 0)
        for hp in range(1, self.__health + 1):
            if self.__health != 0:
                pygame.draw.rect(screen, (255, 0, 0),
                                 [self.x - ((hp - 1) * 15), self.y - 25, 8, 8], 0)

    def add_item(self, item: Item):
        self.__items.append(item)

    def hit(self):
        self.__health -= 1
