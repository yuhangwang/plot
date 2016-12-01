"""
Draw matrices
"""
from typing import List, Dict
from .draw_matrix import draw_matrix
from ...io.input.readFileOrList import readFileOrList
import numpy
from .._tk import append_addon


def draw_matrices(params):
    # type: (Dict) -> Dict
    """Draw matrices

    Draw matrices

    Args:
        params (dict): a complete parameter dictionary

    Returns:
        same as input
    """
    axes = params['internal']['canvas']['axes']
    for i in params['internal']['user']['plots']['matrix']:
        p = params['data'][i]
        data = readFileOrList(
            p['file'], p['values'], p['skip_rows'],
            transpose=p['matrix']['transpose'])
        if data is None:
            continue
        else:
            panel_id = p['which_panel']
            obj_axis = axes[panel_id]
            obj_matrix = draw_matrix(obj_axis, data, p)
            if p['color_bar']['show']:
                color_bar_panel = p['color_bar']['which_panel']
                label = p['color_bar']['content']
                append_addon(
                    'color_bar',
                    obj_matrix, label, color_bar_panel, params)
            else:
                pass

    return params
