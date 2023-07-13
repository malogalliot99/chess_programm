from _params import *
import pygame
pygame.font.init()

class Text:

    def __init__(self, content, coordinates, font_size = 30, font_name = FONT_LINK):
        self.content = content
        self.font_size = font_size
        self.coordinates = coordinates
        
        self.font_link = FONT_LINK

        self.font = pygame.font.SysFont(self.font_link, self.font_size)
        self.surface = None
        
        self.font_rgb_color = FONT_COLOR

    def update_surface(self):
        self.surface = self.font.render(self.content, True, self.font_rgb_color)

    def display_on_ui(self, ui):
        self.update_surface()
        ui.screen.blit(self.surface, self.coordinates)


if __name__ == '__main__':
    fonts = pygame.font.get_fonts()
    print(len(fonts))
    for f in fonts:
        print(f)