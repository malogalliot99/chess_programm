from ui import UI
from game import Game
from text_handler import TextHandler

if __name__ == '__main__':
    game = Game()
    text_handler = TextHandler()
    ui = UI(game, text_handler)
    ui.Run()

