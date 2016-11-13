from plot.tk.dictTK import update


def test():
    dict1 = {"a": {"a1": 1}}
    dict2 = {"a": {"a1": 2}}
    solution = {'a': {"a1": 1}}
    answer = update(dict1, dict2)
    assert answer == solution
