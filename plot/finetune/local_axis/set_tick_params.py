"""
Set tick parameters
"""
from typing import Dict


def set_tick_params(params):
    # type: (Dict) -> Dict
    """Set the tick parameters

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    for panel_id, p in params['local'].items():
        obj_axis = params['internal']['canvas']['axes'][panel_id]
        for k in ['x', 'y']:
            for m in ['major', 'minor']:
                obj_axis.tick_params(
                    axis=k,
                    which=m,
                    labelsize=p['tick_label'][m]['font']['size'][k],
                    width=p['tick'][m]['width'][k])

    return params
