import math

class CalculadoraModular:

    def suma_modular(self, a, b, n):
        return ((a + b) % n)
    
    def multiplicacion_modular(self, a, b, n):
        return ((a * b) % n)
    
    def extended(self, a, b):  #Algoritmo extendido de euclides para calcular MCD
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        return b, x, y

    def inverso_modular(self, a, n):
        g, x, _ = self.extended(a, n)
        if g == 1:
            return x % n
        return None
    
    def division_modular(self, a, b, n):
        
        inverso_b = self.inverso_modular(b, n)
        if inverso_b is not None:
            return ((a * inverso_b) % n)
        else:
            return None
    
    def potencia_modular(self, a, k, n):
        return pow(a, k, n)

    def raizCuadradaModular(self, valor, n):
        valor = valor % n
        raices = []
        for i in range(0, n):
            a = i * i
            if a % n == valor:
                raices.append(i)
        return raices


    def cuadrados_perfectos(self, n):
        return list(set(i * i % n for i in range(n)))