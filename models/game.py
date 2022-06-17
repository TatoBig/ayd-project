import pygame
from .game_object import Bullet, Player

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

        # Needs to be moved
        cooldown = True
        direction = 'down'

        run: bool = True
        while run:
            pygame.time.delay(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            player_box = player.image.get_rect()

            if keys[pygame.K_UP] and player.y > 0:
                player.move_up()
                direction = 'up'
            if keys[pygame.K_DOWN] and player.y < height - player_box.bottom:
                player.move_down()
                direction = 'down'
            if keys[pygame.K_LEFT] and player.x > 0:
                player.move_left()
                direction = 'left'
            if keys[pygame.K_RIGHT] and player.x < width - player_box.right:
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
            if len(bullets) > 0:
                for bullet in bullets:
                    bullet.shoot()
                    screen.blit(bullet.image, (bullet.x + player_box.centerx, bullet.y + player_box.centery))
                    # print(f"bound of screen height {screen.get_height()} , width {screen.get_width()}")
                    # print(f"bullet y {bullet.y}, x {bullet.x}")
                    if bullet.y < -100 or bullet.y > 600 or bullet.x < -100 or bullet.x > 800:
                        print("OUT OF BOUNDS")
                        bullets.remove(bullet)
                    else:
                        print("INSIDE BOUNDS")
                    # bullet.y
                    # bullet.x
                    # detect when the bullets are outside the window and remove from array or delete instance
            print(len(bullets))

            pygame.display.flip()

        pygame.quit()
