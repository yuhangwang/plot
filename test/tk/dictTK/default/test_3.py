from plot.tk.dictTK import default


def test():
    d1 = {"k0": [{"a": {"v": [1,2]}}]}
    solution = {"k0": [{"a": {"v": 1}}]}
    assert default(d1) == solution
