"""
Append a new legend
"""


def append_legend(handle, label, pid, params):
    # type: (object, AnyStr, Dict) -> Dict
    """Append a new legend

    Args:
        handle (obj): a matplotlib object
            e.g. matplotlib.line.Line2D
        label (str): legend label
        pid (tuple): legend panel index
        params (dict): plotting parameters
    Returns:
        updated parameters
    """
    p_legend = params['internal']['panel']['legend']
    if pid is not None:
        p_legend[pid].append([handle, label])
    else:
        pass
