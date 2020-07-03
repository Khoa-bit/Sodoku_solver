class SodokuSolver:
    def __init__(self):
        self.x = 3
        self.y = 5

    def chk_box(self):
        global sodoku, chunks
        tmp_col, tmp_row = [], []
        for chunk in chunks:
            if self.x in chunk:
                tmp_col = chunk
            if self.y in chunk:
                tmp_row = chunk

        for row in tmp_row:
            for col in tmp_col:
                print(sodoku[row][col], end=' ')

    def chk_row(self):
        global sodoku
        for i in range(9):
            print(sodoku[self.y][i], end=' ')

    def chk_col(self):
        global sodoku
        for i in range(9):
            print(sodoku[i][self.x], end=' ')


sodoku = [
    '5 3 _ _ 7 _ _ _ _ '.split(),
    '6 _ _ 1 9 5 _ _ _ '.split(),
    '_ 9 8 _ _ _ _ 6 _ '.split(),
    '8 _ _ _ 6 _ _ _ 3 '.split(),
    '4 _ _ 8 _ 3 _ _ 1 '.split(),
    '7 _ _ _ 2 _ _ _ 6 '.split(),
    '_ 6 _ _ _ _ 2 8 _ '.split(),
    '_ _ _ 4 1 9 _ _ 5 '.split(),
    '_ _ _ _ 8 _ _ 7 9 '.split(),
]

chunks = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]


"""Demo Section"""
slvr = SodokuSolver()
slvr.chk_col()
print()
slvr.chk_row()
print()
slvr.chk_box()
