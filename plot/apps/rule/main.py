"""
Draw a straight line (rule)
"""
from typing import Dict
from .draw_rule import draw_rule


def main(params):
    # type: (Dict) -> Dict
    """Draw a straight line (rule)

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    line_objects = draw_rule(params)
    return params
