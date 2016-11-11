from plot.tk.dict import update


def test():
    dict1 = {"a": 2}
    dict2 = {"a": 1}
    solution = {'a': 2}
    answer = update(dict1, dict2)
    assert answer == solution
