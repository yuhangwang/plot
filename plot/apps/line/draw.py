"""
Draw a line
"""
from typing import Dict
from .draw_lines import draw_lines


def draw(params):
    # type: (Dict) -> Dict
    """Draw line objects

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    line_objects = draw_lines(params)
    return params
