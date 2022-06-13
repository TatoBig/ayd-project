from .game_object import GameObject


class Player(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 'intro_ball.gif')

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1
