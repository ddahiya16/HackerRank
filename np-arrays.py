import numpy

def arrays(arr):
    b = numpy.array([],dtype = 'float')
    for i in range(len(arr)-1, -1, -1):
        b = numpy.append(b, float(arr[i]))
        
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
