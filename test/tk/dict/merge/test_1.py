from plot.tk.dict import merge
def test():
    dict1 = {"a":1}
    dict2 = {"b":1}
    solution = {'a':1, 'b':1}
    answer = merge(dict1, dict2)
    assert answer == solution
