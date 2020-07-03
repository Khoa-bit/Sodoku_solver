from time import sleep

def show_sodoku():
    for y in range(9):
        print(sodoku[y])


def valid_chunk(arr):
    global correct
    diff = correct.difference(set(arr))
    if len(diff) == 0:
        return True
    else:
        return False


class SodokuSolver:
    def __init__(self):
        self.x = 2
        self.y = 0
        self.blank = []

    def solve(self):
        finished = False
        while not finished:
            show_sodoku()
            sleep(2)
            finished = True
            for self.y in range(9):
                for self.x in range(9):
                    if sodoku[self.y][self.x] == '_':
                        finished = False
                        possible_sol = '_'
                        for chk_num in range(1, 10):
                            chk_num = str(chk_num)
                            if self.chk_box(chk_num) and self.chk_row(chk_num) and self.chk_col(chk_num):
                                if possible_sol != '_':
                                    possible_sol = '_'
                                    break
                                else:
                                    possible_sol = chk_num
                        sodoku[self.y][self.x] = possible_sol
            print('===================================')

    def validate(self):
        valid = True
        for y in range(9):
            for x in range(9):
                if self.chk_box()

    def chk_box(self, num):
        global sodoku, chunks
        tmp_col, tmp_row = [], []
        for chunk in chunks:
            if self.x in chunk:
                tmp_col = chunk
            if self.y in chunk:
                tmp_row = chunk

        box = [sodoku[row][col] for row in tmp_row for col in tmp_col]
        if num not in box:
            return True
        elif '_' not in box:
            return valid_chunk(box)
        else:
            return False


    def chk_row(self, num):
        global sodoku
        row = [sodoku[self.y][i] for i in range(9)]
        if num not in row:
            return True
        elif '_' not in row:
            return valid_chunk(row)
        else:
            return False

    def chk_col(self, num):
        global sodoku
        col = [sodoku[i][self.x] for i in range(9)]
        if num not in col:
            return True
        elif '_' not in col:
            return valid_chunk(col)
        else:
            return False


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

correct = set([x for x in range(1, 10)])


"""Demo Section"""
slvr = SodokuSolver()
slvr.solve()
slvr.solve()
