# Estructura de datos básicas

# Ejercicio 1: 

"""
    Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la 
    cantidad de letras que lo componen.
"""

print("----- Ejercicio  1 -----")
nombre_persona = input("Ingrese el nombre de la persona: ")
print("El primer caracter que compone el nombre es: ", nombre_persona[0])
print("La cantidad de letras del nombre son: ", len(nombre_persona))
print("")

# Ejercicio 2: 

"""
    Mostrar uno a uno los nombres almacenados en la siguiente lista:
    nombres = [‘Juan’, ‘Marcos’, ‘Laura’, ‘Jose’]
""" 
print("----- Ejercicio  2 ----- Mostrar nombres almacenados")
nombres = ["Juan", "Marcos", "Laura", "Jose"]
print("El nombre en el indice 0 es: ", nombres[0])
print("El nombre en el indice 1 es: ", nombres[1])
print("El nombre en el indice 2 es: ", nombres[2])
print("El nombre en el indice 3 es: ", nombres[3])
print("")

# Ejercicio 3:

"""
    Definir una lista por asignación que almacene los nombres de los primeros cuatro meses de año. 
    Mostrar el primer y último elemento de la lista solamente
"""

print("----- Ejercicio  3 ----- Mostrar 1eros 4 meses del año")
meses_del_anio = ["Enero", "Febrero","Marzo", "Abril"]
print("El MES en el primer lugar es: ", meses_del_anio[0])
print("El MES en el ultimo lugar es: ", meses_del_anio[-1])
print("")

# Ejercicio 4: 
# Calcular la suma de los números de una lista. Aun sin el FOR

print("----- Ejercicio  4 ----- Calcular suma de los numeros de una lista")
print("La  lista_numeros = [1, 2, 3, 4, 5, 6, 7] ")
lista_numeros = [1, 2, 3, 4, 5, 6, 7]
suma = lista_numeros[0] + lista_numeros[1] + lista_numeros[2] + lista_numeros[3] + lista_numeros[4] + lista_numeros[5] + lista_numeros[6]
print("La suma es: ", suma)
print("")

# Ejercicio 5: 

"""
    Desarrollar un algoritmo que permita mostrar una lista de enteros con sus valores a la mitad. 
    Ejemplo: Lista [1,2,3,4], mostrar: 0.5 1.0 1.5 2.0
""" 

print("----- Ejercicio  5 ----- Numeros de la lista a la mitad")
print("la_lista = [1,2,3,4]")
la_lista = [1,2,3,4]
print("El primer elemento de la lista ahora vale: ", la_lista[0] / 2)
print("El primer elemento de la lista ahora vale: ", la_lista[1] / 2)
print("El primer elemento de la lista ahora vale: ", la_lista[2] / 2)
print("El primer elemento de la lista ahora vale: ", la_lista[3] / 2)
print("")

# Ejercicio 6: 

"""
    Definir una lista por asignación que almacene en la primer componente el nombre de un alumno 
    y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.
""" 

print("----- Ejercicio  6 ----- Alumno y promedio de notas")
lista_alumno = []
lista_alumno.append(input("Ingrese el Nombre del alumno: ")) 
lista_alumno.append(int(input("Ingrese la 1era nota: "))) 
lista_alumno.append(int(input("Ingrese la 2da nota: "))) 
promedio = (lista_alumno[1] + lista_alumno[2]) / 2 
print("El nombre del alumno es: ", lista_alumno[0])
print("El Promedio de notas del alumno es: ", promedio)
print("")

# Ejercicio 7: 

"""
    Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. 
    Imprimir la lista generada.
""" 

print("----- Ejercicio  7 ----- Lista de 5 numeros")
lista_nums = []
lista_nums.append(int(input("Ingrese 1er Numero: "))) 
lista_nums.append(int(input("Ingrese 2do Numero: "))) 
lista_nums.append(int(input("Ingrese 3er Numero: "))) 
lista_nums.append(int(input("Ingrese 4to Numero: "))) 
lista_nums.append(int(input("Ingrese 5to Numero: "))) 
print("La lista de numeros es: ", lista_nums)
print("")

# Ejercicio 8: 

"""
    Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.
"""
print("----- Ejercicio  8 -----")
print("La lista_con_cinconumeros = [2, 4, 6, 8, 10]")
lista_con_cinconumeros = [2, 4, 6, 8, 10]
lista_con_cinconumeros.pop(0)
lista_con_cinconumeros.pop(-1)
lista_con_cinconumeros.pop(2)
print("La lista quedaria asi")
print(lista_con_cinconumeros)
