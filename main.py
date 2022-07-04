import pygame
import sys
import random
from button import Button
from credits import Credits
from player import Player


class Main:
    """Clase menu"""

    def __init__(self):
        """Valores de pantalla"""
        self.playbutton = None
        pygame.init()
        self.width = 900
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        # Pantalla
        pygame.display.set_caption("Game Menu")
        self.gray = (229, 232, 232)
        self.white = (255, 255, 255)
        # Musica
        pygame.mixer.music.load("PokemonStadium.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        # Juego
        self.activate_game = False
        self.activate_credits = False
        self.buttons = Button(self)
        self.credit = Credits(self)
        # self.player = Player(self)
        self.clock = pygame.time.Clock()
        # Objetos que me pide
        self.play_button = None
        self.press_button = None

    def running_game(self):
        """Corre el juego más lectura de eventos"""
        coord_list = []
        for cont in range(90):
            cord_x = random.randint(0, 900)
            cord_y = random.randint(0, 500)
            coord_list.append([cord_x, cord_y])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pass
                    if event.key == pygame.KSCAN_DOWN:
                        pass
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        pass
                    if event.key == pygame.K_DOWN:
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_button(mouse_pos)

            # Activamos el juego
            if self.activate_game:
                # self.player.print_button_mode()
                pass

            if self.activate_credits:
                self.credit.print_button_credits()

            self.screen.fill(self.gray)
            if not self.activate_game:
                self.buttons.print_button()
                for pos_list in coord_list:
                    pygame.draw.circle(self.screen, self.white, pos_list, 3)
                    pos_list[1] += 1
                    if pos_list[1] > 500:
                        pos_list[1] = 0

            pygame.display.flip()
            self.clock.tick(60)

    def check_button(self, mousepos):
        """Comprobamos el clic"""
        self.press_button = self.play_button.rect.collidepoint(mousepos)
        if self.press_button and not self.activate_game and not self.activate_credits:
            if self.playbutton.rect.collidepoint(self.buttons.button_rectangle_start):
                self.activate_game = True
            elif self.playbutton.rect.collidepoint(self.buttons.button_rectangle_credits):
                self.activate_credits = True
            elif self.playbutton.rect.collidepoint(self.buttons.button_rectangle_out):
                sys.exit()


if __name__ == "__main__":
    a = Main()
    a.running_game()
