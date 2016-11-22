"""
Draw a horizontal span
"""
from typing import Dict
import matplotlib.pyplot


def draw_horizontal_span(p):
    # type: (Dict) -> object
    """Draw a horizontal span

    Args:
        p (dict): parameters

    Returns:
        a matplotlib.patches.Polygon object
    """
    return matplotlib.pyplot.axhspan(
        p['min'], p['max'],
        xmin=p['left'],
        xmax=p['right'],
        alpha=p['opacity'],
        facecolor=p['color']['face'],
        edgecolor=p['color']['edge'],
        linesytle=p['line']['style'],
        linewdith=p['line']['width'],
        fill=p['filled'],
        zorder=p['which_layer']
        )
