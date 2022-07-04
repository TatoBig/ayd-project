from .. import Player
from .enemy import Enemy


class Boss(Enemy):
    def __init__(self, x: int, y: int, speed: int, player: Player, health: float):
        super().__init__(x, y, 'boss.png', speed, player, health)
