from .. import GameObject
from ..character import DamageDecorator, Character, Wave, Double
from random import randint
from ...store import Store


class Item(GameObject):
    def __init__(self, image: str):
        self.__store: Store = Store()
        rand_x = randint(15, self.__store.get_width())
        rand_y = randint(15, self.__store.get_height())
        super().__init__(rand_x, rand_y, image)

    def activate(self, current_character: Character) -> Character:
        raise NotImplementedError

