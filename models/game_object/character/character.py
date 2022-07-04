from abc import ABC, abstractmethod
from typing import Optional

from ..bullet import Bullet
from ..game_object import GameObject


class Character(ABC):
    @abstractmethod
    def try_shoot(self, direction: str, player: GameObject) -> Optional[Bullet]:
        raise NotImplementedError

    @abstractmethod
    def shoot(self, direction: str, player: GameObject) -> Bullet:
        raise NotImplementedError

    @abstractmethod
    def _cooldown_loop(self) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def cooldown(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def current_counter(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def bullet_damage(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def bullet_speed(self) -> int:
        raise NotImplementedError

    @cooldown.setter
    @abstractmethod
    def cooldown(self, cooldown: int) -> None:
        raise NotImplementedError

    @current_counter.setter
    @abstractmethod
    def current_counter(self, current_counter: int) -> None:
        raise NotImplementedError

    @bullet_damage.setter
    @abstractmethod
    def bullet_damage(self, bullet_damage: float) -> None:
        raise NotImplementedError

    @bullet_speed.setter
    @abstractmethod
    def bullet_speed(self, bullet_speed: int) -> None:
        raise NotImplementedError
