from Arbol import Arbol


arbol = Arbol(
    1,
    Arbol(
        2,
        Arbol(
            4,
            Arbol(8, None,None),
            Arbol(9,None,None)
        ),
        Arbol(5,None,None)
    ),
    Arbol(3,
          Arbol(6,None,None),
          Arbol(7,None,None)
          )
)

print(arbol.valor)
print(arbol.hizq.valor)
print(arbol.hizq.hizq.valor)
print(arbol.hder.hder.valor)
print(arbol.preorden())
print(arbol.inorden())
print(arbol.posorden())

cola = [arbol]
salida = ""

while len(cola)>0:
  elm = cola.pop(0)
  salida+= str(elm.valor)+" "
  if elm.hizq is not None:
    cola.append(elm.hizq) #Inserto al final
  if elm.hder is not None:
    cola.append(elm.hder) #Inserto al final

print("Recorrido por amplitud ",salida)


pila = [arbol]
salida = ""

while len(pila)>0:
  elm = pila.pop(0)
  salida+= str(elm.valor)+" "
  if elm.hder is not None:
    pila.insert(0,elm.hder) #Inserto al inicio
  if elm.hizq is not None:
    pila.insert(0,elm.hizq) #Inserto al inicio


print("Recorrido por profundidad Izq ",salida)

pila = [arbol]
salida = ""
while len(pila)>0:
  elm = pila.pop(0)
  salida+= str(elm.valor)+" "
  if elm.hizq is not None:
    pila.insert(0,elm.hizq) #Inserto al inicio
  if elm.hder is not None:
    pila.insert(0,elm.hder) #Inserto al inicio



print("Recorrido por profundidad Der ",salida)

