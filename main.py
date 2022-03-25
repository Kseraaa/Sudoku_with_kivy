from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput     import TextInput
from kivy.uix.label         import Label
from kivy.clock             import Clock
from sudoku import Sudoku

class MenuScreen(Screen):
    pass

class SudokuScreen1(Screen):
    # ป้อนข้อความ
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs    = []
        self.error_messages = []
        
        grid = self.ids["grid"]
        for i in range(81) :
            text_input = SudokuCell()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)

        self.text_inputs[ 0].text = "3";
        self.text_inputs[ 1].text = "4";
        self.text_inputs[ 3].text = "8";
        self.text_inputs[ 4].text = "2";
        self.text_inputs[ 5].text = "6";
        self.text_inputs[ 7].text = "7";
        self.text_inputs[ 8].text = "1";
        self.text_inputs[11].text = "8";
        self.text_inputs[15].text = "9";
        self.text_inputs[18].text = "7";
        self.text_inputs[19].text = "6";
        self.text_inputs[22].text = "9";
        self.text_inputs[25].text = "4";
        self.text_inputs[26].text = "3";
        self.text_inputs[28].text = "8";
        self.text_inputs[30].text = "1";
        self.text_inputs[32].text = "2";
        self.text_inputs[34].text = "3";
        self.text_inputs[37].text = "3";
        self.text_inputs[43].text = "9";
        self.text_inputs[46].text = "7";
        self.text_inputs[48].text = "9";
        self.text_inputs[50].text = "4";
        self.text_inputs[52].text = "1";
        self.text_inputs[54].text = "8";
        self.text_inputs[55].text = "2";
        self.text_inputs[58].text = "4";
        self.text_inputs[61].text = "5";
        self.text_inputs[62].text = "9";
        self.text_inputs[65].text = "7";
        self.text_inputs[69].text = "3";
        self.text_inputs[72].text = "4";
        self.text_inputs[73].text = "1";
        self.text_inputs[75].text = "3";
        self.text_inputs[76].text = "8";
        self.text_inputs[77].text = "9";
        self.text_inputs[79].text = "6";
        self.text_inputs[80].text = "2"
    
    # คืนค่า 0 หากไม่มีการระบุค่า
    def get_value(self, row, col):
        text  = self.text_inputs[9 * row + col].text
        return int(text) if len(text) > 0 else 0

    def solve(self):
        # อ่านค่าจากในช่อง
        values = [[self.get_value(row, col) for col in range(9)] for row in range(9)]
        # พยายามแก้โจทย์
        solver = Sudoku(values)
        if solver.solve():
            for row in range(9):
                for col in range(9):
                    self.text_inputs[9 * row + col].text = str(solver.get_value(row, col))
        else:
            error_message = ErrorMessage()
            self.error_messages.append(error_message)
            self.add_widget(error_message)
            Clock.schedule_once(self.remove_error_message, 2)

    # ลบ eorror massege บนจอ
    def remove_error_message(self, dt):
        error_message = self.error_messages.pop()
        self.remove_widget(error_message)
        
class SudokuScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs    = []
        self.error_messages = []

        grid = self.ids["grid"]
        for i in range(81) :
            text_input = SudokuCell()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)

        self.text_inputs[ 1].text = "9";
        self.text_inputs[ 5].text = "5";
        self.text_inputs[ 7].text = "6";
        self.text_inputs[ 9].text = "7";
        self.text_inputs[10].text = "4";
        self.text_inputs[15].text = "1";
        self.text_inputs[16].text = "9";
        self.text_inputs[23].text = "3";
        self.text_inputs[26].text = "4";
        self.text_inputs[28].text = "3";
        self.text_inputs[30].text = "6";
        self.text_inputs[31].text = "2";
        self.text_inputs[34].text = "5";
        self.text_inputs[46].text = "6";
        self.text_inputs[49].text = "3";
        self.text_inputs[50].text = "9";
        self.text_inputs[52].text = "7";
        self.text_inputs[57].text = "1";
        self.text_inputs[64].text = "1";
        self.text_inputs[65].text = "6";
        self.text_inputs[70].text = "4";
        self.text_inputs[71].text = "5";
        self.text_inputs[73].text = "2";
        self.text_inputs[75].text = "9";
        self.text_inputs[79].text = "1";

    def get_value(self, row, col):
        text  = self.text_inputs[9 * row + col].text
        return int(text) if len(text) > 0 else 0

    def solve(self):
        values = [[self.get_value(row, col) for col in range(9)] for row in range(9)]
        solver = Sudoku(values)
        if solver.solve():
            for row in range(9):
                for col in range(9):
                    self.text_inputs[9 * row + col].text = str(solver.get_value(row, col))

        else:
            error_message = ErrorMessage()
            self.error_messages.append(error_message)
            self.add_widget(error_message)
            Clock.schedule_once(self.remove_error_message, 2)

    def remove_error_message(self, dt):
        error_message = self.error_messages.pop()
        self.remove_widget(error_message)

class SudokuScreen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs    = []
        self.error_messages = []

        grid = self.ids["grid"]
        for i in range(81) :
            text_input = SudokuCell()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)

        self.text_inputs[ 1].text = "6";
        self.text_inputs[ 2].text = "8";
        self.text_inputs[ 6].text = "3";
        self.text_inputs[12].text = "1";
        self.text_inputs[21].text = "3";
        self.text_inputs[24].text = "7";
        self.text_inputs[27].text = "5";
        self.text_inputs[28].text = "2";
        self.text_inputs[35].text = "4";
        self.text_inputs[38].text = "1";
        self.text_inputs[41].text = "6";
        self.text_inputs[42].text = "8";
        self.text_inputs[66].text = "4";
        self.text_inputs[69].text = "5";
        self.text_inputs[76].text = "1";
        self.text_inputs[79].text = "6";

    def get_value(self, row, col):
        text  = self.text_inputs[9 * row + col].text
        return int(text) if len(text) > 0 else 0

    def solve(self):
        values = [[self.get_value(row, col) for col in range(9)] for row in range(9)]
        solver = Sudoku(values)
        if solver.solve():
            for row in range(9):
                for col in range(9):
                    self.text_inputs[9 * row + col].text = str(solver.get_value(row, col))

        else:
            error_message = ErrorMessage()
            self.error_messages.append(error_message)
            self.add_widget(error_message)
            Clock.schedule_once(self.remove_error_message, 2)

    def remove_error_message(self, dt):
        error_message = self.error_messages.pop()
        self.remove_widget(error_message)

class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SudokuScreen1(name='easy'))
        sm.add_widget(SudokuScreen2(name='medium'))
        sm.add_widget(SudokuScreen3(name='hard'))
        return sm

class SudokuCell(TextInput):
    pass

class ErrorMessage(Label):
    pass

if __name__ == '__main__':
    GameApp().run()