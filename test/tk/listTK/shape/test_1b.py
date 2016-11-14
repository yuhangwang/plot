from plot.tk.listTK import shape


def test():
    a = [1, 2]
    solution = [2]
    answer = shape(a)
    assert answer == solution
