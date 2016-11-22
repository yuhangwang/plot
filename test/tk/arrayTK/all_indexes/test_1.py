from plot.tk.arrayTK import all_indexes
import numpy


def test():
    array = numpy.array([1, 2])
    answer = all_indexes(numpy.shape(array))
    solution = [(0,), (1,)]
    assert answer == solution
