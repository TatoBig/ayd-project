from typing import Optional
import pygame
import random
from .game_object import Bullet, Player
from .game_object.enemy import Enemy
from .game_object.item import Item
from .store import Store
from .Round import Director, NormalRoundBuilder, NormalRound
from .game_object.character import Fish, Robot, Sniper, Character


class Game:
    def __init__(self):
        pygame.init()

        self.__player_character1: Optional[Character] = None
        self.__player_character2: Optional[Character] = None
        self.__width: int = 1280
        self.__height: int = 720

        self.__multiplayer: bool = False

        self.__screen_bullets: list[Bullet] = []
        self.__screen_enemies: list[Enemy] = []
        self.__screen_items: list[Item] = []
        self.__screen_players: list[Player] = []

        self.__direction: str = 'down'
        self.__direction2: str = 'down'

        self.__normal_round_builder: NormalRoundBuilder = NormalRoundBuilder()
        self.__round_director: Optional[Director] = None
        self.__current_round: Optional[NormalRound] = None
        self.__round_timer: int = 0
        self.__round_counter: int = 0
        self.__new_round: bool = True

        self.__store: Store = Store()
        self.__store.set_round_counter(self.__round_counter)
        self.__store.set_size(self.__width, self.__height)

        self.__screen = pygame.display.set_mode((self.__width, self.__height))

    def set_multiplayer(self, multiplayer: bool) -> None:
        self.__multiplayer = multiplayer

    def set_character1(self, character: str):
        if character == 'fish':
            self.__player_character1 = Fish()
        elif character == 'sniper':
            self.__player_character1 = Sniper()
        elif character == 'robot':
            self.__player_character1 = Robot()

    def set_character2(self, character: str):
        if character == 'fish':
            self.__player_character2 = Fish()
        elif character == 'sniper':
            self.__player_character2 = Sniper()
        elif character == 'robot':
            self.__player_character2 = Robot()

    def set_difficulty(self, difficulty: str):
        self.__round_director = Director(self.__normal_round_builder, difficulty)

    def init_game(self):
        player = Player(400, 300, self.__player_character1)
        self.__store.add_player(player)
        self.__screen_players.append(player)
        if self.__multiplayer:
            player2 = Player(200, 100, self.__player_character2)
            self.__store.add_player(player2)
            self.__screen_players.append(player2)

        run: bool = True
        while run:
            pygame.time.delay(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            black = 0, 0, 0
            self.__screen.fill(black)

            for player in self.__screen_players:
                if player.health > 0:
                    self.__screen.blit(player.image, (player.x, player.y))
                    player.draw_cooldown(self.__screen)
                else:
                    self.__store.remove_player(player)

            my_font = pygame.font.Font(None, 30)
            my_round = my_font.render(f'{self.__round_counter}', 0, (200, 60, 80))
            self.__screen.blit(my_round, (100, 100))

            self.handle_controls(keys)
            self.handle_rounds()
            self.handle_items()
            self.handle_enemies()
            self.handle_bullets()
            self.handle_players()

            pygame.display.flip()

        pygame.quit()

    def handle_players(self):
        if self.__multiplayer:
            if self.__screen_players[1].health == 0 and self.__screen_players[0].health == 0:
                pygame.quit()
        else:
            if self.__screen_players[0].health == 0:
                pygame.quit()

    def handle_controls(self, keys):

        if self.__multiplayer:
            if keys[pygame.K_UP] and self.__screen_players[0].y > 0:
                self.__screen_players[0].move_up()
                self.__direction = 'up'
            if keys[pygame.K_DOWN] and self.__screen_players[0].y < self.__height - \
                    self.__screen_players[0].hitbox.bottom:
                self.__screen_players[0].move_down()
                self.__direction = 'down'
            if keys[pygame.K_LEFT] and self.__screen_players[0].x > 0:
                self.__screen_players[0].move_left()
                self.__direction = 'left'
            if keys[pygame.K_RIGHT] and self.__screen_players[0].x < self.__width - \
                    self.__screen_players[0].hitbox.right:
                self.__screen_players[0].move_right()
                self.__direction = 'right'
            if keys[pygame.K_RETURN] and self.__screen_players[0].health > 0:
                if self.__direction is None:
                    self.__direction = 'down'
                bullet = self.__screen_players[0].shoot(self.__direction)
                if bullet is not None:
                    self.__screen_bullets.append(bullet)
            if keys[pygame.K_w] and self.__screen_players[1].y > 0:
                self.__screen_players[1].move_up()
                self.__direction2 = 'up'
            if keys[pygame.K_s] and self.__screen_players[1].y < self.__height - \
                    self.__screen_players[1].hitbox.bottom:
                self.__screen_players[1].move_down()
                self.__direction2 = 'down'
            if keys[pygame.K_a] and self.__screen_players[1].x > 0:
                self.__screen_players[1].move_left()
                self.__direction2 = 'left'
            if keys[pygame.K_d] and self.__screen_players[1].x < self.__width - \
                    self.__screen_players[1].hitbox.right:
                self.__screen_players[1].move_right()
                self.__direction2 = 'right'
            if keys[pygame.K_SPACE] and self.__screen_players[1].health > 0:
                if self.__direction2 is None:
                    self.__direction2 = 'down'
                bullet = self.__screen_players[1].shoot(self.__direction2)
                if bullet is not None:
                    self.__screen_bullets.append(bullet)
        else:
            if keys[pygame.K_UP]:
                bullet = self.__screen_players[0].shoot('up')
                if bullet is not None:
                    self.__screen_bullets.append(bullet)
            if keys[pygame.K_DOWN]:
                bullet = self.__screen_players[0].shoot('down')
                if bullet is not None:
                    self.__screen_bullets.append(bullet)
            if keys[pygame.K_LEFT]:
                bullet = self.__screen_players[0].shoot('left')
                if bullet is not None:
                    self.__screen_bullets.append(bullet)
            if keys[pygame.K_RIGHT]:
                bullet = self.__screen_players[0].shoot('right')
                if bullet is not None:
                    self.__screen_bullets.append(bullet)
            if keys[pygame.K_w] and self.__screen_players[0].y > 0:
                self.__screen_players[0].move_up()
            if keys[pygame.K_s] and self.__screen_players[0].y < self.__height - self.__screen_players[0].hitbox.bottom:
                self.__screen_players[0].move_down()
            if keys[pygame.K_a] and self.__screen_players[0].x > 0:
                self.__screen_players[0].move_left()
            if keys[pygame.K_d] and self.__screen_players[0].x < self.__width - self.__screen_players[0].hitbox.right:
                self.__screen_players[0].move_right()

    def handle_rounds(self):
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
                             [0, 0, (self.__round_timer / self.__current_round.time) * self.__width, 4], 0)
            if self.__round_timer > self.__current_round.time:
                self.__round_timer = 0
                self.__new_round = True

        if self.__round_counter > 31:
            pygame.quit()

    def handle_items(self):
        if len(self.__screen_items) > 0:
            for player in self.__screen_players:
                for item in self.__screen_items:
                    self.__screen.blit(item.image, (item.x, item.y))
                    if item.x + item.hitbox.width >= player.x >= item.x - player.hitbox.width and \
                            item.y + item.hitbox.height >= player.y >= item.y - player.hitbox.height:
                        player.add_item(item)
                        player.upgrade_character(item)
                        self.__screen_items.remove(item)

    def handle_enemies(self):
        if len(self.__screen_enemies) > 0:
            for player in self.__screen_players:
                if player.health > 0:
                    for enemy in self.__screen_enemies:
                        self.__screen.blit(enemy.image, (enemy.x, enemy.y))
                        enemy.draw_health_bar(self.__screen)

                        if enemy.current_health <= 0:
                            try:
                                self.__screen_enemies.remove(enemy)
                            except:
                                print('Catch')

                        if not enemy.tracking:
                            enemy.track()

                        if enemy.x + enemy.hitbox.width >= player.x >= enemy.x - player.hitbox.width and \
                                enemy.y + enemy.hitbox.height >= player.y >= enemy.y - player.hitbox.height:
                            player.hit()
                            self.__screen_enemies = []

    def handle_bullets(self):
        if len(self.__screen_bullets) > 0:
            for player in self.__screen_players:
                for bullet in self.__screen_bullets:
                    bullet.shoot()
                    self.__screen.blit(bullet.image, (bullet.x + player.hitbox.centerx, bullet.y +
                                                      player.hitbox.centery))
                    if bullet.y < -player.hitbox.bottom or \
                            bullet.y > self.__height or \
                            bullet.x < -player.hitbox.right or \
                            bullet.x > self.__width:
                        try:
                            self.__screen_bullets.remove(bullet)
                        except:
                            print('Catch')

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
