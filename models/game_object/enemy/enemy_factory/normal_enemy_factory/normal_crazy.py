from ...crazy import Crazy
from ....player import Player


class NormalCrazy(Crazy):

    def __init__(self, x: int, y: int, speed: int, player: Player, health: float):
        super().__init__(x, y, speed, player, health)
