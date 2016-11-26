"""
Create a figure object
"""
from typing import Dict
import copy
import matplotlib.pyplot
from .subplot_spacing import subplot_spacing
from .global_axis import global_axis
from .create_image_grid import create_image_grid
from ...tk.fnTK import compose
from ...tk.listTK import upgrade_dimension
import numpy


def create(params):
    # type: (Dict) -> Dict
    """Create a new figure object

    Args:
        params (dict): plotting parameters

    Returns:
        a parameter dict with a new field "figure"
        which contains the new figure object
    """
    fig_id = 0
    p_fig = params['global']['figure']
    shape = (p_fig['rows'], p_fig['columns'])
    obj_fig = matplotlib.pyplot(
        num=fig_id,
        figsize=(p_fig['width'], p_fig['height']),
        facecolor=p_fig['color']['face'],
        edgecolor=p_fig['color']['edge'],
        frameon=p_fig['frame']['show'],
        dpi=p_fig['dpi']
        )
    grid = create_image_grid(obj_fig, p_fig)
    fig, axes = matplotlib.pyplot.subplots(
                nrows=params['global']['figure']['rows'],
                ncols=params['global']['figure']['columns'],
                figsize=(params['global']['figure']['width'],
                         params['global']['figure']['height']),
                sharex=params['global']['figure']['axis']['share']['x'],
                sharey=params['global']['figure']['axis']['share']['y'],
                squeeze=False
            )
    params['internal']['canvas']['figure'] = fig
    params['internal']['canvas']['axes'] = numpy.array(
        upgrade_dimension(axes.tolist(), 4))
    tweek = compose([subplot_spacing, global_axis])
    return tweek(params)
