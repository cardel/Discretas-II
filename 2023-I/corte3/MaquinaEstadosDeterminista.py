"""
Carlos A Delgado
Fecha: 15/06/2023

Implementar una maquina de estados FINITO DETERMINISTA
"""
# ==============================================================================
import numpy as np


"""
Este automata reconoce la expresión regular
a* U ba* y recibe como entrada la cadena y como salida si es aceptado o no
"""
def automata(cadena):
  Q = {"q0", "q1", "q2"}
  Sigma = {"a", "b"}
  q0 = "q0"
  T = {"q0","q1"}
  delta = {"q0":{"a":"q0", "b":"q1"}, "q1":{"a":"q1", "b":"q2"}, "q2":{"a":"q2", "b":"q2"}}

  estado = q0
  for c in cadena:
    estado = delta[estado][c]

  return estado in T

cadena = "baaa"
print(automata(cadena))
cadena = "bab"
print(automata(cadena))
cadena = "baaaaaaaaaaabbbb"
print(automata(cadena))

"""
Este automata reconoce la expresión regular
01* U 01*0 y recibe como entrada la cadena y como salida si es aceptado o no
"""
def automata2(cadena):
  Q = {"q0", "q1", "q2","q3"}
  Sigma = {"0", "1"}
  q0 = "q0"
  T = {"q1","q2"}
  delta = {"q0":{"0":"q1", "1":"q3"}, "q1":{"0":"q2", "1":"q1"}, "q2":{"0":"q3", "1":"q3"},"q3":{"0":"q3", "1":"q3"}}

  estado = q0
  for c in cadena:
    estado = delta[estado][c]

  return estado in T

print("Automata 2")
cadena = "010"
print(automata2(cadena))
cadena= "0100"
print(automata2(cadena))
cadena = "111000"
print(automata2(cadena))
