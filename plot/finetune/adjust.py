"""
Make adjustments to figure axes
"""
from typing import Dict
from .global_axis import adjust as adjust_global_axis
from .local_axis import adjust as adjust_local_axis
from ..tk.fnTK import compose


def adjust(params):
    # type: (Dict) -> Dict
    """Adjust figure/axes

    Adjust global and local axes.

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    tweek = compose([
        adjust_global_axis,
        adjust_local_axis,
        ])
    return tweek(params)
