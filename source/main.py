from ui import UI
from game import Game

if __name__ == '__main__':
    game = Game()
    ui = UI(game)
    ui.Run()
