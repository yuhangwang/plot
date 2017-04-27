from plot.tk.dictTK import update


def test():
    dict1 = {"a": [{"a1": 1}, {"a1": 2}]}
    dict2 = {"a": [{"a1": 0}]}
    solution = {'a': [{"a1": 1}, {"a1": 2}]}
    answer = update(dict1, dict2)
    assert answer == solution
