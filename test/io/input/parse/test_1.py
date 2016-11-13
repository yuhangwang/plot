from plot.io.input import parse
import os


def test():
    user_file = os.path.join(os.getcwd(), "data", "in1.yaml")
    default_file = os.path.join(os.getcwd(), "data", 'default1.yaml')
    solution = {'local': {'k1': 1}}
    answer = parse(user_file, default_file)
    assert answer == solution
