from plot.tk.dictTK import convert_to_internal


def test():
    user_dict = {"public": {"v": 1, "__": "internal"}}
    solution = {"internal": 1}
    answer = convert_to_internal(user_dict)
    assert answer == solution
