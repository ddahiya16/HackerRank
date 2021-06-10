import numpy
n, m, p = map(int, input().split())
array1 = numpy.array([input().strip().split() for _ in range(n)], int)
array2 = numpy.array([input().strip().split() for _ in range(m)], int)
ar = numpy.concatenate((array1, array2))
print(ar)
