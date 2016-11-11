"""
AUTHOR: YUHANG WANG
DATE: 10-11-2016
"""
#================================================
# Use Python 3 compatibility
#================================================
from __future__ import print_function, division
#================================================
import matplotlib
import matplotlib.pyplot 
import sys
import numpy 
import pyparsing
#------------------------------------------------
# MPA Internal modules
#------------------------------------------------
import re
import mpa.mpa_toolkit as MpaTK
from . import io   as IO
import mpa.mpa_core_plot as MPA_PLOT
#================================================

def plot(user_config_dict, preview=False):
	"""
	Main entry for MPA 
	:param str user_config_dict: a python dictionary of user configuration parameters 
	:param bool preview: True | False(default) which decide whether to show a
		preview of the figure 
	"""
	#-------------------------------------------------------------------
	# [1] Read inputs
	#-------------------------------------------------------------------

	[dict_data_parameters, dict_global_parameters, 
	 dict_local_parameters] = IO.read_config(user_config_dict)
	#-------------------------------------------------------------------
	# [3] Plot
	#-------------------------------------------------------------------
	object_figure, list_axis_objects = MPA_PLOT.plot(dict_data_parameters, 
		dict_global_parameters,
		dict_local_parameters)

	#-----------------------------------------------------------------
	# [4] Save
	#-----------------------------------------------------------------
	IO.save_figure(object_figure, 
		dict_global_parameters["figure_output_file"],
		figure_dpi = dict_global_parameters["figure_dpi"],
		figure_padding = dict_global_parameters["figure_padding"],
		figure_transparent = dict_global_parameters["figure_transparent"],
		)
	
	#-----------------------------------------------------------------
	# [5] Preview?
	#-----------------------------------------------------------------
	if preview: matplotlib.pyplot.show()

	return (object_figure, list_axis_objects)


