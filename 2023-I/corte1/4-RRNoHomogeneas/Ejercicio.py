"""
Ejercicio en clase
15 de Abril de 2023
"""

def T(n):
    if n==0:
        return 10
    elif n==1:
        return 22
    else:
        return 3*T(n-1)-2*T(n-2)-5*n+3+n*2**n
    
def f(n):
  return 10 + (5/2)*n**2 + (19/2)*n + n**2*2**n - n*2**n


for n in range(0,10):
    print(n,T(n),f(n))
