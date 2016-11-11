from plot.tk.dict import merge
def test():
    dict1 = {"a":1}
    dict2 = {"a":2}
    solution = {'a':2}
    answer = merge(dict1, dict2)
    assert answer == solution
