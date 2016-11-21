"""
Draw a single series of bars
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray


def draw_one_bar_series(
        obj_axis,         # type: object
        xy,               # type: List
        x_bars,           # type: ndarray
        y_bars,           # type: ndarray
        line_params       # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a single line

    Draw a single line with error bars if specified.

    Args:
        obj_axis (object): matplotlib.axis.Axis object
        xy (list): a list containing either 1 or 2 data arrays
        x_bars (ndarray): data to be used as x error bars
        y_bars (ndarray): data to be used as y error bars
        line_params (dict): line parameters

    Returns:
        a matplotlib.lines.line2D object
    """
    p = line_params
    line, error_bar_caps, error_bar_lines = obj_axis.errorbar(
            *xy, xerr=x_bars, yerr=y_bars, axes=obj_axis,
            color=p['line']['color'],
            linewidth=p['line']['width'],
            linestyle=p['line']['style'],
            alpha=p['line']['opacity'],
            ecolor=p['error_bar']['edge_color'],
            elinewidth=p['error_bar']['line_width'],
            capsize=p['error_bar']['cap']['size'],
            capthick=p['error_bar']['cap']['thickness'],
            errorevery=p['error_bar']['resample_window_size'],
            marker=p['marker']['style'],
            markersize=p['marker']['size']
     )

    if p['legend']['content'] is not None:
        line.set_label(p['legend']['content'])
    else:
        # legend labels staring with '_' are ignored
        #  see matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
        line.set_label("_")

    return line
