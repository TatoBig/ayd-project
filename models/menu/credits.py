import pygame


class Credits:
    """Pantalla de creditos"""
    def __init__(self, a_game):
        pygame.display.set_caption("Creditos")
        self.text_user = None
        self.text_user_rectangle = None
        self.text_user_two = None
        self.text_user_rectangle_two = None
        self.text_user_three = None
        self.text_user_rectangle_three = None
        self.text_user_four = None
        self.text_user_rectangle_four = None
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.button_width = 100
        self.button_height = 80
        self.button_color = (230, 230, 230)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.button_rectangle_pao = None
        self.button_rectangle_tat = None
        self.button_rectangle_ali = None
        self.button_rectangle_jef = None
        self.prepare_text()

    def prepare_text(self):
        """Renderizamos el texto"""
        self.button_rectangle_pao = pygame.Rect(900 / 2 - 50, 500 / 2 - 10, self.button_width, self.button_height)
        self.button_rectangle_tat = pygame.Rect(900 / 2 - 50, 500 / 2 + 100, self.button_width, self.button_height)
        self.button_rectangle_ali = pygame.Rect(900 / 2 - 50, 500 / 2 + 190, self.button_width, self.button_height)
        self.button_rectangle_jef = pygame.Rect(900 / 2 - 50, 500 / 2 + 280, self.button_width, self.button_height)
        self.text_user = self.font.render("Paolo Veliz", True, self.text_color, self.button_color)
        self.text_user_rectangle = self.text_user.get_rect()
        self.text_user_rectangle.center = self.button_rectangle_pao.center
        self.text_user_two = self.font.render("Santiago Navas", True, self.text_color, self.button_color)
        self.text_user_rectangle_two = self.text_user_two.get_rect()
        self.text_user_rectangle_two.center = self.button_rectangle_tat.center
        self.text_user_three = self.font.render("Alison Ramos", True, self.text_color, self.button_color)
        self.text_user_rectangle_three = self.text_user_three.get_rect()
        self.text_user_rectangle_three.center = self.button_rectangle_ali.center
        self.text_user_four = self.font.render("Jeffrey Reyes", True, self.text_color, self.button_color)
        self.text_user_rectangle_four = self.text_user_four.get_rect()
        self.text_user_rectangle_four.center = self.button_rectangle_jef.center

    def print_button_credits(self):
        """Mostramos el boton"""
        self.screen.fill(self.button_color, self.button_rectangle_pao)
        self.screen.blit(self.text_user, self.text_user_rectangle)
        self.screen.fill(self.button_color, self.button_rectangle_tat)
        self.screen.blit(self.text_user_two, self.text_user_rectangle_two)
        self.screen.fill(self.button_color, self.button_rectangle_ali)
        self.screen.blit(self.text_user_three, self.text_user_rectangle_three)
        self.screen.fill(self.button_color, self.button_rectangle_jef)
        self.screen.blit(self.text_user_four, self.text_user_rectangle_four)
