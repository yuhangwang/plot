"""
Draw span regions
"""
from typing import List, Dict
from .draw_horizontal_span import draw_horizontal_span
from .._tk import append_legend
from ...tk.matplotlibTK.legend import format_legend_label


def draw_span(params):
    # type: (Dict) -> Dict
    """Draw span regions

    Args:
        params (dict): a complete parameter dictionary

    Returns:
        same as input
    """
    accum = []
    fn = {"horizontal": draw_horizontal_span}
    for i in params['internal']['user']['plots']['span']:
        p = params['data'][i]
        panel_id = p['which_panel']
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['horizontal']:
            if (p['span'][k]['min'] is None) or (p['span'][k]['max'] is None):
                continue
            else:
                obj_span = fn[k](obj_axis, p['span'][k])
                legend_label = format_legend_label(p['legend']['content'])
                legend_panel = p['legend']['which_panel']
                append_legend(obj_span, legend_panel, legend_panel, params)

    return params
