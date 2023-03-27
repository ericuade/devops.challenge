# Manejo de cadenas de caracteres

# Ejercicio 1: 
"""
    Definir en una variable el nombre del usuario del programa y mostrar un mensaje para 
    saludarlo. Ejemplo: Si el usuario se llama Juan, se debe mostrar el mensaje: Hola Juan y bienvenido.
"""
usuario = "Carlos"
print("Hola",usuario,"bienvenido.")
print("")

#Ejercicio 2

"""
    Asignar a una variable mes el nombre del mes actual y a otra variable año el año actual, 
    mostrar el mes y el año en una sola línea. Por Ejemplo si ingresa mes= Marzo y año= 2023, debe aparecer 
    Marzo 2023.
"""
mes = "Marzo"
anio_actual = 2023
print(mes, anio_actual)
print("")


#Ejercicio 3: 
 
"""
    Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y 
    la cantidad de letras que lo componen. Mostrar el resultado.
"""

nombre_persona = input("Ingrese el su nombre: ")
print("La primera letra del nombre es: ", nombre_persona[0])
print("La cantidad de letras de el nombre son: ", len(nombre_persona))
print("")

#Ejercicio 4

"""
    Asignar (dar un valor) a tres variables y luego mostrarlas en una oración. Ejemplo: 
    nombre=”Juan”, acción=”estudia”, asunto=”Python”, deberá mostrar: Juan estudia Python
"""

nombre="Juan"
acción="estudia"
asunto="Python"
print(nombre,acción,asunto)
print("")

#Ejercicio 5

"""
    Asignar una variable con un texto y mostrarla 3 veces. Mostrar el resultado. Por ejemplo con 
    la variable Historia_corta = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'; debería aparecer por 
    pantalla: Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur 
    adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.
"""
texto = " Hoy es 23 de Marzo y un Tiktoker dijo que nos visitan los ETs"
print(texto * 3)
print("")

#Ejercicio 6

""" 
    Asignar a una variable un texto y reemplazar las a por ¿ (str.replace). Mostrar el resultado.
    Por ejemplo: Letra = “En Argentina nací, tierra de Diego y Lionel, de los pibes de Malvinas que jamás olvidaré”
    debería quedar: En ArgentinA nAcí, tierrA de Diego y Lionel, de los pibes de MAlvinAs que jAmás olvidAré
"""

letra = "En Argentina nací, tierra de Diego y Lionel, de los pibes de Malvinas que jamás olvidaré"
letra_nueva = letra.replace("a", "A")
print(letra_nueva)
print("")

#Ejercicio 7
# Mostrar un ejemplo de uso de slit(),find()

frase = "Los dos guerreros más poderosos son la paciencia y el tiempo"
nueva_frase = frase.split(" ")
print(nueva_frase)
encontrar_en_frase = frase.find("guerreros")
print("La posicion donde esta la palbra es: ",encontrar_en_frase)
print("")

#Ejercicio 8: 
# Dada una cadena que contiene nombres de frutas: frutas = “Manzana,Naranja,Mandarina,Banana,Kiwi”

"""
    ● Mostrar el resultado o imprimir los caracteres 0, 1, 2, 15, -1 y -2
    ● Mostrar el resultado o imprimir los dos primeros caracteres.
    ● Mostrar el resultado o imprimir los tres últimos caracteres.
    ● Mostrar el resultado o imprimir la cadena cada tres caracteres.
    ● Mostrar el resultado o imprimir la cadena en sentido inverso.
"""

frutas = "Manzana,Naranja,Mandarina,Banana,Kiwi"
print(frutas)
print("")
print("Imprimir los caracteres 0, 1, 2, 15, -1 y -2")
print(frutas[0],frutas[1],frutas[2],frutas[15],frutas[-1],frutas[-2])
print("Imprimir los dos primeros caracteres")
print(frutas[0],frutas[1])
print("Imprimir los tres últimos caracteres")
print(frutas[-1],frutas[-2],frutas[-3])
print("Imprimir la cadena en sentido inverso")
print(frutas[::-1])
print("")


#Ejercicio 9. Dada una cadena y un carácter:

"""
    ● Insertar el carácter entre cada letra de la cadena. Por ejemplo, cadena y , debe devolver 
    c,a,d,e,n,a
    ● Reemplazar todos los espacios por el carácter _. Ej: “el nombre de mi archivo de 
    texto.txt” y _ debe devolver el_nombre_de_mi_archivo_de_texto.txt
"""

cadena = "cadena"
cadena_modificada = ",".join(cadena)
print(cadena_modificada)
textonuevo = "El nombre de mi archivo de word.doc"
textonuevo_modificado = textonuevo.replace(" ", "_")
print(textonuevo_modificado)
print("")


#Ejercicio 10. 
# Diseñar un programa que reciba una fecha en formato dd/mm/aaaa y muestre por pantalla, el día, el mes y el año.

fecha = "23/03/2023"
print("El dia es: ", fecha[:2])
print("El mes es: ", fecha[3:5])
print("El año es: ", fecha[6:])


#Ejercicio 11. 

"""
    Dada una cadena con varias palabras, devolver la cadena con la primera letra de cada palabra 
    en mayúsculas. Por ejemplo, si recibe la rioja debe devolver La Rioja.
"""

print("")
cadena_de_palabras = "la rioja la pampa la mendoza la chubut"
print(cadena_de_palabras.title())
print("")

#Ejercicio 12. 

"""
    Dada una cadena de caracteres, devolver solamente las letras consonantes o las vocales.
    Mostrar por consola.
"""



#Ejercicio 13. 

""" 
    Dadas dos cadenas de caracteres, indicar si la segunda cadena es una subcadena de la primera. 
    Por ejemplo, “sub” es una subcadena de “subcadena”
"""
cadena1 = input("Ingrese cadena 1: ")
cadena2 = input("Ingrese cadena 2: ")
print("Es la cadena2 una subcadena de cadena1?", cadena2 in cadena1)