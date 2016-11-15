from plot.tk.listTK import upgrade_index


def test():
    a = []
    dim = 2
    solution = [0, 0]
    answer = upgrade_index(a, dim)
    assert answer == solution
