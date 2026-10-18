"""
    Ejercicio 1: cálculo de número mayor y menor
    Programa que solicita 3 numeros enteros al usuario
    y determina cual es el mayor y cual es el menor
    utilizando las funciones max() y min().

"""

#Solicitando datos al usuario
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
numero3 = int(input("Introduce el tercer numero: "))

#Resultado
print("El numero mas grande entre {}, {} y {} es: {}".format(
    numero1,numero2,numero3,max(numero1,numero2,numero3)) )
print("El numero mas pequeño entre {}, {} y {} es: {}".format(
    numero1,numero2,numero3,min(numero1,numero2,numero3)) )