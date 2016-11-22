"""
Initialize the internal panel legend parameter field
"""
from typing import Dict
from ....tk.arrayTK import all_indexes


def initialize_panel_legend(params):
    # type: (Dict) -> Dict
    """Initialize the internal panel legend parameter field

    Args:
        params(dict): plotting parameters

    Returns:
        updated params
    """
    params['internal']['panel']['legend'] = dict()
    for p in params['data']:
        k = p['legend']['which_panel']
        if k is not None:
            params['internal']['panel']['legend'][k] = []
        else:
            pass
    return params
