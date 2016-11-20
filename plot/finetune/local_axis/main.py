"""
Adjust the local figure axis
"""
from typing import Dict
from ...tk.fnTK import compose
from .add_grid_lines import add_grid_lines
from .refine_legend import refine_legend


def main(params):
    # type: (Dict) -> Dict
    """Adjust local axis parameters

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    aux = compose([
        add_grid_lines,
        refine_legend,
        ])
    return aux(params)
