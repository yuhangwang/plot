"""
Create, draw and save figures based
on user input parameter dictionary.
"""
from typing import Dict
import matplotlib
from .matplotlibConfig import rcParams as new_rcParams


def run(params, preview):
    # type: (Dict, bool) -> bool
    """Create, draw, and save figures

    Args:
        params (dict): a dictionary that defines the figure
        preview (bool): whether to show the preview of the figure

    Returns:
        True if succeeded
    """
    matplotlib.rcParams.update(new_rcParams)

    return True
