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
            sleep(1)
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
        for self.y in range(9):
            for self.x in range(9):
                if not valid_chunk(self.at_box()) or not valid_chunk(self.at_row()) or not valid_chunk((self.at_col())):
                    print('Invalid at: {0}, {1}'.format(self.x, self.y))
                    return False
        return True

    def at_box(self):
        global sodoku, chunks
        tmp_col, tmp_row = [], []
        for chunk in chunks:
            if self.x in chunk:
                tmp_col = chunk
            if self.y in chunk:
                tmp_row = chunk

        box = [sodoku[row][col] for row in tmp_row for col in tmp_col]
        return box

    def chk_box(self, num):
        at_box = self.at_box()
        if num not in at_box:
            return True
        else:
            return False

    def at_row(self):
        global sodoku
        row = [sodoku[self.y][i] for i in range(9)]
        return row

    def chk_row(self, num):
        at_row = self.at_row()
        if num not in at_row:
            return True
        else:
            return False

    def at_col(self):
        global sodoku
        col = [sodoku[i][self.x] for i in range(9)]
        return col

    def chk_col(self, num):
        at_col = self.at_col()
        if num not in at_col:
            return True
        else:
            return False


sodoku = [
    '7 _ _ _ _ 1 _ _ 5'.split(),
    '_ _ 8 3 _ _ _ _ _'.split(),
    '3 5 6 _ 4 9 _ 1 _'.split(),
    '_ _ _ 7 6 4 1 _ _'.split(),
    '_ _ _ _ 9 _ 4 _ _'.split(),
    '_ 7 _ _ _ _ _ _ 3'.split(),
    '_ 6 3 _ _ _ _ _ _'.split(),
    '_ _ _ 9 _ _ _ 3 8'.split(),
    '1 8 _ _ _ _ _ _ _'.split(),
]

chunks = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

correct = set([str(x) for x in range(1, 10)])

"""Demo Section"""
slvr = SodokuSolver()
slvr.solve()
if slvr.validate():
    print('Valid! :3')
else:
    print('Invalid! :(')