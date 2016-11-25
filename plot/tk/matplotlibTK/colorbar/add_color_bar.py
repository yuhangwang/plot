"""
Add a color bar
"""
from typing import List
import matplotlib.ticker 
import matplotlib.pyplot
import mpl_toolkits.axes_grid1 as MplTkAxes


def add_color_bar(
        obj_axis,                                        # type: object
        obj_matshow,                                     # type: object
        bar_tick_label_font_size=20,                     # type: int
        bar_tick_label_decimals=None,                    # type: int
        bar_ticks=None,                                  # type: List
        bar_tick_width=2,                                # type: int
        bar_tick_length=7,                               # type: int
        bar_tick_color="k"                               # type: str
        ):
    # type: (...) -> object
    """Add color bar to an axis object 

    Args:
        obj_axis (object): matplotlib axis object where the color bar will be plotted
        obj_matshow (object): a `matplotlib.image.AxesImage` object
        bar_tick_label_font_size (int): color bar tick label font size 
        bar_tick_label_decimals (int): number of decimal places to show 
            (default: None, i.e. use matplotlib default)
        bar_ticks (list): a list/tuple of tick locations, e.g. (0, 0.5, 1.0) 
            (default: None, i.e. use matplotlib default)
        bar_tick_width (int): width of the color bar ticks
        bar_tick_length (int): length of the color bar ticks
        bar_tick_color (str): color of the color bar ticks

    Returns:
        a `matplotlib.colorbar.Colorbar` object
    """
    # change tick number of decimal places
    # stackoverflow.com/questions/25983218/scientific-notation-colorbar-in-matplotlib
    def tick_formatter(tick_value, tick_position):
            return "{0:.{1}f}".format(tick_value, bar_tick_label_decimals)

    if bar_tick_label_decimals is not None:
        obj_color_bar = matplotlib.pyplot.colorbar(obj_matshow, 
            cax=obj_axis,
            ticks=bar_ticks,
            format=matplotlib.ticker.FuncFormatter(tick_formatter))
    else:
        obj_color_bar = matplotlib.pyplot.colorbar(obj_matshow, 
            ticks=bar_ticks,
            cax=obj_axis)

    # change tick label font size
    for tick in obj_color_bar.ax.get_yticklabels():
        tick.set_fontsize(bar_tick_label_font_size)

    # change tick thickness and length
    obj_axis.yaxis.set_tick_params(which="major", 
        width=bar_tick_width, 
        length=bar_tick_length, 
        color=bar_tick_color)

    return obj_color_bar
