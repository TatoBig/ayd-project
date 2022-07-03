from time import sleep
from typing import Optional

from ..character import Character
from .character_decorator import CharacterDecorator
from ... import GameObject, Bullet


class Wave(CharacterDecorator):
    def __init__(self, character: Character):
        super().__init__(character)
        self.__shots: int = 0
        self.__special_shots: int = 0

    def try_shoot(self, direction: str, player: GameObject) -> Optional[Bullet]:
        if self.current_counter >= self.cooldown:
            self.current_counter = 0
            self.__shots += 1

            if self.__shots == 3:
                self.__shots = 0
                self.__special_shots = 5

            return self.shoot(direction, player)

        if self.__special_shots > 0:
            self.__special_shots -= 1
            if self.__special_shots == 4:
                return self.shoot('up', player)
            if self.__special_shots == 3:
                return self.shoot('right', player)
            if self.__special_shots == 2:
                return self.shoot('down', player)
            if self.__special_shots == 1:
                return self.shoot('left', player)

    def shoot(self, direction: str, player: GameObject) -> Bullet:
        bullet = Bullet(player.x, player.y, direction, self.bullet_speed, self.bullet_damage)
        return bullet

    def _cooldown_loop(self):
        while True:
            sleep(0.05)
            self.current_counter += 1


