"""
Carlos A Delgado
Comprobar la RR que cuenta las cadenas binarias que no puede tener dos 1 consecutivos
"""

def generador_aux(lst,value):
   sal = []
   for el in lst:
      if not (el[-1]=="1" and value[-1]=="1"):
        sal.append(el + value)
   return sal

def generador(n):
    if n==1:
      return ["0","1"]
    else:
        ls1 = generador_aux(generador(n-1),"0")
        ls2 = generador_aux(generador(n-1),"1")
        for x in ls2:
           ls1.append(x)
        return ls1
         
def T(n):
   if n==1:
      return 2
   elif n==2:
      return 3
   else:
      return T(n-1)+T(n-2)       
      

for n in range(1,20):
   print(n,len(generador(n)),T(n))
