from plot.tk.arrayTK import minmax


def test():
    xs = [[1, 2, 3], [10, 11, 13]]
    solution = [[1, 3], [10, 13]]
    answer = minmax(xs)
    assert answer == solution
