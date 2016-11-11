"""
MPA FILE WRITER
AUTHOR: YUHANG WANG
DATE: 06-24-2015
"""

def save_figure(object_figure, output_file_name, 
	figure_dpi,
	figure_padding=0.2,
	figure_transparent=False,
	):
	"""
	Save figure 
	:param object object_figure: matplotlib Figure object 
	:param str output_file_name: output file name 
	:param int figure_dpi: figure resolution in DPI unit (dots/inch)
	:param float figure_padding: padding between edge of the canvas and the figure edge (default: 0.2)
	:param float figure_transparent: True | False (default: False)
	"""
	object_figure.savefig(output_file_name, 
		bbox_inches='tight', 
		dpi=figure_dpi, 
		pad_inches=figure_padding,
		transparent=figure_transparent,
		)