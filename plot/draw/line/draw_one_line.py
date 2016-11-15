"""
Draw a single line
"""
from typing import Dict, Tuple
from numpy import ndarray


def draw_one_line(
        obj_axis,         # type: object
        x,                # type: ndarray
        y,                # type: ndarray
        x_bars,           # type: ndarray
        y_bars,           # type: ndarray
        line_styles,      # type: Dict
        marker_styles,    # type: Dict
        error_bar_styles  # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a single line

    Draw a single line with error bars if specified.

    Args:
        obj_axis (object): matplotlib.axis.Axis object
        x (ndarray): data to be used as x
        y (ndarray): data to be used as y
        x_bars (ndarray): data to be used as x error bars
        y_bars (ndarray): data to be used as y error bars
        line_styles (dict): a dictionary of line styles
        marker_styles (dict): a dictionary of marker styles
        error_bar_styles (dict): a dictionary of error bar styles

    Returns:
        a tuple (obj_line, obj_error_bar_caps, obj_error_bar_lines)
    """
    line, error_bar_caps, error_bar_lines = obj_axis.errorbar(
            x, y,
            xerr=x_bars, yerr=y_bars,
            axes=obj_axis
        )

    return {
            "line": line,
            "error_bar": {
                    "caps": error_bar_caps,
                    "lines": error_bar_lines
                }
        }
