"""
Postprocess the internal parameter dictionary
"""
from typing import Dict
from ....tk.fnTK import compose
from .make_local_dict import make_local_dict
from .set_data_id import set_data_id
from .set_line_color import set_line_color
from .set_shape_color import set_shape_color
from .assort_plots_by_type import assort_plots_by_type
from .set_data_columns import set_data_columns
from .set_panel_minmax import set_panel_minmax
from .initialize_panel_legend import initialize_panel_legend


def postprocess(params):
    # type: (Dict) -> Dict
    """Postprocess the internal parameter dictionary

    Args:
        params(dict): internal parameter dictionary

    Returns:
        enhanced internal parameter dictionary
    """
    aux = compose([
        make_local_dict,
        set_data_id,
        set_line_color,
        set_shape_color,
        assort_plots_by_type,
        set_data_columns,
        set_panel_minmax,
        initialize_panel_legend
        ])
    return aux(params)
