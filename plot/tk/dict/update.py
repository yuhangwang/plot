"""
Update the second dictionary with
the contents of the first dictionary.
"""
from typing import Dict
import copy


def update(src_dict, target_dict):
    # type: (Dict, Dict) -> Dict
    """Recursively update.

    Update the target_dict using
    content from the src_dict.
    Items from src_dict which are not in
    target_dict will be discarded.
    A easy way to remember the priority
    is "1st argument has #1 priority".

    Args:
        src_dict (dict): new information source
        target_dict (dict): target dictionary to be updated

    Returns:
        a new dictionary with updated entries.
    """
    ooo = copy.deepcopy(target_dict)
    for k in src_dict:
        if k in target_dict:  # update
            if (isinstance(target_dict[k], dict) and
                    isinstance(src_dict[k], dict)):
                ooo[k] = update(src_dict[k], target_dict[k])
            else:
                ooo[k] = src_dict[k]
        else:   # irrelevant items from src_dict
            continue
    return ooo
