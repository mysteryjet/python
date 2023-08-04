"""
Paquetes:
Son directorios donde se almacenan módulos relacionados entre sí.

Para qué sirven?
Para organizar mejor el código y poder reutilizarlo mejor (modularización y reutilización).

Cómo se crea un paquete?
Crear una carpeta o directorio con un archivo dentro llamado __init__.py

Lo que hace __init__.py es "convertir" un directorio en un módulo (paquete) que contiene otros
módulos, y esto lo hace para poder importarlo.
"""
from paquete1.funciones_numericas import *
from paquete1.funciones_cadena import contar_letras

print(multiplicar(5, 6))
print(contar_letras("Manuel"))

