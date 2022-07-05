from ..enemy_factory import EnemyFactory
from ...normie import Normie
from ...boss import Boss
from ...crazy import Crazy
from .hard_normie import HardNormie
from .hard_boss import HardBoss
from .hard_crazy import HardCrazy
from .....store import Store
from .....utilities import Utilities


class HardEnemyFactory(EnemyFactory):
    def __init__(self):
        self.__utilities: Utilities = Utilities()
        self.__store: Store = Store()

    def create_normie(self) -> Normie:
        location = self.__utilities.random_border_location()
        return HardNormie(location[0], location[1], 15, self.__store.get_random_player(), 25)

    def create_crazy(self) -> Crazy:
        location = self.__utilities.random_border_location()
        return HardCrazy(location[0], location[1], 18, self.__store.get_random_player(), 20)

    def create_boss(self) -> Boss:
        location = self.__utilities.random_border_location()
        return HardBoss(location[0], location[1], 30, self.__store.get_random_player(), 100)
