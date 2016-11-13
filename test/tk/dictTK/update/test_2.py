from plot.tk.dictTK import update


def test():
    dict1 = {"b": 2}
    dict2 = {"a": 1}
    solution = {'a': 1}
    answer = update(dict1, dict2)
    assert answer == solution
