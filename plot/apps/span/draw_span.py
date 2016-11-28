
"""
Draw span regions
"""
from typing import List, Dict
from .draw_horizontal_span import draw_horizontal_span
from .draw_vertical_span import draw_vertical_span
from .._tk import append_addon
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
    fn = {"horizontal": draw_horizontal_span, "vertical": draw_vertical_span}
    for i in params['internal']['user']['plots']['span']:
        p = params['data'][i]
        panel_id = p['which_panel']
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['horizontal', 'vertical']:
            if (p['span'][k]['min'] is None) or (p['span'][k]['max'] is None):
                continue
            else:
                obj_span = fn[k](obj_axis, p['span'][k], p['span'])
                legend_label = format_legend_label(p['legend']['content'])
                legend_panel = p['legend']['which_panel']
        # I intentionally only want to keep the legend
        # for the last horizontal/vertical plot
        if p['legend']['content'] is not None:
            append_addon(
                'legend', obj_span, legend_label, legend_panel, params)
        else:
            pass

    return params
