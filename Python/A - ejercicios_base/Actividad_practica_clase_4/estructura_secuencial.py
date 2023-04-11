# Estructura secuencial

# Ejercicio 1: 

"""
    Calcular el promedio de las notas que obtiene un 
    alumno al rendir los dos parciales. 
"""

print("Ejercicio 1")
print("-----------")
nota1 = (int(input("Ingrese nota 1: ")))
nota2 = (int(input("Ingrese nota 2: ")))
promedio = (nota1 + nota2) / 2
print("El promedio de las notas es: ", promedio)
print("")

# Ejercicio 2:

"""
     Leer una medida en metros e imprimir esta medida 
     expresada en centímetros y kilómetros.
"""

print("Ejercicio 2 - Ingrese medida en Metros y devuelve el programa centrimetros y kilometros")
print("---------------------------------------------------------------------------------------")
medida_metros = int(input("Ingrese la medida en Metros: "))
print("")
print("El resultado en cm es: ", medida_metros * 100, " cm")
print("El resultado en km es: ", medida_metros / 1000, " km")
print("")
