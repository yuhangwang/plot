"""
Adjust the local figure axis
"""
from typing import Dict
from ...tk.fnTK import compose
from .add_grid_lines import add_grid_lines
from .finetune_legend import finetune_legend
from .tighten_panel_axis_range import tighten_panel_axis_range
from .set_axis_range import set_axis_range
from .add_color_bar import add_color_bar
from .set_axis_tick_direction import set_axis_tick_direction


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
        finetune_legend,
        tighten_panel_axis_range,
        set_axis_range,
        add_color_bar,
        set_axis_tick_direction
        ])
    return aux(params)
