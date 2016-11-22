"""
Add new legend handles/labels to an axis
"""
from typing import Dict
import matplotlib.pyplot


def add_legend(obj_axis, legend_handles, legend_labels):
    # type: (object, Dict) -> obj_axis
    """Add new legend handles/labels to an axis

    Args:
        obj_axis (object): a matplotlib axis object
        legend_handles (list): list of legend handle objects
            e.g. a matplotlib.lines.Line2D object
        legend_labels (list): list of legend labels (strings)

    Returns:
        the input axis object
    """
    handles, labels = obj_axis.get_legend_handles_labels()
    obj_axis.legend(handles + legend_handles, labels + legend_labels)
    return obj_axis
