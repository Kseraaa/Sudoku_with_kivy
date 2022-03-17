from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput     import TextInput

class MenuScreen(Screen):
    pass

class SudokuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs    = []

        grid = self.ids["grid"]
        for i in range(81) :
            text_input = SudokuCell()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)

    def clear(self):
        for text_input in self.ids["grid"].children:
            text_input.text = ""

class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SudokuScreen(name='play'))
        return sm

class SudokuCell(TextInput):
    pass

if __name__ == '__main__':
    GameApp().run()