"""
Convert value of "which_panel" to proper format
"""
from typing import Dict
from ...tk.listTK import upgrade_index
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
    ooo = copy.deepcopy(params)
    for k in ooo:
        if k == "which_panel":
            ooo[k] = tuple(upgrade_index(ooo[k], new_dim))
        elif isinstance(ooo[k], dict):
            ooo[k] = format_panel_index(ooo[k], new_dim)
        else:
            continue
    return ooo
