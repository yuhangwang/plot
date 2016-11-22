"""
Draw a span regions
"""
from typing import Dict
from .draw_span import draw_span


def main(params):
    # type: (Dict) -> Dict
    """Draw span regions

    Args:
        params (dict) -> parameter dictionary

    Returns:
        the same parameter dictionary as input
    """
    line_objects = draw_span(params)
    return params
