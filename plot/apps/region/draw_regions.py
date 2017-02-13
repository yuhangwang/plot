"""
Draw regions
"""
from typing import List, Dict
from ...io.input.extract_data import extract_data
from ...io.input.extract_data_error_bar import extract_data_error_bar
from .draw_one_line import draw_one_line
from ...io.input.readFileOrList import readFileOrList
from .._tk import append_addon
import numpy


def draw_regions(params):
    # type: (Dict) -> Dict
    """Draw regions

    Args:
        params (dict): a complete parameter dictionary

    Returns:
        same as input
    """
    accum = []
    axes = params['internal']['canvas']['axes']
    for i in params['internal']['user']['plots']['line']:
        p = params['data'][i]
        data = readFileOrList(p['file'], p['values'], p['skip_rows'])
        if data is None:
            continue
        else:
            XY = extract_data(data, p)
            x_bars, y_bars = extract_data_error_bar(data, p)
            panel_id = p['which_panel']
            obj_axis = axes[panel_id]

            obj_line, legend_label = draw_one_line(
                obj_axis, XY, x_bars, y_bars, p)
            if p['legend']['content'] is not None:
                legend_panel = p['legend']['which_panel']
                append_addon(
                    'legend',
                    obj_line, legend_label, legend_panel, params)
            else:
                pass

    return params
