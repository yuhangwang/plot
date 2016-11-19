"""
Set which data columns to use for line objects
"""
from typing import Dict
import numpy
from ..readDataFile import readDataFile


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
        if p['values'] is not None:
            data = numpy.array(p['values'])
        elif p['file'] is not None:
            data = readDataFile(p['file'], p['skip_rows'])
        else:
            continue

        if len(numpy.shape(data)) == 0:
            continue
        elif len(numpy.shape(data)) == 1:
            num_columns = 1
        else:
            num_columns = numpy.shape(data)[1]

        if p['line']['data_column']['x'] is None:
            if num_columns > 1:
                p['line']['data_column']['x'] = 0
            else:
                p['line']['data_column']['x'] = None

        if p['line']['data_column']['y'] is None:
            if num_columns == 1:
                p['line']['data_column']['y'] = 0
            else:
                p['line']['data_column']['x'] = 1
                
        return params


