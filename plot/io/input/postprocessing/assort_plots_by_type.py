"""
Assort the plots by their types
and store them in the plotting parameter dictionary
"""
from typing import Dict


def assort_plots_by_type(params):
    # type: (Dict) -> Dict
    """Assort the plots by their types

    Args:
        params (dict): global plotting parameter dictionary

    Returns:
        an updated parameter dictionary
    """
    params['internal']['user']['plots'] = dict()

    for t in params['internal']['available']['plot_types']:
        params['internal']['user']['plots'][t] = []

    for i in range(len(params['data'])):
        plot_type = params['data'][i]['plot_type']
        params['internal']['user']['plots'][plot_type].append(i)
    return params
