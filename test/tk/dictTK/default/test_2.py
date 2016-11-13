from plot.tk.dictTK import default


def test():
    d1 = {"k0": {"__": "k0", "k1": {"__": "k1", "v": [1, 2, 3]}}}
    solution = {"k0": {"__": "k0", "k1": {"__": "k1", "v": 1}}}
    assert default(d1) == solution
