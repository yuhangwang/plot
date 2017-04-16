"""
Draw all data
"""
from typing import Dict
from ..tk.fnTK import compose
from ..tk.importTK import subimportDict
from ._tk import append_addon
import os


def draw(params):
    # type: (Dict) -> Dict
    """Draw all data

    Args:
        params (dict): parameter dictionary

    Returns:
        the same parameter dictionary
    """
    here = os.path.dirname(os.path.realpath(__file__))
    modules = subimportDict(here, "plot.apps")
    # apps = [m.main for m in modules]
    # aux = compose(apps)
    # return aux(params)
    print(modules.keys())
    axes = params['internal']['canvas']['axes']
    for i in range(len(params['data'])):
        p = params['data'][i]
        fn_plot = modules[p['plot_type']].main
        obj, legend_label = fn_plot(
            axes[p['which_panel']],
            p)
        if legend_label is not None:
            legend_panel = p['legend']['which_panel']
            append_addon(
                'legend',
                obj, legend_label, legend_panel, params)
        else:
            pass

    return params
