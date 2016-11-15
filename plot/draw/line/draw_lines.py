"""
Draw lines (with error bars if defined)
"""
from typing import List, Dict
from .read_data import read_data
from .extract_data_x_y import extract_data_x_y
from .extract_data_error_bar import extract_data_error_bar


def draw_lines(params):
    # type: (Dict) -> Dict
    """Draw lines

    Draw lines, with error bars if defined.

    Args:
        params (dict): a complete parameter dictionary

    Returns:
        a list of line objects
    """
    def tail(xs): return xs[1:]

    def aux(line_params, accum):
        # type: (List, List) -> List
        if len(line_params) == 0:
            return accum
        elif line_params[0]['plot type'] != 'line':
            return aux(tail(line_params), accum)
        else:
            p = line_params[0]
            data = read_data(p)
            if data is None:
                return aux(tail(line_params), accum)
            else:
                X, Y = extract_data_x_y(data, p)
                x_bars, y_bars = extract_data_error_bar(data, p)
                index = p['which_panel']
                return aux(tail(line_params))
    return aux(params['data'], [])
