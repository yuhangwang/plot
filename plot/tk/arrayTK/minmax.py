"""
Return the min/max of the input list of arrays
"""
from typing import List
import numpy

def minmax(xs):
    # type: (List) -> List
    """Return the min/max of the input list of arrays

    Example: minmax(X, Y) returns [[min(X), max(X)], [min(Y), max(Y)]]

    Args:
        xs (list): numerical array
    
    Returns:
        a list of min/max values

    """
    def tail(xs): return xs[1:]

    def aux(xs, accum):
        if len(xs) == 0:
            return accum
        else:
            return aux(
                tail(xs), 
                accum + [[numpy.amin(xs[0]), numpy.amax(xs[0])]])

    return aux(xs, [])
