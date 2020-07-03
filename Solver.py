import assets
from time import sleep


class Solver:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.map = assets.sodoku
        self.possibilities = []

    def __repr__(self):
        return '<x: {0!r}, y: {1!r}, possibilities: {2!r}>'.format(self.x, self.y, self.possibilities)

    def at_row(self):
        row = [self.map[self.y][i] for i in range(9)]
        return row

    def at_col(self):
        col = [self.map[i][self.x] for i in range(9)]
        return col

    def at_box(self):
        tmp_col, tmp_row = [], []
        for bound in assets.bounds:
            if self.x in bound:
                tmp_col = bound
            if self.y in bound:
                tmp_row = bound

        box = [self.map[row][col] for row in tmp_row for col in tmp_col]
        return box

    def at_pos(self):
        return set(self.at_row() + self.at_col() + self.at_box())

    def brute_force(self):
        changes = True
        min_possibilities = 10
        while changes:
            changes = False
            for self.y in range(9):
                for self.x in range(9):
                    show(self.x, self.y)
                    # sleep(1)
                    if self.map[self.y][self.x] == '_':
                        possibilities = list(assets.correct.difference(self.at_pos()))
                        length = len(possibilities)
                        if length == 1:
                            self.map[self.y][self.x] = possibilities[0]
                            changes = True
                        elif length <= min_possibilities:
                            min_possibilities = length
                            self.possibilities = [[self.x, self.y], possibilities]

    def validate(self):
        for self.y in range(9):
            for self.x in range(9):
                check = assets.correct.difference(self.at_pos())
                if len(check) != 0:
                    print('Invalid')
                    return False
        print('Valid')


def show(x, y):
    print('At: ({0}, {1})'.format(x, y))
    for y in range(9):
        print(assets.sodoku[y])
