from ..character import Character, Wave
from ..item import Item


class Quad(Item):
    def __init__(self):
        super().__init__('quad.png')

    def activate(self, current_character: Character) -> Character:
        return Wave(current_character)

