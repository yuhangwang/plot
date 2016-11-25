"""
Read a data file and return the content as array.
"""
from typing import AnyStr
import numpy
from numpy import ndarray
from ..tk.ioTK import read as R


def readDataFile(file_name, dtype="float" skip_rows=0):
    # type: (AnyStr) -> ndarray
    """Read a data file

    Read a data file and return its content as ndarray.

    Args:
        file_name (str): file name
        dtype (str): input data type
            (only relevant if input is text)
        skip_rows (int): number of rows to skip
            (only for text data file)

    Returns:
        a numpy.ndarray object
    """
    data = R.readDataFile(
        file_name,
        dtype=dtype,
        skiprows=skip_rows)
    
    if len(numpy.shape(data)) == 0:
        return numpy.array([])
    elif len(numpy.shape(data)) == 1:
        return data[:, numpy.newaxis]
    else:
        return data
