import numpy as np

#Ax + b 

A = np.array(
    [
    [1,0,1],
    [2,2,-3],
    [4,8,9]
    ]
)

b = np.array([4,8,10])

print(np.linalg.solve(A,b))

def T(n):
  if n==0:
    return 4
  elif n==1:
    return 8
  elif n==2:
    return 10
  else:
    return T(n-1)+8*T(n-2)-12*T(n-3)
  
def f(n):
  return (4.24-0.6*n)*2**n-0.24*(-3)**n


for n in range(0,10):
  print(n,T(n),f(n))
