from threading import Thread
from time import sleep
from typing import Optional
from ..game_object import GameObject

from .character import Character
from ..bullet import Bullet


class Robot(Character):
    def __init__(self):
        self.__cooldown: int = 1
        self.__current_counter: int = 0
        self.__bullet_speed: int = 3
        self.__bullet_damage: float = 0.02

        cooldown_loop = Thread(target=self._cooldown_loop)
        cooldown_loop.start()

    @property
    def cooldown(self) -> int:
        return self.__cooldown

    @property
    def current_counter(self) -> int:
        return self.__current_counter

    @property
    def bullet_damage(self) -> float:
        return self.__bullet_damage

    @property
    def bullet_speed(self) -> int:
        return self.__bullet_speed

    @cooldown.setter
    def cooldown(self, cooldown: int) -> None:
        self.__cooldown = cooldown

    @current_counter.setter
    def current_counter(self, current_counter: int) -> None:
        self.__current_counter = current_counter

    @bullet_damage.setter
    def bullet_damage(self, bullet_damage: float) -> None:
        self.__bullet_damage = bullet_damage

    @bullet_speed.setter
    def bullet_speed(self, bullet_speed: int) -> None:
        self.__bullet_speed = bullet_speed

    def try_shoot(self, direction: str, player: GameObject) -> Optional[Bullet]:
        if self.__current_counter >= self.__cooldown:
            self.__current_counter = 0
            return self.shoot(direction, player)

    def shoot(self, direction: str, player: GameObject) -> Bullet:
        bullet = Bullet(player.x, player.y, direction, self.__bullet_speed, self.__bullet_damage)
        return bullet

    def _cooldown_loop(self):
        while True:
            sleep(0.01)
            if self.__current_counter < self.__cooldown:
                self.__current_counter += 1

