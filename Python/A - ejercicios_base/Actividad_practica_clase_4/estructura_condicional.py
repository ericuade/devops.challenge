"""
    Trabajo Practico 4
    Estructura condicional
"""

print("Trabajo Practico 4")
print("Estructura condicional")


# Ejercicio 1:

"""
    Ingresar un nombre si el nombre ingresado es “Marcos” debe mostrar “hola Marcos”, sino debe 
    mostrar “hola desconocido”.
"""

print("")
print("Ejercicio 1 condicionales")
print("-------------------------")
nombre = input("Ingrese el nombre: ")
if nombre == "Marcos":
    print("hola", nombre)
else:
    print("hola desconocido")

# Ejercicio 2:

"""
    Verificar si la cadena de caracteres "manzana" está presente en la lista frutas y, si es así, imprimir 
    un mensaje indicando que se encontraron las manzanas. Si la condición no se cumple, se 
    imprimirá un mensaje indicando que no se encontraron las manzanas. La lista podría ser: 
    fruta=["mandarina", "manzana", "banana", "naranja", "pomelo"
"""

print("")
print("Ejercicio 2")
print("-----------")
lista_frutas = ["mandarina", "manzana", "banana", "naranja", "pomelo"]
if "manzana" in lista_frutas:
    print("Se encontraron las manzanas")
else:
    print("No se encontraron las manzanas")
print("")

# Ejercicio 3: 

"""
    Ingresar la edad de dos hermanos e indicar quién es el mayor o si tienen la misma edad.
""" 

print("")
print("Ejercicio 3")
print("-----------")
edad_hermano_uno = int(input("Ingrese la edad del hermano 1: "))
edad_hermano_dos = int(input("Ingrese la edad del hermano 2: "))
if edad_hermano_uno > edad_hermano_dos:
    print("Hermano 1 es mayor que Hermano 2")
elif edad_hermano_uno < edad_hermano_dos:
    print("Hermano 2 es mayor que Hermano 1")
else:
    print("Tienen la misma edad")

# Ejercicio 4: 

"""
    Ingresar la edad de una persona e indicar si es mayor de edad (mayor o igual a 18 años). 
    Utilizar una variable de tipo booleana para guardar el valor Verdadero si la persona tiene 18 
    años o más y Falso en caso contrario.
"""

print("")
print("Ejercicio 4 - Indicar si una persona es Mayor de edad o no.")
print("-----------")
edad_persona = int(input("Ingrese la edad de la persona: "))
if edad_persona >= 18:
    variableBooleana = True
    print("Es mayor de edad?: ", variableBooleana)
else:
    variableBooleana = False
    print("Es mayor de edad?: ", variableBooleana)
print("")

# Ejercicio 5: 

"""
    Se requiere desarrollar un juego de preguntas, en que se puede responder "si" o "no". Gana 
    quien responde correctamente 3 preguntas. Si se responde mal alguna, no se formula la 
    siguiente y termina el juego (las preguntas son libres, las piensa cada uno)
"""

print("")
print("Ejercicio 5")
print("-----------")
print("""
A continuacion debera responder SI o NO a las preguntas que se le hagan.
Responda correctamente 3 y el juego acaba.
""")

puntuacion = 0

lista = ["Es python un lenguaje interpretado?",
         "Python es orientado a objetos?",
         "Python es multiplataforma?",
         "Se puede usar python como calculadora?"
         ]


for elemento in lista:
    print(elemento)
    respuesta = input("")
    if respuesta == "si":
        puntuacion = puntuacion + 1
    else:
        print("El juego termino")
        break
    if puntuacion == 3:
        print("")
        print("Respondiste bien 3 preguntas, el juego termino")
        break

# Ejercicio 6: 

"""
    Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe 
    recuperar.
    ● Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
    ● Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
    ● Se debe recuperar cuando al menos una de las dos notas es menor a 4.
""" 

print("")
print("Ejercicio 6")
print("-----------")
print("""
Se ingresa las notas de los dos parciales de un alumno
""")
print("")
nota_1 = int(input("Ingrese nota 1: "))
nota_2 = int(input("Ingrese nota 2: "))
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


