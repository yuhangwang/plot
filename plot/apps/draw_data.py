"""
Draw all data
"""
from typing import Dict
from .line import draw as draw_lines


def draw_data(params):
    # type: (Dict) -> Dict
    """Draw all data

    Args:
        params (dict): parameter dictionary

    Returns:
        the same parameter dictionary
    """
    return draw_lines(params)
