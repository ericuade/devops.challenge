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

def suma_ejercicio2():
    print("")
    suma_2 = 0
    valor1 = int(input("Ingrese valor 1: "))
    valor2 = int(input("Ingrese valor 2: "))
    suma_2 = valor1 + valor2
    print("")
    print("El resultado de la suma es: ", suma_2)
    print("-------------------------------------")
    return

for i in range(1, 6):
    suma_ejercicio2()


# Ejercicio 3. 

"""
    Definir una función para imprimir un mensaje por pantalla:
"""

def imprimir_por_pantalla():
    print("Este mensaje esta dentro de la funcion que se invoco.")

imprimir_por_pantalla()



# Ejercicio 4: 

"""
    Escribir dos funciones, una función que le permita al usuario ingresar el texto de la canción favorita 
    y otra para obtener la longitud de esa cadena. Muestre la letra de la canción que ingreso el usuario y la 
    longitud de esa letra.
"""

def texto_cancion_favorita():
    print("** Cancion favorita - Ingresar 1 linea a la vez para generar estrofas **")
    print("** Se pueden pegar parrafos tambien")
    print(" - Para ingresar una linea en blanco presione ENTER")
    print(" - Para salir ingresar 0 ")
    print("------------------------------------------------------------------------")
    cancion = ""
    nombre_cancion = input("Ingrese el nombre de la cancion: ")
    while True:
        texto = input("Ingrese el texto de la cancion favorita: ")
        if texto == "0":
          break
        if texto:
          cancion = cancion + texto + "\n"
        elif texto == "":
          cancion = cancion + texto + "\n"
    print("")
    print("La cancion es: \n", nombre_cancion)
    print("")
    print("La letra es: \n", cancion)
    return cancion

def obtener_longitud_cadena(cadena):
    print("La cantidad de letras de la cancion es: \n", len(cadena))
    return  

cancion = texto_cancion_favorita()
obtener_longitud_cadena(cancion)

# Ejercicio 5. 

"""
    Desarrollar una función que solicite la carga de tres valores y muestre el menor. Desde el bloque 
    principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
"""

def carga_valores():
    valor1 = int(input("Ingrese el 1er valor\n"))
    valor2 = int(input("Ingrese el 2do valor\n"))
    valor3 = int(input("Ingrese el 3er valor\n"))
    if (valor1 < valor2 and valor1 < valor3) or (valor1 < valor3 and valor1 < valor2):
        print("")
        print("El valor mas chicos es:", valor1)
    elif (valor2 < valor1 and valor1 < valor3)  or (valor2 < valor3 and valor2 < valor1):
        print("")
        print("El valor mas chicos es:", valor2)
    elif (valor3 < valor1 and valor3 < valor2)  or (valor3 < valor2 and valor3 < valor1):
        print("")
        print("El valor mas chicos es:", valor3)

carga_valores()
carga_valores()

# Ejercicio 6. 

"""
    Ejercicio 6: Definir dos funciones para Ingresar la primer nota y la segunda nota de los dos parciales 
    de un alumno. Con otra función indicar si promocionó, aprobó o debe recuperar. Se promociona cuando las 
    notas de ambos parciales son mayores o iguales a 7. Se aprueba cuando las notas de ambos parciales son 
    mayores o iguales a 4. Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""

print("")
print("Ejercicio 6")
print("-----------")
print("""
Se ingresa las notas de los dos parciales de un alumno
""")
print("")
def ingreso_notas():
    nota_1 = int(input("Ingrese nota 1: "))
    nota_2 = int(input("Ingrese nota 2: "))
    lista_notas = []
    lista_notas.append(nota_1)
    lista_notas.append(nota_2)  
    return lista_notas

def calculo_notas(nota_1, nota_2):
    print("""
    Si las 2 notas son mayores o iguales a 7 promociona
    Si las 2 notas son mayores o iguales a 4 aprueba
    Si una de las dos notas es menor a 4 , recupera.
    """)
    print("")
    if (nota_1 >= 7 and nota_2 >= 7):
        print("El alumno ha promocionado")
    elif (nota_1 >= 4 and nota_2 >= 4):
        print("El alumno ha aprobado")
    elif (nota_1 <= 4 or nota_2 <= 4):
        print("El alumno debe recuperar")
    return

lista_notas = ingreso_notas()
calculo_notas(lista_notas[0], lista_notas[1])

# Ejercicio 7. 

"""
    Definir una función para calcular e imprimir la suma de los números comprendidos entre 42 y 176.
