from ..character import Character
from .character_decorator import CharacterDecorator


class DamageDecorator(CharacterDecorator):
    def __init__(self, character: Character):
        super().__init__(character)
        self.bullet_damage = self.bullet_damage * 1.5


