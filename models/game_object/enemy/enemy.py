from time import sleep
from threading import Thread
from .. import Player, GameObject

import pygame


class Enemy(GameObject):

    def __init__(self, x: int, y: int, speed: int, player: Player, health: float):
        super().__init__(x, y, 'enemy.png')
        self.__speed: float = speed
        self.__track_player: Player = player
        self.__tracking: bool = False
        self.__health: float = health
        self.__current_health: float = self.__health

    @property
    def tracking(self):
        return self.__tracking

    @property
    def current_health(self):
        return self.__current_health

    def track(self):
        self.__tracking = True
        t = Thread(target=self._keep_tracking)
        t.start()

    def hit(self, damage: int) -> None:
        self.__current_health -= damage

    def draw_health_bar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         [self.x, self.y - 25, ((self.__current_health / self.__health) * 100), 9], 0)
        pygame.draw.rect(screen, (255, 255, 0),
                         [self.x, self.y - 25, 100, 10], 2)

    def _keep_tracking(self):
        while True:
            sleep(self.__speed / 1000)
            if self.y > self.__track_player.y + self.__track_player.hitbox.centery:
                self.y -= 1
            else:
                self.y += 1

            if self.x > self.__track_player.x + self.__track_player.hitbox.centerx:
                self.x -= 1
            else:
                self.x += 1





