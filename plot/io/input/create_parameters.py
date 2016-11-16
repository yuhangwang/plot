"""
Create a dictionary of parameters
"""
from typing import Dict
from ... import tk
from .format_panel_index import format_panel_index
from ...tk.fnTK import compose


def create_parameters(user_dict, default_dict):
    # type: (Dict, Dict) -> Dict
    """Create a new parameter dictionary

    Create a new parameter dictionary based on
    user inputs and defaults.

    Args:
        user_dict (dict): user input parameters
        default_dict (dict): default parameters

    Returns:
        an internal parameter dictionary
    """
    p = tk.dictTK.convert_to_internal(
            tk.dictTK.update(
                    tk.dictTK.wrap_value(user_dict),
                    default_dict
            )
        )
    aux = compose([
        format_panel_index,
        ])
    return aux(p)
