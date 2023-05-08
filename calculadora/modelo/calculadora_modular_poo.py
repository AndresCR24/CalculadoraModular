import math

class CalculadoraModular:

    # Suma dos números y devuelve el resultado módulo n
    def suma_modular(self, a, b, n):
        return ((a + b) % n)
    
    # Multiplica dos números y devuelve el resultado módulo n
    def multiplicacion_modular(self, a, b, n):
        return ((a * b) % n)
    
    # Implementa el Algoritmo Extendido de Euclides para calcular el MCD
    # y también los coeficientes de Bézout
    def extended(self, a, b): 
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            # Divide b entre a y guarda el cociente y el residuo
            q, r = b // a, b % a
            # Actualiza los coeficientes de Bézout
            m, n = x - u * q, y - v * q
            # Actualiza las variables para el siguiente ciclo
            b, a, x, y, u, v = a, r, u, v, m, n
            # Devuelve el MCD (b) y los coeficientes de Bézout
        return b, x, y

    # Calcula el inverso modular de a módulo n utilizando el algoritmo extendido de Euclides
    def inverso_modular(self, a, n):
        g, x, _ = self.extended(a, n)
        if g == 1:
            return x % n
        return None
    
    # Calcula la división modular de a entre b módulo n
    def division_modular(self, a, b, n):
        
        inverso_b = self.inverso_modular(b, n)
        if inverso_b is not None:
            return ((a * inverso_b) % n)
        else:
            return None
        
    # Calcula la potencia modular de a^k módulo n
    def potencia_modular(self, a, k, n):
        return pow(a, k, n)
    
    # Encuentra las raíces cuadradas de un número módulo n
    def raizCuadradaModular(self, valor, n):
        valor = valor % n
        raices = []
        for i in range(0, n):
            a = i * i
            if a % n == valor:
                raices.append(i)
        return raices

    # Encuentra todos los cuadrados perfectos en Zn (Z mod n)
    def cuadrados_perfectos(self, n):
        return list(set(i * i % n for i in range(n)))