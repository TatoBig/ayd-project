from abc import ABC, abstractmethod
from ..normie import Normie
from ..boss import Boss
from ..crazy import Crazy
from ...player import Player


class EnemyFactory(ABC):

    @abstractmethod
    def create_normie(self, x: int, y: int, player: Player) -> Normie:
        raise NotImplementedError

    @abstractmethod
    def create_crazy(self, x: int, y: int, player: Player) -> Crazy:
        raise NotImplementedError

    @abstractmethod
    def create_boss(self, x: int, y: int, player: Player) -> Boss:
        raise NotImplementedError
