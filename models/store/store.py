from .store_meta import StoreMeta
from ..game_object import Player
from random import randint


class Store(metaclass=StoreMeta):
    def __init__(self):
        self.__players: list[Player] = []
        self.__width: int = 0
        self.__height: int = 0
        self.__round_counter: int = 0

    def set_size(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def add_player(self, player: Player):
        self.__players.append(player)

    def get_players(self) -> list[Player]:
        return self.__players

    def get_random_player(self) -> Player:
        return self.__players[randint(1, len(self.__players)) - 1]

    def set_round_counter(self, round_counter: int):
        self.__round_counter = round_counter

    def get_round_counter(self) -> int:
        return self.__round_counter
