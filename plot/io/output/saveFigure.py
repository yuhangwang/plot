"""
Save the matplotlib 'Figure' object into
an image file.
"""
from matplotlib.figure import Figure


def saveFigure(
            output_file_name,    # type: AnyStr
            object_figure,       # type: Figure
            dpi,                 # type: int
            padding=0.2,         # type: float
            transparent=False    # type: bool
        ):
    # type:(...) -> bool
    """Save figure

    Args:
        output_file_name (str): output file name
        object_figure (object): matplotlib.figure.Figure object
        dpi (int): dpi
        padding (float): padding between figure edge and the figure canvas
        transparent (bool): use transparent background

    Returns:
        True if succeeded
    """
    object_figure.savefig(
        output_file_name,
        bbox_inches='tight',
        dpi=dpi,
        pad_inches=padding,
        transparent=transparent,
        )
    return True
