import unittest
from sudoku import Sudoku

class Sudoku_Test(unittest.TestCase):

    def test_sudoku_zaza(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res =sudo.get_value(5, 1) #เอาrow5col1
        res = sudo.solve()
        self.assertTrue(res)