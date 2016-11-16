"""
Return a combine function of
all necessary operations for creating the figure
"""
from typing import Callable, Dict
from .tk.fnTK import compose
from .apps import draw
from .canvas import create as create_canvas
from .finetune import adjust
from .io.output import saveFigure


def workflow(params):
    # type: (Dict) -> Callable
    """Combine all necessary functions into one

    Args:
        params (dict): plotting parameter dictionary
    Returns:
        a function
    """
    aux = compose([
        create_canvas,
        draw,
        adjust,
        saveFigure
        ])
    return aux(params)
