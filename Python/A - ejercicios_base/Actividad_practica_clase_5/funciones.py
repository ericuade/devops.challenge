"""
    Trabajo Practico 5
    Funciones
"""

# Ejercicio 1. 

"""
    Definir una función que muestre una presentación en pantalla del programa. Solicite la carga de dos 
    valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa. Implementar estas 
    actividades en tres funciones.
"""

def presentacion():
    suma()
    despedida()
    return

def suma():
    suma_2 = 0
    valor1 = int(input("Ingrese valor 1: "))
    valor2 = int(input("Ingrese valor 2: "))
    suma_2 = valor1 + valor2
    print("El resultado de la suma es: ", suma_2)
    return

def despedida():
    print("El programa ha finalizado exitosamente!")

presentacion()

# Ejercicio 2. 

"""
    Definir una función que solicite la carga de dos valores enteros y muestre su suma. 
    Repetir la carga e impresión de la suma 5 veces.Mostrar una línea separadora después 
    de cada vez que cargamos dos valores y su suma.
"""

# Ejercicio 3. 

"""
    Definir una función para imprimir un mensaje por pantalla:
"""

# Ejercicio 4: 

"""
    Escribir dos funciones, una función que le permita al usuario ingresar el texto de la canción favorita 
    y otra para obtener la longitud de esa cadena. Muestre la letra de la canción que ingreso el usuario y la 
    longitud de esa letra.
"""

# Ejercicio 5. 

"""
    Desarrollar una función que solicite la carga de tres valores y muestre el menor. Desde el bloque 
    principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
"""

# Ejercicio 6. 

"""
    Ejercicio 6: Definir dos funciones para Ingresar la primer nota y la segunda nota de los dos parciales 
    de un alumno. Con otra función indicar si promocionó, aprobó o debe recuperar. Se promociona cuando las 
    notas de ambos parciales son mayores o iguales a 7. Se aprueba cuando las notas de ambos parciales son 
    mayores o iguales a 4. Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""

# Ejercicio 7. 

"""
    Definir una función para calcular e imprimir la suma de los números comprendidos entre 42 y 176.
""" 

# Ejercicio 8. 

"""
    Utilizando funciones escribir un algoritmo que solicite un nombre de usuario y una contraseña, y 
    que no permita seguir hasta que se introduzcan correctamente. Deberá repetirse hasta que el usuario sea 
    "admin" y la contraseña sea "1234", y en ese caso mostrar el mensaje “Login exitoso”. Tras 3 intentos sin 
    acertar, se deberá mostrar un mensaje indicando que se agotaron esos 3 intentos y finaliza el programa.
"""

# Ejercicio 9. 

"""
    Utilizando una función mostrar uno a uno los nombres almacenados en la siguiente lista: nombres = 
    [‘Juan’, ‘Marcos’, ‘Laura’, ‘Jose’]
"""

# Ejercicio 10. 
"""
    Confeccionar una función que le enviemos como parámetros dos enteros y nos devuelva el mayor.
"""

# Ejercicio 11. 

"""
    Definir una función que le enviemos como parámetro un string y nos retorne la cantidad de 
    caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función    
    dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.
"""

# Ejercicio 12. 

"""
    Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo 
    string con un caracter. La función debe mostrar el string subrayado con el caracter que indica el segundo
    parámetro
""" 