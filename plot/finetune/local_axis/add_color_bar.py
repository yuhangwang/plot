"""
Add color bar
"""
from ...tk import matplotlibTK as mtk
from typing import Dict


def add_color_bar(obj_axis, obj_mat, p):
    # type: (object, object, Dict) -> object
    """ Add color bar
    
    Args:
        obj_axis (object): axis object
        obj_mat (object): matrix object
        p (dict): parameters for the matrix plot
    
    Returns:
        a `matplotlib.colorbar.Colorbar` object
    """
    object_color_bar = mtk.add_color_bar(
        obj_axis,
        obj_mat,
        bar_tick_label_font_size=p["color_bar_tick_label_font_size"],
        bar_tick_label_decimals=p["color_bar_tick_label_number_of_decimal_places"],
        bar_ticks = p["color_bar_tick_array"],
        bar_tick_width = p["color_bar_tick_width"],
        bar_tick_length = p["color_bar_tick_length"],
        bar_tick_color = p["color_bar_tick_color"],
        )

    return object_color_bar