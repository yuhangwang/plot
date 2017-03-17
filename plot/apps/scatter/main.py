"""
Draw a scatter plot
"""
from typing import Dict
from .draw_many import draw_many


def main(params):
    # type: (Dict) -> Dict
    """Draw scattered dots/shapes

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    objects = draw_many(params)
    return params
