from plot.tk.listTK import append


def test():
    a = [1, 3]
    answer = append(a, [0], 2)
    solution = [1, 2, 3]
    assert answer == solution
