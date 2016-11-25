"""
Draw a matrix
"""
from typing import Dict
from .draw_matrix import draw_matrix


def main(params):
    # type: (Dict) -> Dict
    """Draw a matrix object

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    line_objects = draw_matrix(params)
    return params
