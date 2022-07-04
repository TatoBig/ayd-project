from ..enemy_factory import EnemyFactory
from ...normie import Normie
from ...boss import Boss
from ...crazy import Crazy
from ....player import Player
from .hard_normie import HardNormie
from .hard_boss import HardBoss
from .hard_crazy import HardCrazy


class HardEnemyFactory(EnemyFactory):
    def create_normie(self, x: int, y: int, player: Player) -> Normie:
        return HardNormie(x, y, 15, player, 25)

    def create_crazy(self, x: int, y: int, player: Player) -> Crazy:
        return HardCrazy(x, y, 15, player, 20)

    def create_boss(self, x: int, y: int, player: Player) -> Boss:
        return HardBoss(x, y, 30, player, 100)