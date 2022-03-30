import unittest
from sudoku import Sudoku

class Sudoku_Test(unittest.TestCase):

    def test_sudoku_zaza1(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res =sudo.get_value(5, 1) #เอาrow5col1
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_zaza2(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res =sudo.get_value(6, 2) #เอาrow6col2
        res = sudo.solve()
        self.assertTrue(res)
    
    def test_sudoku_zaza3(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res =sudo.get_value(3, 3) #เอาrow3col3
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_zaza4(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res =sudo.get_value(8, 2) #เอาrow8col2
        res = sudo.solve()
        self.assertTrue(res)