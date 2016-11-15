"""
Create a figure object
"""
from typing import Dict
import copy
import matplotlib.pyplot
from .subplot_spacing import subplot_spacing
from .global_axis import global_axis
from ...tk.fnTK import compose


def create(params):
    # type: (Dict) -> Dict
    """Create a new figure object

    Args:
        params (dict): plotting parameters

    Returns:
        a parameter dict with a new field "figure"
        which contains the new figure object
    """
    # axes is a numpy.ndarray
    # axes[0,0] is an instance of <class 'matplotlib.axes._subplots.AxesSubplot'>
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
    tweek = compose([subplot_spacing, global_axis])
    return tweek(params)
