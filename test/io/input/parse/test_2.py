from plot.io.input import parse
import os


def test():
    here = os.path.dirname(os.path.realpath(__file__))
    user_file = os.path.join(here, "data", "in2.yaml")
    default_file = os.path.join(here, "data", 'default1.yaml')
    solution = {
        'local': [{'which_panel': (0, 0, 0, 0)}],
        'data':  [{'which_panel': (0, 0, 0, 0), 'local_id': 0}],
        'global': {'k_1': 1001},
        }
    answer = parse(user_file, default_file)
    assert answer == solution
