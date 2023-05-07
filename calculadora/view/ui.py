from calculadora.modelo.calculadora_modular_poo import CalculadoraModular

class UIConsola:

    def __init__(self):
        self.calculadora = CalculadoraModular()

    def menu(self):
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
            if opcion == 8:
                break
            if opcion == 1:
                self.suma_modular()

            elif opcion == 2:
                self.producto_modular()

            elif opcion == 3:
                self.inverso_modular()

            elif opcion == 4:
                self.division_modular()

            elif opcion == 5:
                self.potencia_modular()

            elif opcion == 6:
                self.raiz_cuadrada_modular()

            elif opcion == 7:
                self.cuadrados_perfectos_mod_n()

            else:
                print("Opción inválida. Por favor, intente de nuevo.")

    def leer_entero_positivo(self,mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                if numero >= 0:
                    return numero
                else:
                    print("Por favor, ingrese un número entero positivo.")
            except ValueError:
                print("Por favor, ingrese un número entero positivo.")

    def suma_modular(self):
        
        a = self.leer_entero_positivo("Ingrese el primer número (entero positivo): ")
        b = self.leer_entero_positivo("Ingrese el segundo número (entero positivo): ")
        n = self.leer_entero_positivo("Ingrese el módulo (entero positivo): ")
        resultado = (a + b) % n
        print(f"El resultado de la suma modular es: {resultado}\n")

    def producto_modular(self):
        a = self.leer_entero_positivo("Ingrese el primer número: ")
        b = self.leer_entero_positivo("Ingrese el segundo número: ")
        n = self.leer_entero_positivo("Ingrese el módulo: ")
        resultado = (a * b) % n
        print(f"El resultado del producto modular es: {resultado}\n")

    def inverso_modular(self):
        a = int(input("Ingrese el número: "))
        n = int(input("Ingrese el módulo: "))
        resultado = self.calculadora.modular_inverse(a, n)
        if resultado is not None:
            print(f"El inverso modular de {a} en Z_{n} es: {resultado}\n")
        else:
            print(f"No existe un inverso modular para {a} en Z_{n}\n")

    def division_modular(self):
        a = int(input("Ingrese el numerador: "))
        b = int(input("Ingrese el denominador: "))
        n = int(input("Ingrese el módulo: "))
        inverso_b = self.calculadora.modular_inverse(b, n)
        if inverso_b is not None:
            resultado = (a * inverso_b) % n
            print(f"El resultado de la división modular es: {resultado}\n")
        else:
            print(f"No se puede realizar la división modular en Z_{n} porque {b} no tiene inverso\n")

    def potencia_modular(self):
        a = int(input("Ingrese la base: "))
        k = int(input("Ingrese el exponente: "))
        n = int(input("Ingrese el módulo: "))
        resultado = pow(a, k, n)
        print(f"El resultado de la potencia modular es: {resultado}\n")

    def raiz_cuadrada_modular(self):
        a = int(input("Ingrese el número: "))
        p = int(input("Ingrese el primo (de la forma 4k+3): "))
        try:
            resultados = self.calculadora.modular_sqrt(a, p)
            if resultados:
                print(f"Las raíces cuadradas de {a} en Z_{p} son: {resultados[0]} y {resultados[1]}\n")
            else:
                print(f"No hay raíces cuadradas de {a} en Z_{p}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    def cuadrados_perfectos_mod_n(self):
        n = int(input("Ingrese el valor de n: "))
        resultados = self.calculadora.perfect_squares_mod_n(n)
        print(f"Los cuadrados perfectos en Z_{n} son: {resultados}\n")
