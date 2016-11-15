"""
Add global axes to the entire figure.
"""
from typing import Dict
import matplotlib.pyplot


def global_axis(params):
    # type: (Dict) -> Dict
    """Add global axes to the figure

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        an updated dictionary with a new field ['canvas']['global_axes']
    """
    obj_axis = params['canvas']['figure'].add_subplot(
                1, 1, 1,
            )

    # make axis background transparent
    obj_axis.patch.set_alpha(0)

    # turn off the extra axis's tick labels
    matplotlib.pyplot.setp(obj_axis.get_xticklabels(), visible=False)
    matplotlib.pyplot.setp(obj_axis.get_yticklabels(), visible=False)
    obj_axis.set_xticks([])
    obj_axis.set_yticks([])

    # Make the frame line transparent
    for child in obj_axis.get_children():
        if isinstance(child, matplotlib.spines.Spine):
            child.set_color((0,0,0,0))

    params['canvas']['global_axis'] = obj_axis
    return params
