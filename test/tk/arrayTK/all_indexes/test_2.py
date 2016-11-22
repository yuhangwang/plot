from plot.tk.arrayTK import all_indexes
import numpy


def test():
    array = numpy.array([[1, 2], [3, 4]])
    answer = all_indexes(numpy.shape(array))
    solution = [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert answer == solution
