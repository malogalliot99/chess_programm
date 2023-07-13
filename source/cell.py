import pygame
from _params import *

class Cell:

    def __init__(self, cellID):
        self.id = cellID
        
        # ROW AND COLUMN
        self.row = cellID // 8
        self.col = cellID % 8

        self.row_litteral = str(1 + self.row)
        self.col_litteral = 'abcdefgh'[self.col]
        self.name_litteral = self.col_litteral + self.row_litteral

        # COLOR
        self.rgb_color = WHITE if (self.row + self.col)%2 == 1 else BLACK
        self.color_litteral = 'white' if (self.row + self.col)%2 == 1 else 'black'

        # SIZE AND LOCATION ON UI
        self.ui_size = CELL_SIZE
        self.ui_x_coord = X0 + self.col * CELL_SIZE
        self.ui_y_coord = Y0 + (7 - self.row) * CELL_SIZE
    

    def describe(self):
        print(f'{self.name_litteral} | {self.color_litteral}')
        print(f'   | ({self.col}, {self.row})')

    
    def display_on_ui(self, ui):
        pygame.Surface.fill(ui.screen, self.rgb_color, [self.ui_x_coord, self.ui_y_coord, self.ui_size, self.ui_size])


#########################################################################################################
#########################################################################################################

if __name__ == '__main__':
    cell = Cell(63)
    cell.describe()