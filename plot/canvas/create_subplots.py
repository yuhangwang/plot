"""
Create a figure object
"""
from typing import Dict
import copy
import matplotlib


def create_subplots(params):
    # type: (Dict) -> Dict
    """Create a new figure object

    Args:
        params (dict): plotting parameters

    Returns:
        a parameter dict with a new field "figure"
        which contains the new figure object
    """
    params['canvas']['figure'],
    params['canvas']['axis'] = matplotlib.pyplot.subplots(
                nrows=params['global']['figure']['rows'],
                ncols=params['global']['figure']['columns'],
                figsize=(params['global']['figure']['width'],
                         params['global']['figure']['height']),
                sharex=params['global']['axis']['share']['x'],
                sharey=params['global']['axis']['share']['y'],
                squeeze=False
            )
    return params
