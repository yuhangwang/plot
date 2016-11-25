"""
Add color bar label
"""


def add_label(obj, label):
    """Add color bar label

    Args:
        obj (object): a ``matplotlib.colorbar.Colorbar`` object
        label (str): label for the color bar
    Returns:
        same as input
    """
    if bar_label is not None:
        obj_color_bar.set_label(bar_label)
    return obj
