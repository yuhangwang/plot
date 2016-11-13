from plot.tk.dictTK import wrap_value


def test():
    d1 = {'k0': {'k1': 1}}
    solution = {'k0': {'k1': {'v': 1}}}
    assert wrap_value(d1) == solution
