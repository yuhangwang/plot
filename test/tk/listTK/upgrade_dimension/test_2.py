from plot.tk.listTK import upgrade_dimension


def test():
    a = [[0, 1], [3, 4]]
    n = 4
    solution = [[[[0]], [[1]]], [[[3]], [[4]]]]
    answer = upgrade_dimension(a, n)
    assert answer == solution
