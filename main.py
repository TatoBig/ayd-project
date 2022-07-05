from models import Game
import pygame
import sys
import random
from button import Button
from models.menu.credits import Credits


class Main:
    """Clase menu"""

    def __init__(self):
        self.__game = Game()

        """Valores de pantalla"""
        self.playbutton = None
        pygame.init()
        self.width = 1280
        self.height = 720
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
        pygame.mixer.music.set_volume(0.1)
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

    def check_button(self, mouse):

        """Comprobamos el clic"""
        if 400 <= mouse[0] <= 500 and 210 <= mouse[1] <= 310:
            self.__game.init_game()
            self.activate_game = True
        if 400 <= mouse[0] <= 500 and 270 <= mouse[1] <= 350:
            print("creditos")
            self.activate_credits = True
        if 400 <= mouse[0] <= 500 and 330 <= mouse[1] <= 410:
            print("salir")
            sys.exit()

    def running_game(self):
        """Corre el juego más lectura de eventos"""
        coord_list = []
        for cont in range(90):
            cord_x = random.randint(0, 900)
            cord_y = random.randint(0, 500)
            coord_list.append([cord_x, cord_y])

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.check_button(mouse)

            self.screen.fill(self.gray)

            if not self.activate_game:
                self.buttons.print_button()
                self.play_button = self.buttons.get_button_start()
                for pos_list in coord_list:
                    pygame.draw.circle(self.screen, self.white, pos_list, 3)
                    pos_list[1] += 1
                    if pos_list[1] > 500:
                        pos_list[1] = 0
            # Activamos el juego
            if self.activate_game:
                # self.player.print_button_mode()
                pass

            if self.activate_credits:
                self.credit.print_button_credits()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    a = Main()
    a.running_game()
