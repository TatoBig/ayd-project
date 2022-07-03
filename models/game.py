import pygame
from .game_object import Bullet, Player
from .game_object.enemy import Enemy, Crazy
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

    def init_game(self):
        player = Player(400, 300)
        item = Item(100, 100)
        direction = 'down'
        enemy = Enemy(100, 100, 20, player, 20)
        enemy2 = Crazy(500, 550, 40, player, 80)
        self.__screen_enemies.append(enemy)
        self.__screen_enemies.append(enemy2)
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
                # bullets.append()

            black = 0, 0, 0
            self.__screen.fill(black)

            self.__screen.blit(player.image, (player.x, player.y))

            if len(self.__screen_items) > 0:
                for item in self.__screen_items:
                    self.__screen.blit(item.image, (item.x, item.y))
                    if player.x + player.hitbox.width >= item.x + 55 + item.hitbox.centerx >= player.x and \
                            player.y + player.hitbox.height >= item.y + 55 + item.hitbox.centery >= player.y:
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
                    self.__screen.blit(bullet.image, (bullet.x + player.hitbox.centerx, bullet.y + player.hitbox.centery))
                    if bullet.y < -player.hitbox.bottom or bullet.y > self.__height or bullet.x < -player.hitbox.right or\
                            bullet.x > self.__width:
                        self.__screen_bullets.remove(bullet)

                    for enemy in self.__screen_enemies:
                        # 50?
                        if enemy.x + enemy.hitbox.width >= bullet.x + 55 + bullet.hitbox.centerx >= enemy.x and\
                                enemy.y + enemy.hitbox.height >= bullet.y + 55 + bullet.hitbox.centery >= enemy.y:
                            self.__screen_bullets.remove(bullet)
                            enemy.hit(bullet.damage)

            pygame.display.flip()

        pygame.quit()
