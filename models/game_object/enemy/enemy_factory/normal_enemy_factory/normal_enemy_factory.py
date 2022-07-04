from ..enemy_factory import EnemyFactory
from ...normie import Normie
from ...boss import Boss
from ...crazy import Crazy
from ....player import Player
from .normal_normie import NormalNormie
from .normal_boss import NormalBoss
from .normal_crazy import NormalCrazy


class NormalEnemyFactory(EnemyFactory):
    def create_normie(self, x: int, y: int, player: Player) -> Normie:
        return NormalNormie(x, y, 20, player, 20)

    def create_crazy(self, x: int, y: int, player: Player) -> Crazy:
        return NormalCrazy(x, y, 18, player, 15)

    def create_boss(self, x: int, y: int, player: Player) -> Boss:
        return NormalBoss(x, y, 40, player, 80)