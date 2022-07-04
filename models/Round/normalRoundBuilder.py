from ..game_object.item.item import Item
from ..game_object.enemy.enemy import Enemy
from .builder import Builder
from .NormalRound import NormalRound

class NormalBuilder(Builder):
    def __init__(self, round: NormalRound):
        self.__round: NormalRound = round

    def reset(self) -> None:
        self.__round = NormalRound()

    def set_enemies(self, enemies: list[Enemy]) -> None:
        self.__round.enemies = enemies

    def set_items(self, items: list[Item]) -> None:
        self.__round.items = items

    def set_time(self, time: float) -> None:
        self.__round.time = time

    def get_round(self):
        return self.__round