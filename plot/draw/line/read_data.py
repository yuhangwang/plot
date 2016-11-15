"""
Read input data based on user inputs
"""
from typing import Dict
from ...io.input import readDataFile
from numpy import ndarray


def read_data(params):
    # type: (Dict) -> ndarray
    """Read input data based on user inputs

    Args:
        params (dict): one entry of the data field

    Returns:
        data array (numpy.ndarray object)
    """
    if p['values'] is not None:
        return numpy.array(p['values'])
    elif p['file'] is not None:
        return readDataFile(p['file'])
    else:
        return None
