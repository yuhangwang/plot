"""
Read a data file and return the content as array.
"""
from typing import AnyStr
import numpy
from numpy import ndarray


def readDataFile(file_name):
    # type: (AnyStr) -> ndarray
    """Read a data file

    Read a data file and return its content as ndarray.

    Args:
        file_name (str): file name

    Returns:
        a numpy.ndarray object
    """
    return numpy.loadtxt(file_name)
