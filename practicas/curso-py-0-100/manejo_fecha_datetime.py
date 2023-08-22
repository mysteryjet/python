# from datetime import datetime
import datetime

# fecha_actual = datetime.now()
fecha_actual = datetime.datetime.now()
print(fecha_actual)

fecha = datetime.datetime(2023, 8, 5, 6, 3, 21)
print(fecha)

fecha_actual2 = datetime.datetime.strftime(fecha_actual, '%d/%m/%Y %H:%M:%S')
print(fecha_actual2)

fecha_actual3 = datetime.datetime.strftime(fecha_actual, '%B %d %Y %H:%M:%S')
print(fecha_actual3)

fecha_texto = 'August 04 2023 18:14:34'
fecha_actual4 = datetime.datetime.strptime(fecha_texto, '%B %d %Y %H:%M:%S')
print("Fecha actual 4: {}".format(fecha_actual4))

dia = int(datetime.datetime.strftime(fecha_actual, '%d'))
print("Día: {}".format(dia))
print(type(dia))

hora_actual = datetime.datetime.strftime(fecha_actual, '%H:%M:%S')
print("Hora actual: {}".format(hora_actual))
print(type(hora_actual))

# operar con fechas
fecha_aniversario = datetime.datetime(2012, 9, 27)
diferencia = fecha_aniversario - fecha_actual
print("Faltan {} para el aniversario.".format(diferencia, '%d'))

anno_actual = int(datetime.datetime.strftime(fecha_actual, '%Y'))
print('Año actual: {}'.format(anno_actual))
anno_ani = int(datetime.datetime.strftime(fecha_aniversario, '%Y'))
print('Año cuando nos conocimos: {}'.format(anno_ani))
anno_juntos = anno_actual - anno_ani
print("Años juntos: {}".format(anno_juntos))

dia_delta = datetime.timedelta(days=5)
fecha_inicial = datetime.date.today()
print("Otra forma de sacar la fecha: {}".format(fecha_inicial))

fecha = datetime.datetime.now().isoformat()
print("Fecha formato ISO: {}".format(fecha))
