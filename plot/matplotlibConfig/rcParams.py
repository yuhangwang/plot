"""
A new set of rcParams for matplotlib
"""
from typing import Dict


def rcParams():
    # type: () -> Dict
    """Return a new set of rcParams"""

    return {
        "font.family": "sans-serif",
        "mathtext.fontset": "stixsans",
        "xtick.major.size": 5,
        "ytick.major.size": 5,
        "xtick.major.width": 2,
        "ytick.major.width": 2,
        "xtick.minor.size": 2,
        "ytick.minor.size": 2,
        "xtick.minor.width": 2,
        "ytick.minor.width": 2,
        "xtick.labelsize": 25,
        "ytick.labelsize": 25,
    }
