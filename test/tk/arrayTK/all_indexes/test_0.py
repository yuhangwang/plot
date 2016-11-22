from plot.tk.arrayTK import all_indexes
import numpy


def test():
    array = numpy.array([])
    answer = all_indexes(numpy.shape(array))
    solution = []
    assert answer == solution
