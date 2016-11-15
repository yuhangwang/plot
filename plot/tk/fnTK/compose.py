"""
Take many functions and compose
"""
from typing import List, Callable, Optional
import functools


def compose(functions):
    # type: (List[Callable]) -> Callable
    """Compose functions

    Args:
        functions (list): a list of functions

    Returns:
        a new function with combined effects from all inputs
    """
    def aux(f1, f2):
        # type: (Callable, Callable) -> Callable
        return lambda x: f1(f2(x))

    return functools.reduce(aux, functions, lambda a: a)
