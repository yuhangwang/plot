"""
Set which data columns to use for line objects
"""
from typing import Dict
from ..readDataFile import readDataFile
from ..readFileOrList import readFileOrList
import numpy


def set_line_data_columns(params):
    # type: (Dict) -> Dict
    """Set which data columns to user for line objects

    If user specified the data columns, then
    no change will be made.

    If the data only has one column,
    then set the default y column is 0-th column.

    If the data has more than one columns,
    then set the x column to 0 and y column to 1.

    Args:
        params (dict): plotting parameter dictionary

    Returns:
        updated params
    """
    for i in params['internal']['user']['plots']['line']:
        p = params['data'][i]
        data = readFileOrList(p['file'], p['values'], p['skip_rows'])
        column_count = numpy.shape(data)[1]

        if p['line']['data_column']['x'] is None:
            if column_count > 1:
                p['line']['data_column']['x'] = 0
            else:
                p['line']['data_column']['x'] = None
        else:
            pass

        if p['line']['data_column']['y'] is None:
            if column_count == 1:
                p['line']['data_column']['y'] = 0
            else:
                p['line']['data_column']['x'] = 1
        else:
            pass

        return params
