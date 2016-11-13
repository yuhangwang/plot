from plot.tk.dict import convert_to_internal


def test():
    user_dict = {"public": {"v": 1, "__": "internal"}}
    solution = {"internal": {"v": 1}}
    answer = convert_to_internal(user_dict)
    assert answer == solution
