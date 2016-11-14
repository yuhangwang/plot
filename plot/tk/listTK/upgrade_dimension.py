"""
Upgrade from a low-dimensional list to a high-dimensional list
"""
from typing import List, Any
from .shape import shape


def upgrade_dimension(a, new_dim):
    # type: (List, int) -> List
    """Return a higher dimensional list

    Args:
        a (list): input list
        new_dim (int): new number of dimension

    Returns:
        a new list with dimension: new_dim
    """
    a_shape = shape(a)
    if new_dim < len(a_shape):
        return a
