"""
Draw bars
"""
from typing import Dict
from .draw_bars import draw_bars


def main(params):
    # type: (Dict) -> Dict
    """Draw bar objects

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    line_objects = draw_bars(params)
    return params