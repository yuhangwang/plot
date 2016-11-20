"""
Read a file or just convert an alternative list to numpy array
"""
from typing import AnyStr, List
from numpy import ndarray
from .readDataFile import readDataFile
import numpy


def readFileOrList(file_name, data_list, skip_rows=0):
    # type: (AnyStr, List) -> ndarray
    """Read a file or just convert an alternative list to numpy array

    If both file_name and data_list are given
    then the content of the data file will be returned.

    Args:
        file_name (str): input file name
        data_list (list): a list of numbers

    Returns:
        a numpy ndarray
    """
    if file_name is not None:
        return readDataFile(file_name, skip_rows)
    elif data_list is not None:
        return numpy.array(data_list)
    else:
        return None
