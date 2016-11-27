from plot.tk.listTK import append


def test():
    a = [[[1]]]
    answer = append(a, [0, 0, 0], 2)
    solution = [[[1, 2]]]
    assert answer == solution
