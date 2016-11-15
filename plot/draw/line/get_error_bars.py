"""
Return two arrays representing the error bars
"""
from numpy import ndarray
from typing import Dict


def get_error_bars(data, params):
    # type: (ndarray, Dict) -> (ndarray, ndarray)
    """Return error bar arrays

    Return error bar arrays along X and Y

    Args:
        data (ndarray): input data
        params (dict): one entry of the 'data' parameter field

    Returns:
        (x_bars, y_bars) where x_bars and y_bars are 1-dimensional numpy arrays
    """
    row_begin = params['line']['first_row']
    x_bars = data[row_begin:, params['error_bar']['data_column']['x']]
    y_bars = data[row_begin:, params['error_bar']['data_column']['y']]
    return (x_bars, y_bars)
