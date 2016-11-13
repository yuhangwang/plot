"""
Convert a user configuration dictionary to
an internal parameter dictionary.
"""
from typing import Dict
import copy


def convert_to_internal(user_dict):
    # type: (Dict) -> Dict
    """Convert to "plot" internal dictionary.

    use the internal key defined by user_dict["__"]
    as the new key.

    Args:
        user_dict (dict): user configuration dictionary

    Returns:
        A new dictionary with new keys.
    """
    ooo = dict()
    for k in user_dict:
        if isinstance(user_dict[k], dict):
            new_key = user_dict[k]["__"]
            ooo[new_key] = convert_to_internal(user_dict[k])
        elif k == "v":
            return {"v": user_dict["v"]}
        else:
            continue
    return ooo
