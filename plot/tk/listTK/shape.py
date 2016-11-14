"""
Return the shape of the input list
"""
from typing import List


def shape(a):
    # type: (List) -> List
    """Return the shape of the input list

    Args:
        a (list): input list

    Returns:
        a list containing the number elements 
        along each dimension
    """
    def aux(a, accum):
        # type: (List, List) -> List
        if isinstance(a, list):
            return aux(a[0], accum + [len(a)])
        else:
            return accum
    return aux(a, [])
