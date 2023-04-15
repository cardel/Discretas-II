"""
Ejercicio 2 clase
Carlos A Delgado
"""
import math

def T(n):
    if n==1:
        return 10
    elif n==2:
        return 24
    else:
        return 4*T(n/2)-4*T(n/4)+2*n+n*math.log(n,math.e)


def f(n):
  B = 0.5*(2-(4/3)*math.log(2,math.e))
  ln = math.log(2,math.e)
  parte = (ln/6*math.log2(n)+0.5*(ln+2))*n*(math.log2(n))**2
  return 10*n+B*math.log2(n)*n+parte

lst = [4**x for x in range(0,10)]

for n in lst:
    print(n,T(n),f(n))
