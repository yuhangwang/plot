"""
Add color bar
"""
from ...tk.matplotlibTK import color_bar
from typing import Dict
from .make_color_bar_axis import make_color_bar_axis


def add_color_bar(params):
    # type: (Dict) -> Dict
    """Refine legend properties

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id in params['internal']['panel']['color_bar']:
        if panel_id in params['local']:
            p = params['local'][panel_id]['color_bar']
        else:
            p = params['internal']['default']['local']['color_bar']
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for handles_labels in params['internal']['panel']['color_bar'][panel_id]:
            handle, label = handles_labels
            obj_color_bar = color_bar.add_color_bar(
                make_color_bar_axis(obj_axis, p),
                handle,
                bar_label=label,
                bar_tick_label_font_size=p['tick_label']['font']['size'],
                bar_tick_label_decimals=p['tick_label']['decimals'],
                bar_tick_label_color=p['tick_label']['color'],
                bar_ticks=p['tick']['set'],
                bar_tick_width=p['tick']['width'],
                bar_tick_length=p['tick']['length'],
                bar_tick_color=p['tick']['color'],
                box_color=p['box']['color'],
                padding=p['padding']['label_and_tick']
                )

    return params
