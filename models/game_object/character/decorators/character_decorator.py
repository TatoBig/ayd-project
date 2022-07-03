from time import sleep
from typing import Optional

from ..character import Character
from ... import GameObject, Bullet


class CharacterDecorator(Character):
    def __init__(self, character: Character):
        self.__decorated_character: Character = character

    def get_character(self) -> Character:
        return self.__decorated_character

    @property
    def cooldown(self) -> int:
        return self.__decorated_character.cooldown

    @property
    def current_counter(self) -> int:
        return self.__decorated_character.current_counter

    @property
    def bullet_damage(self) -> float:
        return self.__decorated_character.bullet_damage

    @property
    def bullet_speed(self) -> int:
        return self.__decorated_character.bullet_speed

    @cooldown.setter
    def cooldown(self, cooldown: int) -> None:
        self.__decorated_character.cooldown = cooldown

    @current_counter.setter
    def current_counter(self, current_counter: int) -> None:
        self.__decorated_character.current_counter = current_counter

    @bullet_damage.setter
    def bullet_damage(self, bullet_damage: float) -> None:
        self.__decorated_character.bullet_damage = bullet_damage

    @bullet_speed.setter
    def bullet_speed(self, bullet_speed: int) -> None:
        self.__decorated_character.bullet_speed = bullet_speed

    def try_shoot(self, direction: str, player: GameObject) -> Optional[Bullet]:
        if self.__decorated_character.current_counter >= self.__decorated_character.cooldown:
            self.__decorated_character.current_counter = 0
            return self.shoot(direction, player)

    def shoot(self, direction: str, player: GameObject) -> Bullet:
        bullet = Bullet(player.x, player.y, direction, self.__decorated_character.bullet_speed,
                        self.__decorated_character.bullet_damage)
        return bullet

    def _cooldown_loop(self):
        while True:
            sleep(0.05)
            self.__decorated_character.current_counter += 1

