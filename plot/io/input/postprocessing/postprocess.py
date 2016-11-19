"""
Postprocess the internal parameter dictionary
"""
from typing import Dict
from ....tk.fnTK import compose
from .set_data_id import set_data_id
from .set_panel_color_order import set_panel_color_order
from .set_data_color import set_data_color
from .assort_plots_by_type import assort_plots_by_type


def postprocess(params):
    # type: (Dict) -> Dict
    """Postprocess the internal parameter dictionary

    Args:
        params(dict): internal parameter dictionary

    Returns:
        enhanced internal parameter dictionary
    """
    aux = compose([
        set_data_id,
        set_panel_color_order,
        set_data_color,
        assort_plots_by_type,
        ])
    return aux(params)
