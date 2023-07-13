from _params import *
from cell import Cell

class Board:

    def __init__(self):
        self.cells = [ Cell(id) for id in range(64) ]


    def get_cell_at(self, cellID):
        '''
        Returns the cell object that is at the cellID location in the list of cells.
        '''
        return self.cells[cellID]
    

    def get_cell_by_litteral_notation(self, notation):
        '''
        Returns the cell object that corresponds to the notation.
        ex : notation = 'a7'
        '''
        col = 'abcdefgh'.index(notation[0])
        row = int(notation[1])-1
        cellID = col + 8*row
        return self.cells[cellID]

    def display_on_ui(self, ui):
        for cell in self.cells:
            cell.display_on_ui(ui)


#########################################################################################################
#########################################################################################################

if __name__ == '__main__':
    b = Board()
    c = b.get_cell_by_litteral_notation('e4')
    c.describe()