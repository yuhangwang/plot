"""
Draw bars
"""
from typing import List, Dict
from ...io.input.extract_data import extract_data
from ...io.input.extract_data_error_bar import extract_data_error_bar
from ...io.input.readFileOrList import readFileOrList
from .draw_one_bar_series import draw_one_bar_series
from .._tk import append_addon
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
            XY = extract_data(data, p)
            x_bars, y_bars = extract_data_error_bar(data, p)
            panel_id = p['which_panel']
            obj_axis = params['internal']['canvas']['axes'][panel_id]
            obj_bar, legend_label = draw_one_bar_series(
                obj_axis, XY, x_bars, y_bars, p)
            if p['legend']['content'] is not None:
                legend_panel = p['legend']['which_panel']
                append_addon(
                    'legend', obj_bar, legend_label, legend_panel, params)
            else:
                pass
    return params
