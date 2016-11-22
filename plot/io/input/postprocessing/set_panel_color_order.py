"""
Add a new field 'panel_colors' under 'global' which collects
the panel colors specified by the user.
Only those panels specified by the user will be collected.
"""
from typing import Dict


def set_panel_color_order(params):
    # type: (Dict) -> Dict
    """Add a new 'panel_colors' under 'global'.

    Add a new field 'panel_colors' under 'global' which collects
    the panel colors specified by the user.
    Only those panels specified by the user will be collected.

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    params['global']['panel_colors'] = {}
    for panel_id, p in params['local'].items():
        params['global']['panel_colors'][panel_id] = p['colors']
    return params
