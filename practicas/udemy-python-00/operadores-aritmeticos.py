# OPERADORES ARITMÉTICOS

# Constantes
# const_NOMBRE_CONSTANTE = tipo_dato | constante de cualquier tipo de datos

# Principales operadores aritméticos en Python

# Símbolo       Significado             Ejemplo             Resultado
#    +                  Suma                        a = 10 + 5              a es 15
#    -                    Resta                         a = 12 - 7              a es 5
#    *                  Multiplicación          a = 7 * 5           a es 35 
#   **                  Exponente               a =  2 ** 3         a es 8
#    /                  División                       a = 12. / 2         a es 6.25
#  //                   División entera         a = 12.5 // 2       a es 6.0
# %                     Módulo                      a = 7 % 2           a es 1

str_trama = "2500000777"
int_parte_entera = 0
int_parte_decimal = 0

#Programa
print("****FORMATEAR TRAMA****")
print("Trama inicial: %s" %(str_trama))
print("*****************************")
int_parte_entera =  int(str_trama)/1000
print("Parte entera: %d " %(int_parte_entera))
int_parte_decimal = int(str_trama)%1000
print("Parte decimal: %d" %(int_parte_decimal))
print("*******************************")
print("Precio: %d.%d" % (int_parte_entera,int_parte_decimal))