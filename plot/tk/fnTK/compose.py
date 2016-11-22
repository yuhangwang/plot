"""
Take many functions and compose
"""
from typing import List, Callable, Optional


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
        return lambda x: f2(f1(x))

    def tail(xs): return xs[1:]

    def reduce(aux, functions, f):
        if len(functions) == 0:
            return f
        else:
            return reduce(
                aux, tail(functions), aux(f, functions[0]))

    return reduce(aux, functions, lambda a: a)
