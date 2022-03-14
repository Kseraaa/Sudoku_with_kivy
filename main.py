from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class MenuScreen(Screen):
    pass

class SudokuScreen(Screen):
    pass

class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SudokuScreen(name='play'))
        return sm


if __name__ == '__main__':
    GameApp().run()
