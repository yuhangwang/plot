from plot.tk.dict import merge
def test():
    dict1 = {"a":{"a1":1}}
    dict2 = {"a":{"b1":1}}
    solution = {'a':{"a1":1, "b1":1}}
    answer = merge(dict1, dict2)
    assert answer == solution
