
# Ejercicio 5. 

""""
    Hacer un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
    Usando la fórmula para la conversión de temperaturas es: F = 9/5 * C + 32.
"""
print("")
print("Convirtiendo Farenheit a Celsius")
print("")
farenheit = int(input("Ingrese la cantidad de Grados Farenheit: "))
convertir_farenheit_a_celsius =  (farenheit - 32) * (5 / 9)
print("")
print("La conversion da el resultado de", convertir_farenheit_a_celsius, "Grados Celsius")

# Ejercicio 6. 

""" 
    Dadas las variables a, b y c, escribir un programa que intercambie el valor de las variables tal que 
    el valor de la variable a pase a la variable b, la b a la c y la c a la a.
"""
print("")
print("Dadas las variables a, b y c")
print("-----------------------------")
a = int(input("Ingrese valor de a: "))
b = int(input("Ingrese valor de b: "))
c = int(input("Ingrese valor de c: "))
b = a
c = b
a = c
print("")
print("Ahora A vale: ", a)
print("Ahora B vale: ", b)
print("Ahora C vale: ", c)

# Manejo de operadores relacionales

# Ejercicio 7. 

"""
    Introduzca las siguientes expresiones en la terminal de Python y evalúe que obtiene:
"""
print("")
print("Evaluar distintas expresiones")
expresion = 3 == 3
print("El resultado es", expresion)
expresion = 3 == 4
print("El resultado es", expresion)
expresion = 3 != 4
print("El resultado es", expresion)
expresion = 3 > 4
print("El resultado es", expresion)
expresion = 3 < 4
print("El resultado es", expresion)
expresion = 3 < 3
print("El resultado es", expresion)
expresion = 3 >= 4
print("El resultado es", expresion)
expresion = 3 <= 4
print("El resultado es", expresion)
expresion = 3 <= 3
print("El resultado es", expresion)
