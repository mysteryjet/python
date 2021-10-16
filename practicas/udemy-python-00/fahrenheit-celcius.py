# Convertir grados Fahrenheit a Celcius

float_celcius = 0
float_fahrenheit = 0
float_fahrenheit = float(input ("Introduce el valor de uno de los grados Fahrenheit: "))
float_celcius = (float_fahrenheit - 32.0) * 5.0 / 9.0
print(f"{ float_fahrenheit} grados Fahrenheit equivalen a {float_celcius} grados Celcius.")
print(type(float_celcius))