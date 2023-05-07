import math

class CalculadoraModular:

    def suma_modular(self, a, b, n):
        return ((a + b) % n)
    
    def multiplicacion_modular(self, a, b, n):
        return ((a * b) % n)
    
    def extended(self, a, b):  #Algoritmo de euclides para calcular MCD
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
        
        return ((a * self.inverso_modular(b, n)) % n)

    def raiz_cuadrada_modular(self, a, p):

        if p == 2:
            return [a % 2]
        if pow(a, (p - 1) // 2, p) != 1:
            return []
        r = pow(a, (p + 1) // 4, p)
        return [r, p - r]

    def cuadrados_perfectos(self, n):
        return list(set(i * i % n for i in range(n)))