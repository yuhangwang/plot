"""
import all sub-modules residing in a directory
"""
from typing import List
import re
import os
import importlib


def subimport(path, parent_module):
    # type: (AnyStr, AnyStr) -> List
    """Import all sub-modules

    Import all sub-modules inside a directory

    Args:
        path (str): path to the target directory
        parent_module (str): absolute module name for that path

    Returns:
        a list of modules
    """
    apps = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if re.match("^[a-zA-Z]+.*$", d):
                m = importlib.import_module(
                    ".{}".format(d),
                    package=parent_module)
                apps.append(m)
    return apps
