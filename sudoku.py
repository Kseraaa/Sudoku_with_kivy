class Sudoku():
    def __init__(self, values):
        self.grid = values

    def get_value(self, row, col):
        return self.grid[row][col]

    def solve(self):
        if not self._is_valid_grid():
            return False
        return self._solve()

    def _is_valid_grid(self):
        for i in range(9):
            # เช็คแถว
            possible_row = [True for v in range(9)]
            for j in range(9):
                val = self.grid[i][j]
                if ( val > 0 ):
                    if possible_row[val - 1]:
                        possible_row[val - 1] = False
                    else:
                        return False
            # เช็คคอลัมน์
            possible_col = [True for v in range(9)]
            for j in range(9):
                val = self.grid[j][i]
                if ( val > 0 ):
                    if possible_col[val - 1]:
                        possible_col[val - 1] = False
                    else:
                        return False
            # เช็คตารางย่อย
            possible_squ = [True for v in range(9)]
            row_min, col_min = 3 * (i // 3), 3 * (i  % 3)
            for j in range(row_min, row_min + 3):
                for k in range(col_min, col_min + 3):
                    val = self.grid[j][k]
                    if ( val > 0 ):
                        if possible_squ[val - 1]:
                            possible_squ[val - 1] = False
                        else:
                            return False
        return True

    def _solve(self):
        # หากไม่พบช่องที่ว่าง แสดงว่าตารางเต็มแล้ว
        row, col, values = self._get_free_cell()
        if row < 0 or col < 0:
            return True
        # ลองค่าที่เป็นไปได้ทั้งหมดสำหรับช่องนั้น ๆ
        for v in values:
            # ลองใส่ค่านั้น ในตาราง
            self.grid[row][col] = v;
            if self._solve():
                return True
            # ถ้าไม่มีค่าใดเป็นไปได้ ก็คืนค่าเดิม
            self.grid[row][col] = 0;
        return False

    def _get_free_cell(self):
        row, col, values = -1, -1, []
        # เทสช่องทั้งหมดในตาราง
        for i in range(9):
            for j in range(9):
                # เช็คหาช่องที่ว่าง
                if self.grid[i][j] != 0:
                    continue
                # หาค่าที่เป็นไปได้สำหรับช่องนั้น ๆ
                ok, cell_values = self._get_possible_values(i, j, len(values) if len(values) > 0 else 10)
                if ok:
                    row    = i
                    col    = j
                    values = cell_values
                    if len(values) <= 1:  # ถ้ามีแค่ค่าเดียว ก็ใส่ค่านั้นไป
                        return row, col, values
        return row, col, values

    def _get_possible_values(self, row, col, only_if_better_than):
        nb_possible = 9
        possible    = [True,True,True,True,True,True,True,True,True]
        # เช็คตามแถวและคอลัมน์
        for i in range(9):
            val_row = self.grid[row][i]
            if val_row > 0 and possible[val_row - 1]:
                possible[val_row - 1] = False
                nb_possible -= 1
            val_col = self.grid[i][col]
            if val_col > 0 and possible[val_col - 1]:
                possible[val_col - 1] = False
                nb_possible -= 1
        # เช็คในตารางย่อย
        row_min, col_min = 3 * (row // 3), 3 * (col // 3);
        for i in range(row_min, row_min + 3):
            for j in range(col_min, col_min + 3):
                val = self.grid[i][j]
                if val > 0 and possible[val - 1]:
                    possible[val - 1] = False
                    nb_possible -= 1
        # ใส่ค่าที่เป็นไปได้ทั้งหมด
        if nb_possible < only_if_better_than:
            values = []
            for i in range(9):
                if possible[i]:
                    values.append(i + 1)
            return True, values
        return False, []

    def __str__(self):
        out = "";
        for row in range(9):
            out += " ".join(map(str, self.grid[row])) + "\n"
        return out