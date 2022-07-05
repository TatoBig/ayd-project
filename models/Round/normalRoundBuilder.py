from ..game_object.item.item import Item
from ..game_object.enemy.enemy import Enemy
from .builder import Builder
from .NormalRound import NormalRound


class NormalRoundBuilder(Builder):
    def __init__(self):
        self.__round: NormalRound = NormalRound()

    def reset(self) -> None:
        self.__round = NormalRound()

    def set_enemies(self, enemies: list[Enemy]) -> None:
        self.__round.enemies = enemies

    def set_items(self, items: list[Item]) -> None:
        self.__round.items = items

    def set_time(self, time: float) -> None:
        self.__round.time = time

    def get_result(self) -> NormalRound:
        return self.__round
