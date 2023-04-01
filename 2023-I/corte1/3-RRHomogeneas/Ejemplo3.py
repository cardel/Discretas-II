"""
Carlos A Delgado
T(n) = -4T(n-1)-4T(n-2), T(0) = 10, T(1) = -10
"""

def T(n):
    if n==0:
        return 10
    elif n==1:
        return -10
    else:
        return -4*T(n-1)-4*T(n-2)
  
def sol(n):
    return (-5*n+10)*(-2)**n

for n in range(0,10):
  print(n,T(n),sol(n))
