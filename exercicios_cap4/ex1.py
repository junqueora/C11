import numpy

arr1 = numpy.ones(8).astype(int)
arr2 = numpy.random.randint(0, 9, 8)

arr_sum = arr1 + arr2

if sum(arr_sum) >= 40:
    arr_sum = arr_sum.reshape(4, 2)
else:
    arr_sum = arr_sum.reshape(2, 4)