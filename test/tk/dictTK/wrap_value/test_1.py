from plot.tk.dictTK import wrap_value


def test():
    d1 = {'k0': 0}
    solution = {'k0': {'v': 0}}
    assert wrap_value(d1) == solution
