from plot.tk.fnTK import compose


def test():
    f = compose([])
    assert f(0) == 0
