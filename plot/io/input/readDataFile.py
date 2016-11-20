"""
Read a data file and return the content as array.
"""
from typing import AnyStr
import numpy
from numpy import ndarray


def readDataFile(file_name, skip_rows=0):
    # type: (AnyStr) -> ndarray
    """Read a data file

    Read a data file and return its content as ndarray.

    Args:
        file_name (str): file name

    Returns:
        a numpy.ndarray object
    """
    data = numpy.loadtxt(file_name, skiprows=skip_rows)
    if len(numpy.shape(data)) == 0:
        return numpy.array([])
    elif len(numpy.shape(data)) == 1:
        return data[:, numpy.newaxis]
    else:
        return data
