"""
Merge two dictionaries into one.
"""
from typing import Dict
import copy


def merge(dict1, dict2):
    # type: (Dict, Dict) -> Dict
    """Recrusively merge two dictionaries.

    The two input dictionaries can have arbitrary depths.

    Args:
        dict1 (dict): input dictionary 1
        dict2 (dict): input dictionary 2

    Returns:
        A new dictionary that combines both inputs.

    """
    ooo = copy.deepcopy(dict1)
    for k in dict2:
        if (k in dict1 and  # resolve conflicts
                isinstance(dict1[k], dict) and
                isinstance(dict2[k], dict)):
            ooo[k] = merge(dict1[k], dict2[k])
        else:
            ooo[k] = dict2[k]  # non-conflicting items
    return ooo
