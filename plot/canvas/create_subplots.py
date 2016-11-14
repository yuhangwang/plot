"""
Create a figure object
"""
from typing import Dict
import copy
import matplotlib.pyplot


def create_subplots(params):
    # type: (Dict) -> Dict
    """Create a new figure object

    Args:
        params (dict): plotting parameters

    Returns:
        a parameter dict with a new field "figure"
        which contains the new figure object
    """
    fig, axes = matplotlib.pyplot.subplots(
                nrows=params['global']['figure']['rows'],
                ncols=params['global']['figure']['columns'],
                figsize=(params['global']['figure']['width'],
                         params['global']['figure']['height']),
                sharex=params['global']['figure']['axis']['share']['x'],
                sharey=params['global']['figure']['axis']['share']['y'],
                squeeze=False
            )
    params['canvas']['figure'] = fig
    params['canvas']['axes'] = axes
    return params
