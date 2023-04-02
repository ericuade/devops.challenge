#!/usr/bin/python
# This Python file uses the following encoding: utf-8

# Ejercicio 4. 

"""
    Las variables guardan datos de diferente tipo y permiten cambiar su valor. 
    Dadas dos variables numéricas A y B, que el usuario debe ingresar por teclado, se pide:
    a. Duplicar el valor que poseen y mostrarlo por pantalla.
    b. Mostrar en pantalla el valor de A menos el valor de B
"""

print("Duplicando variables")
print("--------------------")
A = int(input("Ingrese primer numero: "))
B = int(input("Ingrese segundo numero: "))
print("a. Duplicamos el valor que poseen y mostramos por pantalla.")
print("El PRIMER numero ahora vale: ", A * 2)
print("El SEGUNDO numero ahora vale: ", B * 2)
print("b. Mostramos en pantalla el valor de A menos el valor de B: ", A - B)

