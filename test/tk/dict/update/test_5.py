from plot.tk.dict import update


def test():
    dict1 = {"a": {"a1": 1}}
    dict2 = {"a": 1}
    solution = {'a': {"a1": 1}}
    answer = update(dict1, dict2)
    assert answer == solution
