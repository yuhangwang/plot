"""
Add grids to the local axes
"""
from typing import Dict
from ...tk.matplotlibTK.grid import add_grid


def add_grid_lines(params):
    # type: (Dict) -> Dict
    """Add grids to the local axes

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    def tail(xs): return xs[1:]
    obj_figure = params['canvas']['figure']
    for p in params['local']:
        if p['grid']['show'] is True:
            panel_id = p['which_panel']
            obj_axis = params['canvas']['axes'][panel_id]
            add_grid(
                obj_axis, obj_figure, True,
                which_ticks=p['grid']['which_ticks'],
                which_axis=p['grid']['which_axis'],
                grid_line_style=p['grid']['line']['style'],
                grid_line_width=p['grid']['line']['width'],
                grid_line_color=p['grid']['line']['color'],
                grid_line_opacity=p['grid']['line']['opacity'],
                grid_z_order=p['grid']['which_layer']
            )
        else:
            continue
    return params
