"""
    Ejercicio 2: Conversor de temperatura de Fahrenheit a Celcius
    Pide la temperaturta en grados Fahrenheit al usuario, aplica
    la formula de conversion y muestra el resultado en Celcius.

    FORMULA: (Fahrenheit - 32) * 5 / 9

"""

print("Conversor de Fahrenheit (°F) a Celcius (°C)")
print(".................................")

#Solicitud de datos al usuario
grados_fahrenheit = float(input("¿Cual es la temperatura en °F?: "))
print(".................................")
#Conversion de temperatura
grados_celcius = (grados_fahrenheit - 32) * 5 / 9

#Resultado
print("La temperatura en grados °C es: {:.2f}".format(grados_celcius))