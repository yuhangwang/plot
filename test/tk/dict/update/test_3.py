from plot.tk.dict import update


def test():
    dict1 = {"a": 2}
    dict2 = {"a": 1, "b": 3}
    solution = {'a': 2, "b": 3}
    answer = update(dict1, dict2)
    assert answer == solution