"""

print("")
print("Ejercicio 7 - Sumar los numeros entre 42 y 176")
print("----------------------------------------------")
def suma_numeros():
    suma_numeros = []
    suma = 0
    # Ingresamos todos los valores a una lista o array
    for i in range(42, 177):
        suma_numeros.append(i)
    # Recorremos la lista y sumamos cada uno de sus valores en una variable
    for i in suma_numeros:
        suma = suma + i
    print(suma)

suma_numeros()

# Ejercicio 8. 

"""
    Utilizando funciones escribir un algoritmo que solicite un nombre de usuario y una contraseña, y 
    que no permita seguir hasta que se introduzcan correctamente. Deberá repetirse hasta que el usuario sea 
    "admin" y la contraseña sea "1234", y en ese caso mostrar el mensaje “Login exitoso”. Tras 3 intentos sin 
    acertar, se deberá mostrar un mensaje indicando que se agotaron esos 3 intentos y finaliza el programa.
"""

print("Ejercicio 7 - User y password")
print("------------------------------")
def user_pass():
    user = "admin"
    passwd = "1234"
    recuento_de_intentos = 0
    user_input = input("Ingrese usuario: ")
    passwd_input = input("Ingrese clave: ")
    recuento_de_intentos = recuento_de_intentos + 1
    while user_input != user and passwd_input != passwd:
        user_input = input("Ingrese usuario: ")
        passwd_input = input("Ingrese clave: ")
        recuento_de_intentos = recuento_de_intentos + 1
        if recuento_de_intentos == 3:
          print("Se agotaron los intentos, programa finalizado!")  
          break
        
    if user_input == user and passwd_input == passwd:
        print("Login Exitoso!")
    
    print("")

user_pass()

# Ejercicio 9. 

"""
    Utilizando una función mostrar uno a uno los nombres almacenados en la siguiente lista: nombres = 
    [‘Juan’, ‘Marcos’, ‘Laura’, ‘Jose’]
"""
print("Ejercicio 9 - mostrar nombres de una lista")
print("nombres Juan, Pedro, Luis, Laura")
print("------------------------------")
def mostrar_nombres():
    nombres = ["Juan", "Pedro", "Luis", "Laura"]
    for nombre in nombres:
        print(nombre)

mostrar_nombres()

# Ejercicio 10. 
"""
    Confeccionar una función que le enviemos como parámetros dos enteros y nos devuelva el mayor.
"""

print("Ejercicio 10 - Mayor de 2 numeros enteros")
print("-----------------------------------------")
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))
print("")
def mayor_que(numero1, numero2):
    if numero1 < numero2:
        print("El numero mayor es el: ", numero2)
    else:
        print("El numero mayor es el: ", numero1)

mayor_que(numero1, numero2)

# Ejercicio 11. 

"""
    Definir una función que le enviemos como parámetro un string y nos retorne la cantidad de 
    caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función    
    dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.
"""

print("")
print("Ejercicio 11 - Cantidad de caracteres de un nombre")
print("---------------------------------------------------")
print("")
nombre1 = input("Ingrese nombre 1: ")
nombre2 = input("Ingrese nombre 2: ")

def cantidad_caracteres(nombre):
    cantidad_caracteres = len(nombre)
    return cantidad_caracteres

cantidad_nombre_1 = cantidad_caracteres(nombre1)
cantidad_nombre_2 = cantidad_caracteres(nombre2)

if cantidad_nombre_1 > cantidad_nombre_2:
    print("La palabra que tiene mas caracteres es: ", nombre1)
else:
    print("La palabra que tiene mas caracteres es: ", nombre2)


# Ejercicio 12. 

"""
    Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo 
    string con un caracter. La función debe mostrar el string subrayado con el caracter que indica el segundo
    parámetro
"""

