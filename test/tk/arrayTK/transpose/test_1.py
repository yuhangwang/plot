from plot.tk.arrayTK import transpose


def test():
    a = [[1, 2], [3, 4]]
    answer = transpose(a, True)
    solution = [[1, 3], [2, 4]]
    assert answer.tolist() == solution
