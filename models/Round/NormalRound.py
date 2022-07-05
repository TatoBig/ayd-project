from ..game_object.item.item import Item
from ..game_object.enemy.enemy import Enemy


class NormalRound:
    def __init__(self):
        self.__enemies: list[Enemy] = []
        self.__items: list[Item] = []
        self.__is_clean: bool = False
        self.__time: float = None

    @property
    def enemies(self) -> list[Enemy]:
        return self.__enemies

    @enemies.setter
    def enemies(self, enemies: list[Enemy]) -> None:
        self.__enemies = enemies

    @property
    def items(self) -> list[Item]:
        return self.__items

    @items.setter
    def items(self, items: list[Item]) -> None:
        self.__items = items

    @property
    def is_clean(self) -> bool:
        return self.__is_clean

    @is_clean.setter
    def is_clean(self, is_clean: bool) -> None:
        self.__is_clean = is_clean

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, time: float) -> None:
        self.__time = time