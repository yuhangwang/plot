"""
Draw bars
"""
from typing import List, Dict
from .extract_data_x_y import extract_data_x_y
from ...io.input.readFileOrList import readFileOrList
import numpy


def draw_bars(params):
    # type: (Dict) -> Dict
    """Draw lines

    Draw histogram-like bars with error bars if defined.

    Args:
        params (dict): a complete parameter dictionary

    Returns:
        same as input
    """
    accum = []
    for i in params['internal']['user']['plots']['bar']:
        p = params['data'][i]
        data = readFileOrList(p['file'], p['values'], p['skip_rows'])
        if data is None:
            continue
        else:
            XY = extract_data_x_y(data, p)
            x_bars, y_bars = extract_data_error_bar(data, p)
            panel_id = p['which_panel']
            obj_axis = params['internal']['canvas']['axes'][panel_id]
            draw_one_bar_series(
                obj_axis, XY, x_bars, y_bars, 
                p['bar'], p['error_bar'])

    return params
