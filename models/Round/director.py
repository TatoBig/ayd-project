from models.game_object.enemy import enemy_factory
from .builder import Builder
from ..game_object.enemy import EnemyFactory, HardEnemyFactory, NormalEnemyFactory
from ..store import Store
from ..utilities import Utilities


class Director:
    def __init__(self, builder: Builder, mode: str):
        self.__factory: EnemyFactory = None
        self.__utilities: Utilities = Utilities()
        self.__store: Store = Store()
        if mode == "normal":
            self.__factory = NormalEnemyFactory()
        elif mode == "hard":
            self.__factory = HardEnemyFactory()
        self.__builder: Builder = builder

    def make_rounds(self, current_round: int):
        if current_round == 1:
            enemies = [self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(1500)

        if current_round == 2:
            enemies = [self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(3000)

        if current_round == 3:
            enemies = [self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(1000)

        if current_round == 4:
            enemies = [self.__factory.create_crazy(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(1500)

        if current_round == 5:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(1500)

        if current_round == 6:
            enemies = [self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
    
    
