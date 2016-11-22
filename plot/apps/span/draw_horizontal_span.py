"""
Draw a horizontal span
"""
from typing import Dict


def draw_horizontal_span(obj_axis, p):
    # type: (object, Dict) -> object
    """Draw a horizontal span

    Args:
        obj_axis (object): a matplotlib axis object
        p (dict): parameters

    Returns:
        a matplotlib.patches.Polygon object
    """
    return obj_axis.axhspan(
        p['min'], p['max'],
        xmin=p['left'],
        xmax=p['right'],
        alpha=p['opacity'],
        facecolor=p['color']['face'],
        edgecolor=p['color']['edge'],
        linestyle=p['line']['style'],
        linewidth=p['line']['width'],
        fill=p['filled'],
        zorder=p['which_layer']
        )
