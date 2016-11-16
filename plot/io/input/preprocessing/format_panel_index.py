"""
Convert value of "which_panel" to proper format
"""
from typing import Dict
from ....tk.listTK import upgrade_index
import copy


def format_panel_index(params, new_dim=4):
    # type: (Dict, int) -> Dict
    """Convert the value of "panel_index" to proper format

    Example: [0, 0] will be changed to tuple(0, 0, 0, 0)

    Args:
        params (dict): internal parameter dictionary
        new_dim (int): (optional) new dimension of the index

    Return:
        updated internal parameter dictionary
    """
    for k in params:
        if k == "which_panel":
            params[k] = tuple(upgrade_index(params[k], new_dim))
        elif isinstance(params[k], dict):
            params[k] = format_panel_index(params[k], new_dim)
        else:
            continue
    return params
