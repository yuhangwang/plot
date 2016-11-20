"""
Draw a single line
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray


def draw_one_line(
        obj_axis,         # type: object
        xy,               # type: List
        x_bars,           # type: ndarray
        y_bars,           # type: ndarray
        legend_label,     # type: AnyStr
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
        legend_label (str): text content for the legend
        line_params (dict): line parameters

    Returns:
        a matplotlib.lines.line2D object
    """
    line, error_bar_caps, error_bar_lines = obj_axis.errorbar(
            *xy, xerr=x_bars, yerr=y_bars, axes=obj_axis,
            color=line_params['line']['color'],
            linewidth=line_params['line']['width'],
            linestyle=line_params['line']['style'],
            alpha=line_params['line']['opacity'],
            ecolor=line_params['error_bar']['edge_color'],
            elinewidth=line_params['error_bar']['line_width'],
            capsize=line_params['error_bar']['cap']['size'],
            capthick=line_params['error_bar']['cap']['thickness'],
            errorevery=line_params['error_bar']['resample_window_size'],
            marker=line_params['marker']['style'],
            markersize=line_params['marker']['size']
     )

    if legend_label is not None:
        line.set_label(legend_label)
    else:
        # legend labels staring with '_' are ignored
        #  see matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
        line.set_label("_")

    return line
