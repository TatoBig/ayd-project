import pygame
from .game_object import Bullet, Player
from .game_object.enemy import Enemy, Crazy, EnemyFactory, HardEnemyFactory, NormalEnemyFactory
from .game_object.item import Item


class Game:
    def __init__(self):
        pygame.init()

        self.__screen_bullets: list[Bullet] = []
        self.__screen_enemies: list[Enemy] = []
        self.__screen_items: list[Item] = []
        self.__width: int = 800
        self.__height: int = 600
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        # self.__enemy_factory: EnemyFactory = HardEnemyFactory()
        self.__enemy_factory: EnemyFactory = NormalEnemyFactory()

    def init_game(self):
        player = Player(400, 300)
        item = Item(250, 250)
        direction = 'down'

        self.__screen_items.append(item)
        self.__screen_enemies.append(self.__enemy_factory.create_normie(300, 400, player))
        self.__screen_enemies.append(self.__enemy_factory.create_crazy(600, 200, player))
        self.__screen_enemies.append(self.__enemy_factory.create_boss(70, 500, player))

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

            if len(self.__screen_items) > 0:
                for item in self.__screen_items:
                    self.__screen.blit(item.image, (item.x, item.y))
                    if item.x + item.hitbox.width >= player.x >= item.x - player.hitbox.width and \
                            item.y + item.hitbox.height >= player.y >= item.y - player.hitbox.height:
                        player.add_item(item)
                        player.upgrade_character(item)
                        self.__screen_items.remove(item)

            if len(self.__screen_enemies) > 0:
                for enemy in self.__screen_enemies:
                    self.__screen.blit(enemy.image, (enemy.x, enemy.y))
                    enemy.draw_health_bar(self.__screen)

                    if enemy.current_health <= 0:
                        self.__screen_enemies.remove(enemy)

                    if not enemy.tracking:
                        enemy.track()

            if len(self.__screen_bullets) > 0:
                for bullet in self.__screen_bullets:
                    bullet.shoot()
                    self.__screen.blit(bullet.image, (bullet.x + player.hitbox.centerx, bullet.y +
                                                      player.hitbox.centery))
                    if bullet.y < -player.hitbox.bottom or \
                            bullet.y > self.__height or \
                            bullet.x < -player.hitbox.right or\
                            bullet.x > self.__width:
                        self.__screen_bullets.remove(bullet)

                    for enemy in self.__screen_enemies:
                        # 50?
                        if enemy.x + enemy.hitbox.width >= bullet.x + 55 + bullet.hitbox.centerx \
                                >= enemy.x and\
                                enemy.y + enemy.hitbox.height >= bullet.y + 55 + bullet.hitbox.centery \
                                >= enemy.y:
                            self.__screen_bullets.remove(bullet)
                            enemy.hit(bullet.damage)

            pygame.display.flip()

        pygame.quit()
