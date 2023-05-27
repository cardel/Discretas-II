"""
27 de Mayo de 2023
Implementación arbol en Python
"""

class Arbol:
    def __init__(self, valor, hizq, hder):
      self.valor = valor
      self.hizq = hizq
      self.hder = hder

    def preorden(self):
      recorrIzq = ""
      recorrDer = ""
      if self.hizq is not None:
        recorrIzq = self.hizq.preorden()
      if self.hder is not None:
        recorrDer = self.hder.preorden()
      return (str(self.valor)+" "+recorrIzq+" "+recorrDer).strip()

    def inorden(self):
      recorrIzq = ""
      recorrDer = ""
      if self.hizq is not None:
        recorrIzq = self.hizq.inorden()
      if self.hder is not None:
        recorrDer = self.hder.inorden()
      return (recorrIzq+" "+str(self.valor)+" "+recorrDer).strip()
      
    def posorden(self):
      recorrIzq = ""
      recorrDer = ""
      if self.hizq is not None:
        recorrIzq = self.hizq.posorden()
      if self.hder is not None:
        recorrDer = self.hder.posorden()
      return (recorrIzq+" "+recorrDer +" "+str(self.valor)).strip()
