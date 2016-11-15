from plot.tk.listTK import upgrade_index


def test():
    a = [1, 2]
    dim = 2
    solution = [1, 2]
    answer = upgrade_index(a, dim)
    assert answer == solution
