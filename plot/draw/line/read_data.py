"""
Read input data based on user inputs
"""
from typing import Dict
from ...io.input import readDataFile
from numpy import ndarray


def read_data(p):
    # type: (Dict) -> ndarray
    """Read input data based on user inputs

    Args:
        p (dict): one entry of the ['data'] field from the
            parameter dictionary

    Returns:
        data array (numpy.ndarray object)
    """
    if p['values'] is not None:
        return numpy.array(p['values'])
    elif p['file'] is not None:
        return readDataFile(p['file'], p['skip_rows'])
    else:
        return None
