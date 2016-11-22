"""
Refine the properties of legend
"""
from typing import Dict
from ...tk.matplotlibTK.legend import refine_legend


def finetune_legend(params):
    # type: (Dict) -> Dict
    """Refine legend properties

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for p in params['local']:
        panel_id = p['which_panel']
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        refine_legend(obj_axis, p['legend'])
    return params
