from time import sleep
from typing import Optional

from ..character import Character
from .character_decorator import CharacterDecorator
from ... import GameObject, Bullet


class Double(CharacterDecorator):
    def __init__(self, character: Character):
        super().__init__(character)
        self.__double_shot: bool = True
        self.__condition: bool = True

    def try_shoot(self, direction: str, player: GameObject) -> Optional[Bullet]:
        if self.current_counter >= self.cooldown:
            if self.__double_shot is False:
                self.__double_shot = True
            elif self.__condition is False:
                self.__condition = True

        bullet = super().try_shoot(direction, player)
        if bullet is not None:
            return bullet

        if self.__double_shot and self.__condition:
            self.current_counter = round(self.cooldown * 0.8)
            self.__double_shot = False
            self.__condition = False









