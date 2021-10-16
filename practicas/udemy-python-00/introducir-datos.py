# ESTILO WCODE PARA CREAR VARIABLES

# int_Nombre_variable = tipo_dato | Variables del tipo entero
# float_Nombre_variable = tipo_dato | Variables con decimales
# str_Nombre_variable = tipo_dato | Variables con Cadenas o caracteres
# bool_Nombre_variable  = tipo_dato | Variables booleanas

# Pseudocódigo
# nombre_variable = tipo_dato
# introducir nombre_variable
# imprime "comentario"

# Declaracion de variables

int_Edad = 0
float_Estatura = 0.0
str_Inicial = ""
str_Apellido = ""

# Inicio del programa

int_Edad = int (input('Introduce tu edad: '))
float_Estatura = float (input('Introduce tu estatura: '))
str_Inicial = input('Introduce tu inicial: ')
str_Apellido = input('Introduce tu apellido: ')

print ("")
print ("Tus datos son: ")
print("")
print("Edad es: %d" %(int_Edad))
print("Estatura es: %.2f" %(float_Estatura))
print("Inicial es: %s" %(str_Inicial))
print("Apellido es: %s" %(str_Apellido))
