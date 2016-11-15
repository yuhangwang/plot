"""
Return two arrays based on input data and input parameters
"""
from numpy import ndarray
from typing import Dict


def extract_data_x_y(data, params):
    # type: (ndarray, Dict) -> (ndarray, ndarray)
    """Return two arrays based on input data and input parameters

    Args:
        data (ndarray): input data
        params (dict): one entry of the 'data' parameter field

    Returns:
        (X, Y) where X and Y are 1-dimensional numpy arrays
    """
    row_begin = params['line']['row_start']
    ooo = []
    for k in ['x', 'y']:
        j = params['line']['data_column'][k]
        if j is None:
            ooo.append(None)
        else:
            ooo.append(data[row_begin:, j])
    return tuple(ooo)
