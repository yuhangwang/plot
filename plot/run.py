"""
Read the input and start working
"""
from typing import Dict, AnyStr
from .work import work
import os
from .io.input import parse


def run(user_config_file, preview):
    # type: (AnyStr, bool) -> bool
    """Read input and start working

    Args:
        user_config_file (str): file name of user configuration file
        preview (bool): whether to show the preview window

    Returns:
        True of succeeds
    """
    here = os.path.dirname(os.path.realpath(__file__))
    default_config_file = os.path.join(here, "parameter", "all.json")
    params = parse(user_config_file, default_config_file)

    if len(params.keys()) == 0:
        raise Exception(
            "ERROR HINT: invalid input "
            "configuration file {}".format(user_config_file)
            )
        exit()

    return work(params, preview)
