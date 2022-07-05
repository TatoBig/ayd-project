from ..game_object.item.item import Item
from ..game_object.enemy.enemy import Enemy
from .builder import Builder
from .BossRound import BossRound


class BossRoundBuilder(Builder):
    def __init__(self):
        self.__round: BossRound = BossRound()

    def reset(self) -> None:
        self.__round = BossRound()

    def set_enemies(self, enemies: list[Enemy]) -> None:
        self.__round.enemies = enemies

    def set_items(self, items: list[Item]) -> None:
        self.__round.items = items

    def set_time(self, time: float) -> None:
        self.__round.time = time

    def get_result(self) -> BossRound:
        return self.__round
