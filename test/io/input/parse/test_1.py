from plot.io.input import parse
import os


def test():
    here = os.path.dirname(os.path.realpath(__file__))
    user_file = os.path.join(here, "data", "in1.yaml")
    default_file = os.path.join(here, "data", 'default1.yaml')
    solution = {
        'local': [{'k_1': 11}],
        'data':  [{'k_1': 101}],
        'global': {'k_1': 0},
        }
    answer = parse(user_file, default_file)
    assert answer == solution
