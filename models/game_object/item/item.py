from .. import GameObject
from ..character import DamageDecorator, Character, Wave


class Item(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'item.png')

    def activate(self, current_character: Character) -> Character:
        print('Decorado')
        return Wave(current_character)

