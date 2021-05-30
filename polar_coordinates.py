import cmath
import math

x = input()


z = complex(x)
i = z.real
j = z.imag

print(math.sqrt(i*i + j*j))
print(cmath.phase(complex(i,j)))
