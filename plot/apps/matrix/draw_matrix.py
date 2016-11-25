"""
Draw a matrix
"""
from typing import Dict
from numpy import ndarray
from .set_aspect_ratio import set_aspect_ratio
from .set_matrix_extent import set_matrix_extent


def draw_matrix(
        obj_axis,         # type: object
        data,             # type: ndarray
        p                 # type: Dict
        ):
    # type: (...) -> object
    """Draw a matrix

    Args:
        obj_axis (object): a matplotlib axis object
        data (ndarray): a numpy ndarray object
        p (dict): a python dictionary

    Returns:
        a `matplotlib.image.AxesImage` object
    """
    obj = obj_axis.matshow(
        data,
        vmin=p['matrix']['vertical']['min'],
        vmax=p['matrix']['vertical']['max'])
    set_aspect_ratio(obj_axis)
    set_matrix_extent(obj, p)
    return obj
