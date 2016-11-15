"""
Alter the tick labels
"""
from typing import AnyStr, List, Any


def alter_tick_labels(
        obj_axis,             # type: object
        which_axis,           # type: AnyStr
        major_minor,          # type: AnyStr
        new_tick_labels       # type: List[AnyStr]
        ):
    # type: (...) -> Tuple[bool, AnyStr]
    """ Alter the tick labels

    Args:
        obj_axis (object): matplotlib axis object
        which_axis (str):"x" or "y"
        major_minor (str): "major" or "minor"
        new_tick_labels (list): a list of new tick labels

    Returns:
        (True, "") if succeeded
        (False, "error message") if not
    """
    if new_tick_labels is None:
        return

    if major_minor == "minor":
        isMinor = True
    else:
        isMinor = False

    if which_axis == 'x':
        obj_axis.get_xaxis().set_ticklabels(new_tick_labels, minor=isMinor)
    elif which_axis == 'y':
        obj_axis.get_yaxis().set_ticklabels(new_tick_labels, minor=isMinor)
    else:
        msg = "ERROR HINT: you must specify either 'x' or 'y' axis;\n"
        msg += " Your input: {0}".format(which_axis)
        return (False, msg)

    return (True, "")
