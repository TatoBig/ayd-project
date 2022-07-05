from models import Game
import pygame
import sys
import random
from button import Button
from models.menu.credits import Credits
from models.menu.player_menu import PlayerMenu
from models.menu.player_menu_1 import PlayerMenu1
from models.menu.player_menu_2 import PlayerMenu2


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
        self.activate_player1 = False
        self.activate_player2 = False
        self.buttons = Button(self)
        self.credit = Credits(self)
        self.playerMenu = PlayerMenu(self)
        self.playerMenu1 = PlayerMenu1(self)
        self.playerMenu2 = PlayerMenu2(self)
        # self.player = Player(self)
        self.clock = pygame.time.Clock()
        # Objetos que me pide
        self.play_button = None
        self.press_button = None
        self.use_check_button = True
        self.use_check_button_player = False
        self.use_check_button_election = False

    def check_button(self, mouse):

        """Comprobamos el clic"""
        if 400 <= mouse[0] <= 500 and 210 <= mouse[1] <= 310:
            self.activate_game = True
            self.use_check_button = False
            self.use_check_button_player = True
            #self.__game.init_game()
        if 400 <= mouse[0] <= 500 and 270 <= mouse[1] <= 350:
            print("creditos")
            self.activate_credits = True
            self.use_check_button = False
            self.use_check_button_player = True
        if 400 <= mouse[0] <= 500 and 330 <= mouse[1] <= 410:
            print("salir")
            sys.exit()
    
    def check_button_players(self, mouse):

        """Comprobamos el clic"""
        if 400 <= mouse[0] <= 500 and 210 <= mouse[1] <= 310:
            self.activate_player1 = True
            self.use_check_button_player = False
            self.use_check_button_election = True
            print("1 jugador")
            
        if 400 <= mouse[0] <= 500 and 270 <= mouse[1] <= 350:
            self.activate_player1 = True
            self.activate_player2 = True            
            self.use_check_button_player = False
            self.use_check_button_election = True
            print("2 jugadores")
            
    def check_button_election(self, mouse):

        """Comprobamos el clic"""
        if 400 <= mouse[0] <= 500 and 210 <= mouse[1] <= 310:
            print("fish")
            #self.__game.init_game()
        if 400 <= mouse[0] <= 500 and 270 <= mouse[1] <= 350:
            print("bobot")
        if 400 <= mouse[0] <= 500 and 330 <= mouse[1] <= 410:
            print("sniper")

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
                if ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button == True and self.use_check_button_player == False:
                    self.check_button(mouse)
                elif ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button == False and self.use_check_button_player == True:
                    print("activado para player")
                    self.check_button_players(mouse)
                elif ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button == False and self.use_check_button_player == False and self.use_check_button_election == True:
                    self.check_button_election(mouse)

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
                self.playerMenu.print_button_mode()

            if self.activate_credits:
                self.credit.print_button_credits()
            
            if self.activate_player1:
                self.playerMenu1.print_button()
            
            if self.activate_player2:
                self.playerMenu2.print_button()

            
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    a = Main()
    a.running_game()
