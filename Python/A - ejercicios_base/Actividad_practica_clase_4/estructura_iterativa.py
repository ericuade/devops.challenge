"""
    ESTRUCTURA ITERATIVA
"""

# Ejercicio 1: 

"""
    Escribir un algoritmo que muestre los primeros 25 números naturales.
"""

print("")
print("Ejercicio 1 - 25 primeros numeros naturales")
print("-------------------------------------------")
for i in range(1,26):
    print(i)


# Ejercicio 2: 

"""
    Definir una cadena de caracteres. Recorrer contando 
    la cantidad de vocales que la componen
"""

print("")
print("Ejercicio 2")
print("Dada una cadena de caracteres: 'Otorrinonaringolo' devolver la cantidad de vocales que la componen")
print("--------------------------------------------------------------------------------------------------")
cadena_caracteres = "Otorrinonaringologo"
cantidadVocales = 0
for i in cadena_caracteres:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cantidadVocales = cantidadVocales + 1
print("")
print("La cantidad de Vocales que componen la cadena son: ", cantidadVocales)

#Ejercicio 3: 

"""
    Escribir un algoritmo que muestre la cuenta regresiva desde 10.
"""

print("")
print("Ejercicio 3 - Cuenta regresiva desde 10") 
print("---------------------------------------") 
aux = 11
for i in range(1, aux + 1):
    print(aux - i)
print("")

#Ejercicio 4: 

"""
    Crear un algoritmo que haga la cuenta regresiva desde 20 solo mostrando números pares.
"""

print("")
print("Ejercicio 4 - Cuenta regresiva desde 20 mostrando numeros pares") 
print("---------------------------------------") 
aux = 21
for i in range(1, aux, 2):
    print(aux - i)
print("")

#Ejercicio 5: 

"""
    Desarrollar un programa que realice la cuenta regresiva entre dos números que el usuario 
    ingrese.
"""

print("")
print("Ejercicio 5 - Cuenta regresiva con parametros pasados por el usuario") 
print("--------------------------------------------------------------------") 
valor1 = int(input("Ingrese valor 1 (Desde): "))
valor2 = int(input("Ingrese valor 2 (Hasta): "))
for i in range(valor1 - 1, valor2):
    print(valor2 - i)
print("")


#Ejercicio 6: 

"""
    Calcular e imprimir la suma de los números comprendidos entre 42 y 176.
"""
print("")
print("Ejercicio 6 - Sumar los numeros entre 42 y 176")
print("----------------------------------------------")
suma_numeros = []
suma = 0
# Ingresamos todos los valores a una lista o array
for i in range(42, 177):
    suma_numeros.append(i)
# Recorremos la lista y sumamos cada uno de sus valores en una variable
for i in suma_numeros:
    suma = suma + i
print(suma)


#Ejercicio 7: 

"""
    Mostrar las tablas de multiplicar (entre 1 y 10) del número 4. 
    ¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la 
    tabla de multiplicar a mostrar?
"""

print("")
print("Ejercicio 7 - Tabla de multiplicar del 4")
print("----------------------------------------")
cuatro = 4
for i in range(1 ,11):
    print(f"{cuatro} * {i} = ",cuatro * i)
print(" ")
numero_usuario = int(input("Le solicitamos ingresar un numero para calcular la tabla de multiplicar de ese numero: "))
print("")
if numero_usuario == 4:
    print("El numero ya fue calculado")
elif numero_usuario != 4:
    print(f"La tabla de multiplicar de {numero_usuario} es: ")
    for i in range(1 ,11):
        print(f"{numero_usuario} * {i} = ",numero_usuario * i)


#Ejercicio 8: 

"""
    Iterando sobre una lista de cadenas de caracteres e imprimiendo solo las que comienzan con 
    una letra específica. Por ej: cadena=[“pepinos”, “tomates”, “naranjas”, “peras”], debe mostrar solo las que 
    comiencen con la letra “p”
"""
print("Ejercicio 8 - Indicar las cadenas de caracteres que empiezan con la letra p ")
print("------------")
cadena = ["pepinos", "tomates", "naranjas", "peras"]
for i in cadena:
    if "p" in i:
        print(f"La palabra {i} contiene la letra 'p'")
print("")


#Ejercicio 9: 

"""
    Escribir un algoritmo que lea números enteros hasta que se ingrese un 0, y muestre el 
    promedio y la cantidad de números ingresados. Piense cómo debe inicializar las variables.
"""

