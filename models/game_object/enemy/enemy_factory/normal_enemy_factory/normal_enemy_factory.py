from ..enemy_factory import EnemyFactory
from ...normie import Normie
from ...boss import Boss
from ...crazy import Crazy
from .normal_normie import NormalNormie
from .normal_boss import NormalBoss
from .normal_crazy import NormalCrazy
from .....store import Store
from .....utilities import Utilities


class NormalEnemyFactory(EnemyFactory):
    def __init__(self):
        self.__utilities: Utilities = Utilities()
        self.__store: Store = Store()

    def create_normie(self) -> Normie:
        location = self.__utilities.random_border_location()
        return NormalNormie(location[0], location[1], 20, self.__store.get_random_player(), 20)

    def create_crazy(self) -> Crazy:
        location = self.__utilities.random_border_location()
        return NormalCrazy(location[0], location[1], 20, self.__store.get_random_player(), 15)

    def create_boss(self) -> Boss:
        location = self.__utilities.random_border_location()
        return NormalBoss(location[0], location[1], 40, self.__store.get_random_player(), 80)