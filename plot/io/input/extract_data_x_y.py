"""
Return two arrays based on input data and input parameters
"""
from numpy import ndarray
from typing import Dict
from ...tk.arrayTK import smooth


def extract_data_x_y(data, params):
    # type: (ndarray, Dict) -> (ndarray, ndarray)
    """Return two arrays based on input data and input parameters

    Args:
        data (ndarray): input data
        params (dict): one entry of the 'data' parameter field

    Returns:
        (X, Y) where X and Y are 1-dimensional numpy arrays
        or (Y) if only params[plot_type]['data_column']['y'] is specified
    """
    plot_type = params['plot_type']
    row_start = params[plot_type]['row_start']
    ooo = []
    for k in ['x', 'y']:
        j = params[plot_type]['data_column'][k]
        if j is None:
            continue
        else:
            ooo.append(data[row_start:, j])

    if params['smooth']['window_size'] is not None:
        ooo[-1] = smooth(ooo[-1], params['smooth'])

    return tuple(ooo)
