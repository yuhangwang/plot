"""
Read User defined configuration dictionary and 
convert it to internal parameter dictionaries.

AUTHOR: YUHANG WANG 
DATE: 10-10-2016
"""
#----------------------------------------------------
from __future__ import print_function, division
#----------------------------------------------------
import re
import json
#----------------------------------------------------
import mpa.mpa_toolkit as MpaTK
from mpa.mpa_core_parameter import UserDataParameters  as MpaDataParameters
from mpa.mpa_core_parameter import GlobalParameters    as MpaGlobalParameters
from mpa.mpa_core_parameter import LocalParameters      as MpaLocalParameters
from mpa.mpa_reader_data_parameter import read   as MpaDataParameterReader
from mpa.mpa_reader_global_parameter import read as MpaGlobalParameterReader
from mpa.mpa_reader_local_parameter import read  as MpaLocalParameterReader
#----------------------------------------------------


#----------------------------------------------------
#                     INPUT
#----------------------------------------------------
def read_config(params):
    """
    Read a file containing a list of plot parameters 
    and put them into a python dictionary.
    :param str params: user configuration parameter dictionary
    :return: (dict_data_parameters, dict_global_plot_parameters, dict_local_plot_parameters)
    """
    print([k for k in params.keys()])
    # Read file parameters 
    dict_data_parameters  = MpaDataParameterReader([MpaTK.lowercase_keys(d) for d in params["data"]])

    # Read global parameters
    dict_global_plot_parameters = MpaGlobalParameterReader(MpaTK.lowercase_keys(params["global"]))

    # Read local parameters 
    dict_local_plot_parameters = MpaLocalParameterReader([MpaTK.lowercase_keys(d) for d in params["local"]])

    if len(dict_data_parameters.keys()) == 0:
        msg = "ERROR HINT: YOU MUST SPECIFY AT LEAST ONE GROUP OF INPUT DATA PARAMETERS\n"
        raise UserWarning(msg)

    return (dict_data_parameters, dict_global_plot_parameters, dict_local_plot_parameters)
