"""
Set the color for each marker entry.
"""
from typing import Dict
import copy
from .choose_color import choose_color


def set_marker_color(params):
    # type: (Dict) -> Dict
    """Set the ID of reach marker data entry

    Args:
        params (dict): internal plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    # counter for each data series to be plotted
    # within each panel
    counter = dict()
    fields = ['scatter']

    def aux(i, panel_id):
        if (panel_id in params['local'] and
                params['local'][panel_id]['colors'] is not None):
            return choose_color(i, params['local'][panel_id]['colors'])
        else:
            return choose_color(i, params['global']['colors'])

    for p in params['data']:
        for field in fields:
            if p[field]['marker']['color'] is None:
                p[field]['marker']['color'] = aux(
                    p['local_id'], p['which_panel'])
            elif type(p[field]['marker']['color']) == int:
                # this allows the user to specify which default color to use
                p[field]['marker']['color'] = aux(
                    p[field]['marker']['color'], p['which_panel'])
            else:
                pass  # keep user's color choice

    return params
