from plot.tk.dict import merge
def test():
    dict1 = {"a":{"a1":1}}
    dict2 = {"a":{"a1":2}, "b":1}
    solution = {'a':{"a1":2}, "b":1}
    answer = merge(dict1, dict2)
    assert answer == solution
