import math

"""def gcd(a, b):
    while b:
        a, b = b, a % b
    return a"""

def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y

def modular_inverse(a, n):
    g, x, _ = extended_gcd(a, n)
    if g == 1:
        return x % n
    return None

def modular_sqrt(a, p):
    if p % 4 != 3:
        raise ValueError("El algoritmo de raíz cuadrada modular solo funciona para primos de la forma 4k+3")
    if p == 2:
        return [a % 2]
    if pow(a, (p - 1) // 2, p) != 1:
        return []
    r = pow(a, (p + 1) // 4, p)
    return [r, p - r]

def perfect_squares_mod_n(n):
    return [i * i % n for i in range(n)]

def main():
    while True:
        print("Calculadora Modular\n")
        print("1. Suma modular")
        print("2. Producto modular")
        print("3. Inverso modular")
        print("4. División modular")
        print("5. Potencia modular")
        print("6. Raíz cuadrada modular")
        print("7. Cuadrados perfectos en Zn")
        print("8. Salir")

        opcion = int(input("Seleccione una opción: "))
        if opcion not in range(1, 9):
            print("Opción inválida. Por favor, intente de nuevo.")
            continue

        if opcion == 8:
            break

        n = int(input("Ingrese el número n para el modulo Zn(entero positivo, obligatorio): "))
        a = int(input("Ingrese el número  (no negativo, perteneciente a Zn): "))

        if opcion == 1 or opcion == 2 or opcion == 4 or opcion == 5:
            b = int(input("Ingrese el número b (entero no negativo, perteneciente a Zn): "))

        if opcion == 1:
            resultado = (a + b) % n
            print(f"La suma modular de {a} y {b} en Z{n} es: {resultado}")
        elif opcion == 2:
            resultado = (a * b) % n
            print(f"El producto modular de {a} y {b} en Z{n} es: {resultado}")
        elif opcion == 3:
            resultado = modular_inverse(a, n)
            if resultado is None:
                print(f"No existe inverso modular para {a} en Z{n}")
            else:
                print(f"El inverso modular de {a} en Z{n} es: {resultado}")
        elif opcion == 4:
            inv_b = modular_inverse(b, n)
            if inv_b is None:
                print(f"No se puede realizar la división modular de {a} y {b} en Z{n} porque {b} no tiene inverso modular en Z{n}.")
            else:
                resultado = (a * inv_b) % n
                print(f"La división modular de {a} y {b} en Z{n} es: {resultado}")
        elif opcion == 5:
            e = int(input("Ingrese el exponente: "))
            resultado = pow(a, e, n)
            print(f"La potencia modular de {a}^{e} en Z{n} es: {resultado}")
        elif opcion == 6:
            try:
                raices = modular_sqrt(a, n)
                if not raices:
                    print(f"No existen raíces cuadradas para {a} en Z{n}")
                else:
                    print(f"Las raíces cuadradas de {a} en Z{n} son: {raices[0]} y {raices[1]}")
            except ValueError as e:
                print(str(e))
        elif opcion == 7:
            cuadrados_perfectos = perfect_squares_mod_n(n)
            print(f"Los cuadrados perfectos en Z{n} son: {cuadrados_perfectos}")
        print("\n")

if __name__ == "__main__":
    main()

