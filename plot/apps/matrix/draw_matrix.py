"""
Draw a matrix
"""
from typing import Dict
from numpy import ndarray


def draw_matrix(
        obj_axis,         # type: object
        data,             # type: ndarray
        p                 # type: Dict
        ):
    # type: (...) -> Tuple
    """Draw a matrix

    Args:
        obj_axis (object): a matplotlib axis object
        data (ndarray): a numpy ndarray object
        p (dict): a python dictionary

    Returns:
        a `matplotlib.image.AxesImage` object
    """
    return obj_axis.matshow(
        data,
        vmin=p['matrix']['vertical']['min'],
        vmax=p['matrix']['vertical']['max'])
