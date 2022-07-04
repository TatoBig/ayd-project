from models.game_object.enemy import enemy_factory
from .builder import Builder
from ..game_object.enemy import EnemyFactory, HardEnemyFactory, NormalEnemyFactory

class Director:
    def __init__(self, builder: Builder, mode: str):
        self.__factory: EnemyFactory = None
        if mode == "normal":
            self.__factory = NormalEnemyFactory()
        elif mode == "hard":
            self.__factory = HardEnemyFactory()
        self.__builder: Builder = builder
        
    def make_round1(self):
        enemies = []
        enemies.append(self.__factory.create_normie(0,0,None))
        enemies.append(self.__factory.create_normie(0,0,None))
        self.__builder.set_enemies(enemies)
        self.__builder.set_time(30000)
    
    
    