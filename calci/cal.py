import math
from complex import ComplexNumber

# you can include the complex class, to use it in other files

def parallel(a, b):
    return (a*b) / (a+b)

L = 9 * 10**-6
C = 127 * 10**-12

print(L, C)

mp = L*C


w = math.sqrt( 1/mp ) 

_C = ComplexNumber(0, -1/(w*C))
_L = ComplexNumber(0, w*L)

print(_C, _L)

R1 = ComplexNumber(1800)
R2 = ComplexNumber(22000)

Z1 = _C
Z2 = R1 + _L
Z3 = R2

#print(parallel(_C, _L))

combinedZ12 = parallel(Z1, Z2)

print(combinedZ12)

#print("C", combinedZ12)

combined = parallel(combinedZ12, Z3)

print(combined)