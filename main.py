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

def chk_row(nth_row):
    for i in range(9):
        print(sodoku[nth_row][i], end=' ')


def chk_col(nth_col):
    for i in range(9):
        print(sodoku[i][nth_col], end=' ')


"""Demo Section"""
chk_row(1)
print()
chk_col(0)
