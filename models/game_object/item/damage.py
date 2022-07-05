from ..character import DamageDecorator, Character
from ..item import Item


class Damage(Item):
    def __init__(self):
        super().__init__('damage.png')

    def activate(self, current_character: Character) -> Character:
        return DamageDecorator(current_character)

