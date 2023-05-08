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
            print("------------------------------------------------------------------")
            opcion = self.excepcion_menu("Seleccione una opción: ")
            
            print("------------------------------------------------------------------")
            if opcion == 8:
                print("Gracias por utilizar la Calculadora modular de: Andres Cardenas")
                print("------------------------------------------------------------------")
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
                print("------------------------------------------------------------------")
                print("Opción inválida. Por favor, intente de nuevo.")
                print("------------------------------------------------------------------")

    def excepcion_menu(self,mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                if numero >= 1:
                    return numero
                else:
                    print("---------------------------------------------------")
                    print("Por favor, ingrese un dato valido en el menu.")
                    print("---------------------------------------------------")
                    self.menu()
            except ValueError:
                print("-------------------------------------------------------")
                print("Por favor, ingrese un dato valido al menu.")
                print("--------------------------------------------------------")
                self.menu()

    def leer_entero_positivo(self,mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                if numero >= 1:
                    return numero
                else:
                    print("---------------------------------------------------")
                    print("Por favor, ingrese un número entero positivo.")
                    print("---------------------------------------------------")
            except ValueError:
                print("-------------------------------------------------------")
                print("Por favor, ingrese un número entero positivo.")
                print("--------------------------------------------------------")

    def exp_raiz(self,mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                if numero >= 0:
                    return numero
                else:
                    print("---------------------------------------------------")
                    print("Por favor, ingrese un número entero positivo.")
                    print("---------------------------------------------------")
            except ValueError:
                print("-------------------------------------------------------")
                print("Por favor, ingrese un número entero positivo.")
                print("--------------------------------------------------------")

    def suma_modular(self):
        
        a = self.leer_entero_positivo("Ingrese el primer número (entero positivo): ")
        b = self.leer_entero_positivo("Ingrese el segundo número (entero positivo): ")
        n = self.leer_entero_positivo("Ingrese el módulo (entero positivo): ")
        resultado = self.calculadora.suma_modular(a, b, n)
        print("---------------------------------------------------")
        print(f"El resultado de la suma modular es: {resultado}\n")
        print("---------------------------------------------------")

    def producto_modular(self):
        a = self.leer_entero_positivo("Ingrese el primer número: ")
        b = self.leer_entero_positivo("Ingrese el segundo número: ")
        n = self.leer_entero_positivo("Ingrese el módulo: ")
        resultado = self.calculadora.multiplicacion_modular(a, b, n)
        print("--------------------------------------------------------")
        print(f"El resultado del producto modular es: {resultado}\n")
        print("---------------------------------------------------------")

    def inverso_modular(self):
        a = self.leer_entero_positivo("Ingrese el número: ")
        n = self.leer_entero_positivo("Ingrese el módulo: ")
        resultado = self.calculadora.inverso_modular(a, n)
        if resultado is not None:
            print("---------------------------------------------------------")
            print(f"El inverso modular de {a} en Z_{n} es: {resultado}\n")
            print("----------------------------------------------------------")
        else:
            print("---------------------------------------------------")
            print(f"No existe un inverso modular para {a} en Z_{n}\n")
            print("---------------------------------------------------")

    def division_modular(self):
        a = self.leer_entero_positivo("Ingrese el numerador: ")
        b = self.leer_entero_positivo("Ingrese el denominador: ")
        n = self.leer_entero_positivo("Ingrese el módulo: ")
        resultado = self.calculadora.division_modular(a, b, n)
        if resultado is not None:
            print("-----------------------------------------------------------")
            print(f"El resultado de la división modular es: {resultado}\n")
            print("------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------------------")
            print(f"No se puede realizar la división modular en Z_{n} porque {b} no tiene inverso\n")
            print("----------------------------------------------------------------------------------")
    def potencia_modular(self):
        a = self.leer_entero_positivo("Ingrese la base: ")
        k = self.leer_entero_positivo("Ingrese el exponente: ")
        n = self.leer_entero_positivo("Ingrese el módulo: ")
        resultado = self.calculadora.potencia_modular(a, k, n)
        print("---------------------------------------------------------")
        print(f"El resultado de la potencia modular es: {resultado}\n")
        print("----------------------------------------------------------")

    def raiz_cuadrada_modular(self):
        a = self.exp_raiz("Ingrese el número: ")
        n = self.leer_entero_positivo("Ingrese el modulo: ")
        resultados = self.calculadora.raizCuadradaModular(a, n)
        if len(resultados) >= 1:
            print("---------------------------------------------------------------------------------")
            print(f"Las raíces cuadradas de {a} en Z_{n} son: {resultados}")
            print("---------------------------------------------------------------------------------")
        else:
            print(f"No hay raíces cuadradas de {a} en Z_{n}\n")

    def cuadrados_perfectos_mod_n(self):
        n = self.leer_entero_positivo("Ingrese el valor de n: ")
        resultados = self.calculadora.cuadrados_perfectos(n)
        print("-------------------------------------------------------------------------------------")
        print(f"Los cuadrados perfectos en Z_{n} son: {resultados}\n")
        print("--------------------------------------------------------------------------------------")
