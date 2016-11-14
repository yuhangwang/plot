from plot.tk.listTK import upgrade_dimension


def test():
    a = []
    n = 2
    solution = [[]]
    answer = upgrade_dimension(a, n)
    assert answer == solution
