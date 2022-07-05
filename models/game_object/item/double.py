from ..character import Character, Double as DoubleDecorator
from ..item import Item


class Double(Item):
    def __init__(self):
        super().__init__('double.png')

    def activate(self, current_character: Character) -> Character:
        return DoubleDecorator(current_character)

