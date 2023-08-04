import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Comadreja234!',
        db='administracioncursos'
    )
    if conexion.is_connected():
        print("Conexión exitosa.")
        cursor = conexion.cursor()
        nombre_asignatura = input("Ingrese nombre de la asignatura: ")
        materia_asignatura = int(input("Ingrese el numero de MateriaAsignatura: "))
        # cursor.execute("INSERT INTO asignaturas (Asignatura, MateriaAsignatura) VALUES ('Herramientas de Cómputo', 2)")
        sentencia = "INSERT INTO asignaturas (Asignatura, MateriaAsignatura) VALUES ('{}', {})".format(nombre_asignatura, materia_asignatura)
        cursor.execute(sentencia)
        conexion.commit()  # confirma la acción que se esta ejecutando
        print("Registro insertado con éxito.")
except Error as ex:
    print("Error durante la conexión: ", ex)
finally:
    if conexion.is_connected():
        conexion.close()  # se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

