"""
    TIPOS, VARIABLES, EXPRESIONES, ASIGNACIONES
    Ejercicio 1
"""

# A. Definir una variable y asignarle un valor numérico. Mostrar por consola. Por ej: miNumero=10 deberá mostrar el número 10.

miNumero = 8
print(miNumero)
print(" ")

# b. Definir una variable de tipo texto y asignar el mensaje “Hola Mundo”. Mostrar por consola.Debería mostrar por consola Hola Mundo.

miString = "Hola Mundo"
print(miString)
print(" ")

# C
print("c. Asignar a dos variables dos números y guardar el resultado en otra variable. Con esos datos mostrar la suma, la diferencia, la multiplicación y división.")

primerNum = [1, 2]
segundoNum = [4, 5]
guardoLasDos = primerNum, segundoNum
#suma
suma = guardoLasDos[0] + guardoLasDos[1]
suma = (int(suma[0])) + (int(suma[1])) + (int(suma[2])) + (int(suma[3])) 
print("La suma es: ", suma)
#resta
resta = guardoLasDos[0] + guardoLasDos[1]
resta = (int(resta[0])) - (int(resta[1])) - (int(resta[2])) - (int(resta[3]))
print("La resta es: ", resta)
#multiplica
multiplica = guardoLasDos[0] + guardoLasDos[1]
multiplica = (int(multiplica[0])) * (int(multiplica[1])) * (int(multiplica[2])) * (int(multiplica[3]))
print("La multiplicacion es: ", multiplica) 
#division
division = guardoLasDos[0] + guardoLasDos[1]
division = (int(division[0])) / (int(division[1])) / (int(division[2])) / (int(division[3]))
print("La division es: ", division) 
print(" ")

# D
print("d. Ingresar tres números y con esos datos mostrar la suma y el promedio")
ingresoPrimero = input("Ingrese el primer numero: ")
ingresoSegundo = input("Ingrese el segundo numero: ")
ingresoTercero = input("Ingrese el tercer numero: ")
suma = (int(ingresoPrimero + ingresoSegundo + ingresoTercero))
promedio = suma / 3
print("La suma es : ", suma)
print("El promedio es: ", promedio)
print(" ")

# E
print("e. Imprima el tipo de dato de una variable numérica entera y una variable numérica decimal.")
numeroEntero = 5
numeroDecimal = 10.50
print("El tipo ", type(numeroEntero), " pertenece al valor", numeroEntero)
print("El tipo ", type(numeroDecimal), " pertenece al valor", numeroDecimal)
