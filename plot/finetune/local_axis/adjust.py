"""
Adjust the local figure axis
"""
from typing import Dict
from .add_grid_lines import add_grid_lines
from ...tk.fnTK import compose


def adjust(params):
    # type: (Dict) -> Dict
    """Adjust local axis parameters

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    aux = compose([
        add_grid_lines
        ])
    return aux(params)
