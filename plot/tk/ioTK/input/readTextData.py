"""
Read data in text format
"""
from typing import AnyStr
from numpy import ndarray
import numpy


def readTextData(file_name, dtype_str):
    # type: (AnyStr, AnyStr) -> ndarray
    """Read data in text format and return an array

    Supported dtype: "int", "float"

    Args:
        file_name (str): input file name
        dtype_str (str): data type as string

    Returns:
        a numpy ndarray
    """
    return numpy.loadtxt(file_name, dtype=eval(dtype_str))
