"""
Adjust the global figure axis
"""
from typing import Dict
from .add_axis_labels import add_axis_labels
from ...tk.fnTK import compose


def adjust(params):
    # type: (Dict) -> Dict
    """Adjust global parameters

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    aux = compose([
        add_axis_labels
        ])
    return aux(params)
