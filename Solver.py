import assets
from time import sleep
from copy import deepcopy


class Solver:
    def __init__(self, s_map=assets.sodoku):
        self.x = 0
        self.y = 0
        self.s_map = s_map
        self.possibilities = []

    def __repr__(self):
        return '<x: {0!r}, y: {1!r}, possibilities: {2!r}>, map: {3!r}'\
            .format(self.x, self.y, self.possibilities, self.s_map)

    def run(self):
        succeed = self.brute_force()
        if not succeed:
            tmp_map = self.test_possibilities()
            if tmp_map is not None:
                self.s_map = tmp_map
        valid = self.validate()
        return valid

    def at_row(self):
        row = [self.s_map[self.y][i] for i in range(9)]
        return row

    def at_col(self):
        col = [self.s_map[i][self.x] for i in range(9)]
        return col

    def at_box(self):
        tmp_col, tmp_row = [], []
        for bound in assets.bounds:
            if self.x in bound:
                tmp_col = bound
            if self.y in bound:
                tmp_row = bound

        box = [self.s_map[row][col] for row in tmp_row for col in tmp_col]
        return box

    def at_pos(self):
        return set(self.at_row() + self.at_col() + self.at_box())

    def brute_force(self):
        changes = True
        min_possibilities = 10
        while changes:
            changes = False
            self.possibilities = []
            # show(self.x, self.y)
            # sleep(2)
            for self.y in range(9):
                for self.x in range(9):
                    if self.s_map[self.y][self.x] == '_':
                        possibilities = list(assets.correct.difference(self.at_pos()))
                        length = len(possibilities)
                        if length == 1:
                            self.s_map[self.y][self.x] = possibilities[0]
                            # print('Changed!')
                            changes = True
                        elif length <= min_possibilities:
                            min_possibilities = length
                            self.possibilities = [[self.x, self.y], possibilities]
        # show(self.x, self.y)
        # print('NO Changed!')
        if len(self.possibilities) != 0 and len(self.possibilities[1]) != 0:
            # print('BF false')
            return False
        else:
            # print('BF true')
            return True

    def test_possibilities(self):
        for possibility in self.possibilities[1]:
            test_s_map = deepcopy(self.s_map)
            test_x, test_y = self.possibilities[0][0], self.possibilities[0][1]
            test_s_map[test_y][test_x] = possibility
            print('Test: Possibilities {0!r}'.format(self.possibilities))
            print('Test: Replaced {0!r} at ({1}, {2})'.format(possibility, test_x, test_y))
            # sleep(2)
            test_solver = Solver(test_s_map)
            if test_solver.run():
                return test_solver.s_map

    def validate(self):
        for self.y in range(9):
            for self.x in range(9):
                check = assets.correct.difference(self.at_pos())
                if len(check) != 0:
                    print('Invalid')
                    return False
        print('Valid')
        return True

    def show(self):
        print('At: ({0}, {1})'.format(self.x, self.y))
        for y in range(9):
            print(assets.sodoku[y])
