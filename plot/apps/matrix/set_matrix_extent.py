"""
Set matrix extent (min/max along x/y)
"""
from typing import Dict
import matplotlib.pyplot as pyplot


def set_matrix_extent(obj_mat, p):
    # type: (object, Dict) -> object
    """Draw a matrix

    Args:
        obj_mat (object): a matplotlib.image.AxesImage object
        p (dict): a properties of the matrix plot

    Returns:
        same as inputs
    """
    offsets = [
        p['matrix']['extent']['offset']['x'],
        p['matrix']['extent']['offset']['y']]

    # get old extent
    extent = list(pyplot.getp(obj_mat, "extent"))
    # update extent
    for i, a in enumerate(['x', 'y']):
        for j, m in enumerate(['min', 'max']):
            h = p['matrix']['extent'][m][a]
            if h is not None:
                extent[i*2 + j] = h + offsets[i]
    pyplot.setp(obj_mat, extent=extent)
    return
