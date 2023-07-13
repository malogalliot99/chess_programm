
from text import Text


class TextHandler:

    def __init__(self):
        self.texts = [
            Text('White :', (0,0)),
            Text('aaa', (100,0))
        ]
    

    def display_on_ui(self, ui):
        for text in self.texts:
            text.display_on_ui(ui)