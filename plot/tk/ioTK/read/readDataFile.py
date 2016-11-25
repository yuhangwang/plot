"""
Read one data file
"""
import os
import numpy
from .readTextData import readTextData
from .readNpy import readNpy
from .readMdat import readMdat


def readDataFile(input, dtype="float"):
    """Read one data file

    Return a numpy array

    Args:
        inputs (str): file name
        dtype (str): input data type
            default: "float"

    Returns:
        an ndarray
    """
    _, ext = os.path.splitext(f)
    if ext == ".npy":
        return readNpy(f)
    elif ext == ".mdat":
        return readMdat(f)
    else:
        return readTextData(f, dtype)
