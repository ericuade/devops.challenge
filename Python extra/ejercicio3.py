# Ejercicio 3. 

"""
    Desarrollar un algoritmo que, dados el valor de una hora de trabajo y la cantidad de horas 
    trabajadas por día, calcule y muestre el valor del sueldo semanal, asumiendo que se trabajan todos los días 
    hábiles y media jornada los sábados. 
    Ejemplo: Ingresa 120 y 8, debe devolver 5280.
"""

print("Algoritmo para calculo de horas trabajo semanal en base a una jornada de 8 horas")
print("---------------------------------------")
valor_hora = int(input("Ingrese valor de hora de trabajo: "))
print(" ")
horas_trabajadas_por_dia = int(input("Ingrese la cantidad de horas de trabajo por dia: "))
print(" ")
total_semana = (valor_hora * horas_trabajadas_por_dia) * 5.5 
print("Debe pagarse por esta semana el total de : ", total_semana)

