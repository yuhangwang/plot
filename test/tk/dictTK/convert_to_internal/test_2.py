from plot.tk.dictTK import convert_to_internal


def test():
    user_dict = {"p1": {"p2": {"__": "i2", "v": 2}, "__": "i1"}}
    solution = {"i1": {"i2": 2}}
    answer = convert_to_internal(user_dict)
    assert answer == solution
