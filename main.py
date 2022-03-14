from kivy.app import App
from kivy.uix.screenmanager import Screen

class MenuScreen(Screen):
    pass

class SudokuScreen(Screen):
    pass

class GameApp(App):
    def build(self):
        return MenuScreen()

if __name__ == '__main__':
    GameApp().run()
