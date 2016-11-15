"""
Save the matplotlib 'Figure' object into
an image file.
"""
from matplotlib.figure import Figure


def saveFigure(params):
    # type:(Dict) -> bool
    """Save figure

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        same as input
    """
    obj_figure = params['canvas']['figure']
    obj_figure.savefig(
            params['global']['figure']['output'],
            bbox_inches='tight',
            dpi=params['global']['figure']['dpi'],
            pad_inches=params['global']['figure']['padding'],
            transparent=params['global']['figure']['transparent'],
        )
    return params
