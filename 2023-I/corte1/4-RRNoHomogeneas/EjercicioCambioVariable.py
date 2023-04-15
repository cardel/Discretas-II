"""
Ejercicio cambio de variable
"""

import math

def T(n):
    if n==1:
        return 10
    else:
        return 2*T(n/2)+ 2*math.log2(n)

def f(n):
    return 14*n-2*math.log2(n)-4


lst = [2**x for x in range(0,10)]

for n in lst:
    print(n,T(n),f(n))
