from typing import Optional

import pygame
import random
from .game_object import Bullet, Player
from .game_object.enemy import Enemy
from .game_object.item import Item
from .store import Store
from .Round import Director, NormalRoundBuilder, NormalRound


class Game:
    def __init__(self):
        pygame.init()
        self.__width: int = 1280
        self.__height: int = 720

        self.__screen_bullets: list[Bullet] = []
        self.__screen_enemies: list[Enemy] = []
        self.__screen_items: list[Item] = []

        self.__normal_round_builder: NormalRoundBuilder = NormalRoundBuilder()
        self.__round_director: Director = Director(self.__normal_round_builder, 'hard')
        self.__current_round: Optional[NormalRound] = None
        self.__round_timer: int = 0
        self.__round_counter: int = 0
        self.__new_round: bool = True

        self.__store: Store = Store()
        self.__store.set_round_counter(self.__round_counter)
        self.__store.set_size(self.__width, self.__height)

        self.__screen = pygame.display.set_mode((self.__width, self.__height))

    def init_game(self):
        player = Player(400, 300)
        self.__store.add_player(player)
        item = Item(250, 250)
        direction = 'down'

        self.__screen_items.append(item)

        run: bool = True
        while run:
            pygame.time.delay(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and player.y > 0:
                player.move_up()
                direction = 'up'
            if keys[pygame.K_DOWN] and player.y < self.__height - player.hitbox.bottom:
                player.move_down()
                direction = 'down'
            if keys[pygame.K_LEFT] and player.x > 0:
                player.move_left()
                direction = 'left'
            if keys[pygame.K_RIGHT] and player.x < self.__width - player.hitbox.right:
                player.move_right()
                direction = 'right'
            if keys[pygame.K_SPACE]:
                bullet = player.shoot(direction)
                if bullet is not None:
                    self.__screen_bullets.append(bullet)

            black = 0, 0, 0
            self.__screen.fill(black)

            self.__screen.blit(player.image, (player.x, player.y))
            player.draw_cooldown(self.__screen)

            my_font = pygame.font.Font(None, 30)
            my_round = my_font.render(f'{self.__round_counter}', 0, (200, 60, 80))
            self.__screen.blit(my_round, (100, 100))

            # Rounds
            if self.__new_round:
                self.__round_counter += 1
                self.__round_timer = 0
                self.__store.set_round_counter(self.__round_counter)

                self.__new_round = False
                self.__round_director.make_rounds(self.__round_counter)
                self.__current_round = self.__normal_round_builder.get_result()
                for enemy in self.__current_round.enemies:
                    self.__screen_enemies.append(enemy)
                for items in self.__current_round.items:
                    self.__screen_items.append(items)

            if len(self.__screen_enemies) == 0:
                self.__new_round = True

            if self.__current_round is not None:
                self.__round_timer += 1

                pygame.draw.rect(self.__screen, (255, 255, 255),
                                 [0, 100 - 25, (self.__round_timer / self.__current_round.time) * self.__width, 4], 0)
                if self.__round_timer > self.__current_round.time:
                    self.__round_timer = 0
                    self.__new_round = True

            # Items
            if len(self.__screen_items) > 0:
                for item in self.__screen_items:
                    self.__screen.blit(item.image, (item.x, item.y))
                    if item.x + item.hitbox.width >= player.x >= item.x - player.hitbox.width and \
                            item.y + item.hitbox.height >= player.y >= item.y - player.hitbox.height:
                        player.add_item(item)
                        player.upgrade_character(item)
                        self.__screen_items.remove(item)

            # Enemies
            if len(self.__screen_enemies) > 0:
                for enemy in self.__screen_enemies:
                    self.__screen.blit(enemy.image, (enemy.x, enemy.y))
                    enemy.draw_health_bar(self.__screen)

                    if enemy.current_health <= 0:
                        self.__screen_enemies.remove(enemy)

                    if not enemy.tracking:
                        enemy.track()

            # Bullets
            if len(self.__screen_bullets) > 0:
                for bullet in self.__screen_bullets:
                    bullet.shoot()
                    self.__screen.blit(bullet.image, (bullet.x + player.hitbox.centerx, bullet.y +
                                                      player.hitbox.centery))
                    if bullet.y < -player.hitbox.bottom or \
                            bullet.y > self.__height or \
                            bullet.x < -player.hitbox.right or \
                            bullet.x > self.__width:
                        self.__screen_bullets.remove(bullet)

                    for enemy in self.__screen_enemies:
                        # 50?
                        if enemy.x + enemy.hitbox.width >= bullet.x + 55 + bullet.hitbox.centerx \
                                >= enemy.x and \
                                enemy.y + enemy.hitbox.height >= bullet.y + 55 + bullet.hitbox.centery \
                                >= enemy.y:
                            try:
                                self.__screen_bullets.remove(bullet)
                            except:
                                print('temp')
                            enemy.hit(bullet.damage)

            pygame.display.flip()

        pygame.quit()
