"""
Initialize the internal panel color bar
"""
from typing import Dict
from ....tk.arrayTK import all_indexes


def initialize_panel_legend(params):
    # type: (Dict) -> Dict
    """Initialize the internal panel color bar

    Args:
        params(dict): plotting parameters

    Returns:
        updated params
    """
    params['internal']['panel']['color_bar'] = dict()
    for p in params['data']:
        k = p['color_bar']['which_panel']
        if k is not None:
            params['internal']['panel']['color_bar'][k] = []
        else:
            pass
    return params
