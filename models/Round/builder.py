from __future__ import annotations
from abc import ABC, abstractmethod
from ..game_object.enemy import Enemy
from ..game_object.item import Item


class Builder(ABC):
    @abstractmethod
    def set_enemies(self, enemies: list[Enemy]) -> None:
        raise NotImplementedError

    @abstractmethod
    def set_items(self, items: list[Item]) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def set_time(self, time: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError
    
