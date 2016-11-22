"""
Draw a single line
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray
from ...tk.matplotlibTK.legend import format_legend_label


def draw_one_line(
        obj_axis,         # type: object
        obj_legend_axis,  # type: object
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
        obj_legend_axis (obj): axis object to place the legend
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
            ecolor=p['error_bar']['color']['edge'],
            elinewidth=p['error_bar']['line']['width'],
            capsize=p['error_bar']['cap']['size'],
            capthick=p['error_bar']['cap']['thickness'],
            errorevery=p['error_bar']['resample_window_size'],
            marker=p['marker']['style'],
            markersize=p['marker']['size']
     )

    return (line, format_legend_label(legend_label))
