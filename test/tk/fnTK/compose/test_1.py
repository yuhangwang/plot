from plot.tk.fnTK import compose


def test():
    def add1(x): return x + 1
    f = compose([add1, add1, add1, add1])
    assert f(0) == 4
