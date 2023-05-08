import math

class CalculadoraModular:

    # Suma dos números y devuelve el resultado módulo n
    def suma_modular(self, a, b, n):
        return ((a + b) % n)
    
    # Multiplica dos números y devuelve el resultado módulo n
    def multiplicacion_modular(self, a, b, n):
        return ((a * b) % n)
    
    #El metodo extended toma dos argumentos: a y b, que son los números para los que deseamos calcular 
    # el MCD y los coeficientes de Bézout.
    def extended(self, a, b): 
        #Inicializa las variables "x", "y", "u", "v". Las variables "x", "y" almacenarán los coeficientes 
        # de Bézout, mientras que "u", "v" se utilizan para actualizar "x","y" en cada iteración del bucle.
        x, y, u, v = 0, 1, 1, 0
        #El bucle while se ejecuta mientras a no sea igual a 0.
        while a != 0:
            #Calcula "q" y "r", que son el cociente y el residuo de la división entera de "b" por "a".
            #Utilizando division entera // y el modulo
            q, r = b // a, b % a
            # Actualiza los coeficientes de Bézout
            m, n = x - u * q, y - v * q
            # Actualiza las variables para el siguiente ciclo
            b, a, x, y, u, v = a, r, u, v, m, n
        #Cuando "a" se vuelve 0, el bucle termina y se devuelve el MCD (que es el valor actual de "b") 
        # junto con los coeficientes de Bézout "x" e "y".
        return b, x, y

    #Calcula el inverso modular de a módulo n utilizando el metodo extended anterior
    def inverso_modular(self, a, n):
        
        #Esta función devuelve tres valores: el máximo común divisor "g" de "a" y "n", así como los 
        # coeficientes de Bézout "x" e "y". Aquí, solo nos interesan los valores de "g" y "x", 
        # por lo que usamos "_" para ignorar el valor de "y".
        g, x, _ = self.extended(a, n)
        #Comprueba si g es igual a 1. Si g es 1, eso significa que a y n son coprimos
        if g == 1:
            #Si g es 1, entonces el coeficiente de Bézout "x" es el inverso multiplicativo modular 
            # que estamos buscando y se realiza la operacion x % n
            return x % n
        #Si no cumple devuelve None
        return None
    
    #La función division_modular toma tres argumentos: "a", el numerador de la división,"b", 
    # el denominador de la división, y "n", el módulo.
    def division_modular(self, a, b, n):

        #Llama a la función inverso_modular(b, n) para calcular el inverso multiplicativo
        inverso_b = self.inverso_modular(b, n)
        #Comprueba si inverso_b no es None. Si inverso_b no es None, eso significa que existe un 
        # inverso multiplicativo modular
        if inverso_b is not None:
            #En este caso, multiplica a por inverso_b y calcula el resultado en módulo n usando 
            # ((a * inverso_b) % n). 
            # Este valor es el resultado de la división modular y se devuelve.
            return ((a * inverso_b) % n)
        else:
            #Si no cumple devuelve None
            return None
        
    #La función potencia_modular toma tres argumentos: a, la base de la potencia, k,
    #el exponente de la potencia, y n, el módulo.
    def potencia_modular(self, a, k, n):
        #Utiliza la función incorporada pow(a, k, n) para calcular la potencia modular.
        #Retorna el resultado de la operación pow(a, k, n), que es el valor de a^k (mod n)
        return pow(a, k, n)
    
    # Encuentra las raíces cuadradas de un número módulo n
    def raizCuadradaModular(self, valor, n):
        valor = valor % n
        #lista para guardar las raices encontradas
        raices = []
        #Bucle for para iterar sobre todos los números enteros i
        for i in range(0, n):
            #Calcular el cuadrado para cada entero i
            a = i * i
            #si el resultado de a%1 es igual al valor lo agrega a lista ya que es una raiz cuadrada
            if a % n == valor:
                raices.append(i)
        return raices

    # Encuentra todos los cuadrados perfectos en Zn (Z mod n)
    def cuadrados_perfectos(self, n):
        #list comprehension que calcula el cuadrado (i*i) y luego le saca el modulo
        #utilizacion del set para borrar los duplicados en la lista
        return list(set(i * i % n for i in range(n)))

    def lista_inversos(self, n):
        inversos = {}
        for A in range(0, n):
            for X in range(1, n):
                operacion = (A % n) * (X % n)
                if operacion % n == 1:
                    inversos[A] = X
        return inversos

    
    def modulo(self, a, n):
        return(a % n)
