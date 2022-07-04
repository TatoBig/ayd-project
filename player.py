import pygame.font


class Player:
    """Clase para elegir número de jugadores"""

    def __init__(self, a_game):
        self.text_player = None
        self.text_player_rectangle = None
        self.text_player_two = None
        self.text_player_rectangle_two = None
        self.button_player = None
        self.button_player_two = None
        pygame.display.set_caption("Modo de juego")
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.button_width = 100
        self.button_height = 80
        self.button_color = (230, 230, 230)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.prepare_mode()

    def prepare_mode(self):
        """Renderizado del texto"""
        self.button_player = pygame.Rect(900 / 4 - 50, 500 / 2 - 40, self.button_width, self.button_height)
        self.button_player_two = pygame.Rect(900 / 4 - 50, 500 / 2 - 40, self.button_width, self.button_height)
        self.text_player = self.font.render("1 Jugador", True, self.text_color, self.button_color)
        self.text_player = self.text_player.get_rect()
        self.text_player_rectangle.center = self.button_player.center
        self.text_player_two = self.font.render("2 Jugadores", True, self.text_color, self.button_color)
        self.text_player_rectangle_two = self.text_player_two.get_rect()
        self.text_player_rectangle_two.center = self.button_player_two.center

    def print_button_mode(self):
        """Mostramos botones"""
        self.screen.fill(self.button_color, self.button_player)
        self.screen.blit(self.text_player, self.text_player_rectangle)
        self.screen.fill(self.button_color, self.button_player_two)
        self.screen.blit(self.text_player_two, self.text_player_rectangle_two)
