"""
Add global axes to the entire figure.
"""
from typing import Dict


def global_axis(params):
    # type: (Dict) -> Dict
    """Add global axes to the figure

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        an updated dictionary with a new field ['canvas']['global_axes']
    """
    params['canvas']['global_axis'] = (
        params['canvas']['figure'].add_subplot(1, 1, 1))
    return params
