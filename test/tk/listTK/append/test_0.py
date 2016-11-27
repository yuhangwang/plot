from plot.tk.listTK import append


def test():
    a = []
    answer = append(a, [], 1)
    solution = [1]
    assert answer == solution
