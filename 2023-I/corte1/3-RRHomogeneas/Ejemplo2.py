"""
Carlos A Delgado
Solución T(n) = 7T(n-1)-12T(n-2)
T(0) = 10, T(1) = 15
"""
def T(n):
    if n==0:
        return 10
    elif n==1:
        return 15
    else:
        return 7*T(n-1)-12*T(n-2)
    
def sol(n):
    return -15*4**n+25*3**n

for n in range(0,40):
  print(n,T(n),sol(n))
