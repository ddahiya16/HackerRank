import numpy

l = input().split()
l = tuple(map(int, l))
    
print(numpy.zeros(l,dtype = int))
print(numpy.ones(l, dtype = int))