print("Ejercicio 9 - Promedio de numeros y cantidad")
print("--------------------------------------------")
suma_de_numeros = 0
cantidad_numero_ingresado = 0
numero_ingresado = int(input("Ingrese el numero: "))
while (numero_ingresado != 0):
    numero_ingresado = int(input("Ingrese el numero: "))
    suma_de_numeros = suma_de_numeros + numero_ingresado
    cantidad_numero_ingresado = cantidad_numero_ingresado + 1
promedio = suma_de_numeros / cantidad_numero_ingresado
print("")
print(f"El promedio de los numeros es: {promedio}")
print(f"La cantidad de numeros ingresados es: {cantidad_numero_ingresado}")
print("")


#Ejercicio 10: 

"""
    Un negocio desea saber el importe total recaudado al fin del día, desea contar con un programa 
    que pueda ingresar el importe de cada venta realizada. Para indicar que finalizó el día se ingresa 
    -1. ¿Cuál fue el monto total vendido y cuántas ventas se realizaron? El importe de cada venta 
    realizada debe ser un valor positivo.
"""

print("Ejercicio 10 - Promedio de ventas diarias - Para cancelar el programa ingrese '-1'")
print("----------------------------------------------------------------------------------")
venta_ingresada = int(input("Ingrese el valor de la venta: "))
if venta_ingresada == 0:
        print("No puede haber una venta con valor 0")
cantidad_ventas_ingresadas = 0
monto_total_vendido = 0
while (venta_ingresada != -1):
    venta_ingresada = int(input("Ingrese el valor de la venta: "))
    if venta_ingresada == 0:
        print("No puede haber una venta con valor 0")
    elif venta_ingresada >= 1:
        monto_total_vendido = monto_total_vendido + venta_ingresada
        cantidad_ventas_ingresadas = cantidad_ventas_ingresadas + 1
print("")
print(f"El monto total vendido es: {monto_total_vendido}")
print(f"La cantidad de ventas ingresadas es: {cantidad_ventas_ingresadas}")
print("")


#Ejercicio 11: 

"""
    “El Veloz”, una pequeña agencia de automóviles, cuenta con un vendedor que cobra un salario 
    base y una comisión del 1,5% sobre el precio de cada unidad vendida. Ingresar el nombre del 
    vendedor, el salario base y según la cantidad de autos vendida en el mes, ingresar el valor de 
    cada unidad para calcular el salario bruto del mes.
"""

print("Ejercicio 11 - Agencia de Automoviles 'El Veloz'")
print("------------------------------------------------")
suma_ventas_mes = 0
autos = ["Peugeot 208", "Toyota Etios", "Renault Logan","Audi A3"]
comision = 0.015
nombre_vendedor = input("Ingrese el nombre del vendedor: ")
base_salario_agente = int(input("Ingrese el salario Base sin comisiones: "))
for elemento in autos:
    print(f"Cuantos {elemento} vendio?")
    cantidad_vendido = int(input())
    print(f"Cuanto vale {elemento}?")
    precio_venta = int(input())
    monto_total = cantidad_vendido * precio_venta 
    comision_total = monto_total * comision
    suma_ventas_mes = suma_ventas_mes + monto_total + comision_total
print("")
print(f"El salario total del Vendedor es: {base_salario_agente + suma_ventas_mes}")




#Ejercicio 12: 

"""
    Escribir un algoritmo que solicite un nombre de usuario y una contraseña, y que no permita 
    seguir hasta que se introduzcan correctamente. Deberá repetirse hasta que el usuario sea 
    "admin" y la contraseña sea "1234", y en ese caso mostrar el mensaje “Login exitoso”. Tras 3 
    intentos sin acertar, se deberá mostrar un mensaje indicando que se agotaron esos 3 intentos 
    y finaliza el programa.
"""

print("Ejercicio 12 - User y password")
print("------------------------------")

user = "admin"
passwd = "1234"
recuento_de_intentos = 0
user_input = input("Ingrese usuario: ")
passwd_input = input("Ingrese clave: ")

while user_input != user and passwd_input != passwd:
    user_input = input("Ingrese usuario: ")
    passwd_input = input("Ingrese clave: ")
    recuento_de_intentos = recuento_de_intentos + 1
    if recuento_de_intentos == 2:
      print("Se agotaron los intentos, programa finalizado!")  
      break
      
if user_input == user and passwd_input == passwd:
  print("Login Exitoso!")
  
print("")




#Ejercicio 13: 

"""
    Escoger tres ejercicios y resolver cambiando FOR por WHILE ó WHILE por FOR
"""

