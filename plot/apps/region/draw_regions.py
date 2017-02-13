"""
Draw regions
"""
from typing import List, Dict
from ...io.input.extract_data import extract_data
from ...io.input.extract_data_error_bar import extract_data_error_bar
from .draw_one_region import draw_one_region
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
    for i in params['internal']['user']['plots']['region']:
        p = params['data'][i]
        data = readFileOrList(p['file'], p['values'], p['skip_rows'])
        if data is None:
            continue
        else:
            XY1Y2 = extract_data(data, p)
            panel_id = p['which_panel']
            obj_axis = axes[panel_id]

            obj_region, legend_label = draw_one_region(
                obj_axis, XY1Y2, p)

            if p['legend']['content'] is not None:
                legend_panel = p['legend']['which_panel']
                append_addon(
                    'legend',
                    obj_region, legend_label, legend_panel, params)
            else:
                pass

    return params
