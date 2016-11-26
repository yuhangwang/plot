"""
Add a color bar
"""
from typing import List, AnyStr
import matplotlib.ticker 
import matplotlib.pyplot
import mpl_toolkits.axes_grid1 as MplTkAxes
from .add_label import add_label
from .set_tick_label_font_size import set_tick_label_font_size


def add_color_bar(
        obj_axis,                                        # type: object
        obj_matshow,                                     # type: object
        bar_label=None,                                  # type: AnyStr
        bar_tick_label_font_size=20,                     # type: int
        bar_tick_label_decimals=None,                    # type: int
        bar_tick_label_color="k",                        # type: AnyStr
        bar_ticks=None,                                  # type: List
        bar_tick_width=2,                                # type: int
        bar_tick_length=7,                               # type: int
        bar_tick_color="k",                              # type: AnyStr
        box_color="k",                                   # type: AnyStr
        padding=5                                        # type: int
        ):
    # type: (...) -> object
    """Add color bar to an axis object 

    Args:
        obj_axis (object): matplotlib axis object where the color bar will be plotted
        obj_matshow (object): a ``matplotlib.image.AxesImage`` object
        bar_label=None (str): label for the color bar
        bar_tick_label_font_size (int): color bar tick label font size 
        bar_tick_label_decimals (int): number of decimal places to show 
            (default: None, i.e. use matplotlib default)
        bar_tick_label_color='k' (str): color for tick labels
        bar_ticks (list): a list/tuple of tick locations, e.g. (0, 0.5, 1.0) 
            (default: None, i.e. use matplotlib default)
        bar_tick_width (int): width of the color bar ticks
        bar_tick_length (int): length of the color bar ticks
        bar_tick_color (str): color of the color bar ticks
        box_color (str): color bar box color
        padding (int): padding between ticks and tick labels

    Returns:
        a ``matplotlib.colorbar.Colorbar`` object
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

    # add color bar label
    add_label(obj_color_bar, bar_label)
    
    # change tick label font size
    set_tick_label_font_size(obj_color_bar, bar_tick_label_font_size)

    # set tick label color
    obj_color_bar.ax.yaxis.set_tick_params(labelcolor=bar_tick_label_color)

    #set ticks color 
    obj_color_bar.ax.yaxis.set_tick_params(color=bar_tick_color)

    # set tick width
    obj_color_bar.ax.yaxis.set_tick_params(width=bar_tick_width)

    # set tick length
    obj_color_bar.ax.yaxis.set_tick_params(length=bar_tick_length)

    # set box color
    # obj_color_bar.outline.set_color(box_color)

    # set padding between ticks and tick labels
    obj_color_bar.ax.yaxis.set_tick_params(pad=padding)

    return obj_color_bar
