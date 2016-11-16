from plot.tk.arrayTK import minmax


def test():
    xs = []
    solution = []
    answer = minmax(xs)
    assert answer == solution
