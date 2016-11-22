"""
Draw lines (with error bars if defined)
"""
from typing import List, Dict
from ...io.input.extract_data_x_y import extract_data_x_y
from ...io.input.extract_data_error_bar import extract_data_error_bar
from .draw_one_line import draw_one_line
from ...io.input.readFileOrList import readFileOrList
import numpy


def draw_lines(params):
    # type: (Dict) -> Dict
    """Draw lines

    Draw lines, with error bars if defined.

    Args:
        params (dict): a complete parameter dictionary

    Returns:
        same as input
    """
    accum = []
    axes = params['internal']['canvas']['axes']
    panel_legends = params['internal']['panel']['legend']
    for i in params['internal']['user']['plots']['line']:
        p = params['data'][i]
        data = readFileOrList(p['file'], p['values'], p['skip_rows'])
        if data is None:
            continue
        else:
            XY = extract_data_x_y(data, p)
            x_bars, y_bars = extract_data_error_bar(data, p)
            panel_id = p['which_panel']
            obj_axis = axes[panel_id]

            obj_line, legend_label = draw_one_line(
                obj_axis, XY, x_bars, y_bars, p)

            legend_panel_id = p['legend']['which_panel']
            if legend_panel_id is not None:
                panel_legends[legend_panel_id].append(
                    [obj_line, legend_label])
            else:
                pass

    return params
