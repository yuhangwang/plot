"""
Draw a line
"""
from typing import Dict
from .get_data import get_data
from .get_x_y import get_x_y
from .get_error_bars import get_error_bars


def draw_line(params):
    # type: (Dict) -> Dict
    """Draw line objects

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    for p in params['data']:
        if p['plot type'] != 'line':
            continue
        else:
            data = get_data(p)
            if data is None:
                continue
            else:
                X, Y = get_x_y(data, p)
                x_bars, y_bars = get_error_bars(data, p)
