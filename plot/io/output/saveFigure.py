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
    obj_figure = params['internal']['canvas']['figure']
    for f_out in params['global']['figure']['outputs']:
        obj_figure.savefig(
                f_out,
                bbox_inches='tight',
                dpi=params['global']['figure']['dpi'],
                pad_inches=params['global']['figure']['padding'],
                transparent=params['global']['figure']['transparent'],
            )
    return params
