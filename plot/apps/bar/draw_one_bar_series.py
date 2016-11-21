"""
Draw a single series of bars
"""
from typing import Dict, Tuple, List, AnyStr
from numpy import ndarray
from .draw_vertical_bars import draw_vertical_bars
from .draw_horizontal_bars import draw_horizontal_bars


def draw_one_bar_series(
        obj_axis,         # type: object
        xy,               # type: List
        x_error_bars,     # type: ndarray
        y_error_bars,     # type: ndarray
        p_bars            # type: Dict
        p_errors          # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a single line

    Draw a single line with error bars if specified.

    Args:
        obj_axis (object): matplotlib.axis.Axis object
        xy (list): a list containing either 1 or 2 data arrays
        x_error_bars (ndarray): data to be used as x error bars
        y_error_bars (ndarray): data to be used as y error bars
        p_bars (dict): bar parameters
        p_errors (dict): error bar parameters

    Returns:
        a matplotlib.container.BarContainer object
    """
    p = p_bars
    if p['orientation'] == 'vertical':
        draw_vertical_bars(
            *xy, x_error_bars, p_bars, p_errors)
    else:
        bar = draw_horizontal_bars(
            *xy, y_error_bars, p_bars, p_errors)

    if p['legend']['content'] is not None:
        bar.set_label(p['legend']['content'])
    else:
        # legend labels staring with '_' are ignored
        #  see matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
        bar.set_label("_")

    return bar
