import numpy

arr1 = numpy.arange(0, 52, 2)
arr2 = numpy.arange(100, 49, -2)

arr_concat = numpy.concatenate((arr1, arr2))

print(numpy.sort(arr_concat))