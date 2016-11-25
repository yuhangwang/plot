"""
Set the color for each line data entry.
"""
from typing import Dict
import copy
from .choose_color import choose_color


def set_line_color(params):
    # type: (Dict) -> Dict
    """Set the ID of reach line data entry

    Set the color for each line data entry.

    Args:
        params (dict): internal plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    # counter for each line to be plotted
    # within each panel
    counter = dict()
    fields = ['line']

    def aux(i, panel_id):
        if (panel_id in params['local'] and
                params['local'][panel_id]['colors'] is not None):
            return choose_color(i, params['local'][panel_id]['colors'])
        else:
            return choose_color(i, params['global']['colors'])

    for p in params['data']:
        for field in fields:
            if p[field]['color'] is None:
                p[field]['color'] = aux(p['local_id'], p['which_panel'])
            elif type(p[field]['color']) == int:
                # this allows the user to specify which default color to use
                p[field]['color'] = aux(p[field]['color'], p['which_panel'])
            else:
                pass  # keep user's color choice

    return params
