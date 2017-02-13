"""
Draw a region (using fill_between)
"""
from typing import Dict
from .draw_regions import draw_regions


def main(params):
    # type: (Dict) -> Dict
    """Draw line objects

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    objects = draw_regions(params)
    return params
