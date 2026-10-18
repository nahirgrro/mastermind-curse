
"""
    Ejercicio 3: Conversor de Libras a Euro con dos enfoques
    de forma variable en la cual solicita la tasa de cambio
    directamente al usurio, y de forma estática utilizando
    una taza de cambio fija.

"""

print("Conversor de Libras a Euros")
print("...........................")

#Conversor de monto variable
cantidad_en_libras = float(input("Ingrese la cantidad de libras: "))
print("...........................")

conversor_libra_euro = float(input("Introduzca la conversion euro -> libra: "))
print("...........................")

print("La cantidad de euros es: {:.2f} €".format(cantidad_en_libras * conversor_libra_euro))
print("...........................")

#Conversor de monto estático
cantidad_en_libras = float(input("Ingrese la cantidad de libras: "))
print("...........................")

precio_del_euro = 1.186

print("La cantidad de euro es: {:.2f} €".format(cantidad_en_libras * precio_del_euro))
