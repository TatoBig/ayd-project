from .builder import Builder
from ..game_object.item import Double, Damage, Quad
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
            self.__builder.set_items([Quad()])

        if current_round == 2:
            enemies = [self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(3000)
            self.__builder.set_items([Damage()])

        if current_round == 3:
            enemies = [self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(1000)
            self.__builder.set_items([])

        if current_round == 4:
            enemies = [self.__factory.create_crazy(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(1500)
            self.__builder.set_items([Quad()])

        if current_round == 5:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(1500)
            self.__builder.set_items([])

        if current_round == 6:
            enemies = [self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([Double(), Damage()])

        if current_round == 7:
            enemies = [self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 8:
            enemies = [self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie(),
                       self.__factory.create_normie(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 9:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([Double()])

        if current_round == 10:
            enemies = [self.__factory.create_boss(), self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])
        if current_round == 11:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])
        if current_round == 12:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])
        if current_round == 13:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])
        if current_round == 14:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])
        
        if current_round == 15:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 16:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_normie(),
                       self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 17:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_crazy(),
                       self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 18:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 19:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 20:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss(),
                       self.__factory.create_boss()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 21:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 22:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 23:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(), 
                       self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 24:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 25:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 26:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie(),
                       self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie(),
                       self.__factory.create_normie(), self.__factory.create_normie(), self.__factory.create_normie()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 27:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 28:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy()
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

        if current_round == 29:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_crazy(), self.__factory.create_crazy()
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])
        
        if current_round == 30:
            enemies = [self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_normie(),
                       self.__factory.create_crazy(), self.__factory.create_normie(), self.__factory.create_boss(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_crazy(), self.__factory.create_crazy(), self.__factory.create_crazy(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss(),
                       self.__factory.create_boss(), self.__factory.create_boss(), self.__factory.create_boss()]
            self.__builder.set_enemies(enemies)
            self.__builder.set_time(2500)
            self.__builder.set_items([])

    
