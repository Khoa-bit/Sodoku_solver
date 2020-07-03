sodoku = [
    '_ _ _ 1 _ 7 3 _ _'.split(),
    '_ _ 7 _ 2 8 5 _ _'.split(),
    '_ 6 _ 3 _ _ _ 9 _'.split(),
    '_ 9 4 6 3 _ _ _ 8'.split(),
    '_ 3 2 _ 9 _ 1 7 _'.split(),
    '6 _ _ _ 8 2 4 3 _'.split(),
    '_ 2 _ _ _ 6 _ 1 _'.split(),
    '_ _ 6 5 4 _ 8 _ _'.split(),
    '_ _ 9 2 _ 3 _ _ _'.split(),
]

bounds = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

correct = {str(x) for x in range(1, 10)}