from _params import *

import pygame

class UI:

    def __init__(self, game, text_handler):
        
        self.__init_graphics__()
        self.screen = None
        self.running = False
        self.game = game
        self.text_handler = text_handler


    def __init_graphics__(self):
        # color
        self.backcolor = BACKCOLOR
        self.white = WHITE
        self.black = BLACK
        
        # dimensions
        self.screen_x = SCREEN_X
        self.screen_y = SCREEN_Y
        self.cell_size = CELL_SIZE
        self.board_size = BOARD_SIZE
    

    def QUIT_pygame(self, event):
        '''
        Sets the "self.running" variable to False and thus quits the loop and quits pygame.
        '''
        if event.type == pygame.QUIT:
            self.running=False
        else:
            pass


    def Run(self):


        # initialize the screen, running state and pygame
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        pygame.display.set_caption('Chess program')

        # for as long as the state is running, load graphics and go through events
        while(self.running):
            pygame.Surface.fill(self.screen, self.backcolor)
            self.game.display_on_ui(self)
            self.text_handler.display_on_ui(self)
            pygame.display.flip()

            for event in pygame.event.get():
                self.QUIT_pygame(event)
        
        # once running is set to False, we can quit pygame
        pygame.quit()