from time import sleep
from threading import Thread
from .. import Player, GameObject

import pygame


class Enemy(GameObject):

    def __init__(self, x: int, y: int, speed: int, player: Player, health: float):
        super().__init__(x, y, 'enemy.png')
        self.__health: float = health
        self.__speed: float = speed
        self.__track_player: Player = player
        self.__tracking: bool = False
        self.__current_health: float = self.__health

    @property
    def tracking(self):
        return self.__tracking

    @property
    def speed(self):
        return self.__speed

    @property
    def track_player(self):
        return self.__track_player

    @property
    def current_health(self):
        return self.__current_health

    def hit(self, damage: float) -> None:
        self.__current_health -= damage

    def draw_health_bar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         [self.x, self.y - 25, ((self.__current_health / self.__health) * 100), 9], 0)
        pygame.draw.rect(screen, (255, 255, 0),
                         [self.x, self.y - 25, 100, 10], 2)

    def track(self):
        self.__tracking = True
        t = Thread(target=self._keep_tracking)
        t.start()

    def _keep_tracking(self):
        while True:
            sleep(self.__speed / 1000)
            if self.y > self.__track_player.y + self.__track_player.hitbox.centery:
                self.move_up()
            else:
                self.move_down()
            if self.x > self.__track_player.x + self.__track_player.hitbox.centerx:
                self.move_left()
            else:
                self.move_right()





