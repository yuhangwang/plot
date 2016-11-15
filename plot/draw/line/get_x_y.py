"""
Return two arrays based on input data and input parameters
"""
from numpy import ndarray
from typing import Dict


def get_x_y(data, params):
    # type: (ndarray, Dict) -> (ndarray, ndarray)
    """Return two arrays based on input data and input parameters

    Args:
        data (ndarray): input data
        params (dict): one entry of the 'data' parameter field

    Returns:
        (X, Y) where X and Y are 1-dimensional numpy arrays
    """
    row_begin = params['line']['first_row']
    X = data[row_begin:, params['line']['data_column']['x']]
    Y = data[row_begin:, params['line']['data_column']['y']]
    return (X, Y)
