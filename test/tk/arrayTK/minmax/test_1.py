from plot.tk.arrayTK import minmax


def test():
    xs = [[1, 2, 3]]
    solution = [[1, 3]]
    answer = minmax(xs)
    assert answer == solution
