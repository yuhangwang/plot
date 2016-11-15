"""
Draw a line
"""
from typing import Dict
from .get_data import get_data
from .get_x_y import get_x_y


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
            X, Y = get_x_y(get_data(p), p)
            if data is None:
                continue
            else:
