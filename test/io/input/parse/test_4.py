from plot.io.input import parse
import os


def test():
    here = os.path.dirname(os.path.realpath(__file__))
    user_file = os.path.join(here, "data", "in4.yaml")
    default_file = os.path.join(here, "data", 'default3.yaml')
    solution = {
        'local': [{'which_panel': (1, 2, 0, 0)}],
        'data':  [{
            'which_panel': (1, 2, 3, 0),
            'legend': {
                'which_panel': (1, 1, 0, 0)
            }
        }],
        'global': {'k_1': 1001},
        }
    answer = parse(user_file, default_file)
    assert answer == solution
