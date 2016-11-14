from plot.tk.listTK import upgrade_dimension


def test():
    a = [0, 1]
    n = 2
    solution = [[0], [1]]
    answer = upgrade_dimension(a, n)
    assert answer == solution
