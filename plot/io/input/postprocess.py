"""
Postprocess the internal parameter dictionary
"""
from typing import Dict
from .set_data_id import set_data_id
from ...tk.fnTK import compose


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
        ])
    return aux(params)
