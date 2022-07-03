from .game_object import GameObject
from .character import Character
from .character import Sniper
from .character import Robot
from .item import Item


class Player(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'intro_ball.gif')
        self.__character: Character = Robot()

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
