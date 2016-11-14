"""
Create a canvas
"""
from typing import Dict
import copy
from .create_subplots import create_subplots


def create(params):
    # type: (Dict) -> Dict
    """Create a canvas

    Create a canvas and
    add "canvas" field in the
    returned dictionary.

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        a dictionary the same as the input except
        for an added new field 'canvas' which
        contains canvas objects.
    """
    params['canvas'] = {}  # add a new field
    return create_subplots(params)
