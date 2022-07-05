import pygame


class PlayerMenu1:
    """Clase para crear los botones en el menu"""

    def __init__(self, a_game):
        self.text_image = None
        self.text_image_rectangle = None
        self.text_image_two = None
        self.text_image_rectangle_two = None
        self.text_image_three = None
        self.text_image_rectangle_three = None
        self.text_tittle = None
        self.text_tittle_rectangle = None
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.button_width = 100
        self.button_height = 80
        self.button_color = (230, 230, 230)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.font_tittle = pygame.font.SysFont(None, 100)
        self.button_rectangle_start = None
        self.button_rectangle_credits = None
        self.button_rectangle_out = None
        self.tittle = None
        self.prepare_text()

    def prepare_text(self):
        """Renderizamos el texto"""
        self.button_rectangle_start = pygame.Rect(900 / 2 - 50, 500 / 2 - 40, self.button_width, self.button_height)
        self.button_rectangle_credits = pygame.Rect(900 / 2 - 50, 500 / 2 + 20, self.button_width, self.button_height)
        self.button_rectangle_out = pygame.Rect(900 / 2 - 50, 500 / 2 + 80, self.button_width, self.button_height)
        self.tittle = pygame.Rect(900 / 2 - 200, 20, 400, 200)
        self.text_image = self.font.render("Fish", True, self.text_color, self.button_color)
        self.text_image_rectangle = self.text_image.get_rect()
        self.text_image_rectangle.center = self.button_rectangle_start.center
        self.text_image_two = self.font.render("Robot", True, self.text_color, self.button_color)
        self.text_image_rectangle_two = self.text_image_two.get_rect()
        self.text_image_rectangle_two.center = self.button_rectangle_credits.center
        self.text_image_three = self.font.render("Sniper", True, self.text_color, self.button_color)
        self.text_image_rectangle_three = self.text_image_three.get_rect()
        self.text_image_rectangle_three.center = self.button_rectangle_out.center
        self.text_tittle = self.font_tittle.render("Jugador 1 - Eleccion de personaje", True, self.text_color, self.button_color)
        self.text_tittle_rectangle = self.text_tittle.get_rect()
        self.text_tittle_rectangle.center = self.tittle.center

    def print_button(self):
        """Hacemos visibles los botones"""
        self.screen.fill(self.button_color, self.button_rectangle_start)
        self.screen.blit(self.text_image, self.text_image_rectangle)
        self.screen.fill(self.button_color, self.button_rectangle_credits)
        self.screen.blit(self.text_image_two, self.text_image_rectangle_two)
        self.screen.fill(self.button_color, self.button_rectangle_out)
        self.screen.blit(self.text_image_three, self.text_image_rectangle_three)
        self.screen.fill(self.button_color, self.tittle)
        self.screen.blit(self.text_tittle, self.text_tittle_rectangle)

    def get_button_start(self):
        return self.button_rectangle_start

    def get_button_credits(self):
        return self.button_rectangle_credits

    def get_button_quit(self):
        return self.button_rectangle_out