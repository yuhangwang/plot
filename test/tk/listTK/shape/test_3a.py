from plot.tk.listTK import shape


def test():
    a = [[[1], [1]], [[2], [2]]]
    solution = [2, 2, 1]
    answer = shape(a)
    assert answer == solution
