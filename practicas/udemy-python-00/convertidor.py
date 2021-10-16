'''
CONVERTIR NUMERO DECIMAL EN AÑOS CON MESES Y DIAS
1 año  = 12 meses
1 mes =  30 dias
1 dia  = 24 horas


1 año          -------    12 meses
num user -------      x
'''

num_user = float(input("Ingrese los años con punto decimal: "))
int_anio = int(num_user)
int_meses = (num_user * 12) % 12
int_dias = (num_user * 360)  % 30

print(f"{num_user} años es igual a {int_anio} años, {int(int_meses)} meses y {int(int_dias)} días.")
