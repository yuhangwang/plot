"""
Draw all data
"""
from typing import Dict
from ..tk.fnTK import compose
from ..tk.importTK import subimport
import os


def draw(params):
    # type: (Dict) -> Dict
    """Draw all data

    Args:
        params (dict): parameter dictionary

    Returns:
        the same parameter dictionary
    """
    here = os.path.dirname(os.path.realpath(__file__))
    modules = subimport(here, "plot.apps")
    apps = [m.main for m in modules]
    aux = compose(apps)
    return aux(params)
