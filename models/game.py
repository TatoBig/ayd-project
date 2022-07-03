from time import sleep

import pygame
import threading
from .game_object import Bullet, Player
from .game_object.enemy import Enemy

import sys




class Game:
    def __init__(self):
        pass

    def init_game(self):
        pygame.init()

        size = width, height = 800, 600
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)

        player = Player(400, 300)

        bullets: list[Bullet] = []
        enemies: list[Enemy] = []

        # Needs to be moved
        cooldown = True
        direction = 'down'
        enemy = Enemy(100, 100, 20, player, 20)
        enemy2 = Enemy(500, 550, 40, player, 80)
        enemies.append(enemy)
        enemies.append(enemy2)

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
            if keys[pygame.K_DOWN] and player.y < height - player.hitbox.bottom:
                player.move_down()
                direction = 'down'
            if keys[pygame.K_LEFT] and player.x > 0:
                player.move_left()
                direction = 'left'
            if keys[pygame.K_RIGHT] and player.x < width - player.hitbox.right:
                player.move_right()
                direction = 'right'
            if keys[pygame.K_SPACE]:
                if cooldown > 20:
                    cooldown = 0
                    bullet = Bullet(player.x, player.y, direction)
                    bullets.append(bullet)

            screen.fill(black)
            cooldown += 1

            screen.blit(player.image, (player.x, player.y))

            if len(enemies) > 0:
                for enemy in enemies:
                    screen.blit(enemy.image, (enemy.x, enemy.y))
                    enemy.draw_health_bar(screen)

                    if enemy.current_health <= 0:
                        enemies.remove(enemy)

                    if not enemy.tracking:
                        enemy.track()

            if len(bullets) > 0:
                for bullet in bullets:
                    bullet.shoot()
                    screen.blit(bullet.image, (bullet.x + player.hitbox.centerx, bullet.y + player.hitbox.centery))
                    if bullet.y < -player.hitbox.bottom or bullet.y > height or bullet.x < -player.hitbox.right or\
                            bullet.x > width:
                        bullets.remove(bullet)

                    for enemy in enemies:
                        # 50?
                        if enemy.x + enemy.hitbox.width >= bullet.x + 50 + bullet.hitbox.centerx >= enemy.x and\
                                enemy.y + enemy.hitbox.height >= bullet.y + 50 + bullet.hitbox.centery >= enemy.y:
                            bullets.remove(bullet)
                            enemy.hit(1)

            pygame.display.flip()

        pygame.quit()
