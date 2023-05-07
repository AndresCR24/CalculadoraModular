import math

class CalculadoraModular:

    def gcd(self, a, b):
        if b < 0:
            raise ValueError("Ingresa un numero entero positivo")
        while b:
            a, b = b, a % b
        return a

    def extended_gcd(self, a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        return b, x, y

    def modular_inverse(self, a, n):
        g, x, _ = self.extended_gcd(a, n)
        if g == 1:
            return x % n
        return None

    def modular_sqrt(self, a, p):
        if p % 4 != 3:
            raise ValueError("El algoritmo de raíz cuadrada modular solo funciona para primos de la forma 4k+3")
        if p == 2:
            return [a % 2]
        if pow(a, (p - 1) // 2, p) != 1:
            return []
        r = pow(a, (p + 1) // 4, p)
        return [r, p - r]

    def perfect_squares_mod_n(self, n):
        return list(set(i * i % n for i in range(n)))