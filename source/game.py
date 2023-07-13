from _params import *
from board import Board


class Game:

    def __init__(self):
        self.board = Board()
    

    def display_on_ui(self, ui):
        self.board.display_on_ui(ui)