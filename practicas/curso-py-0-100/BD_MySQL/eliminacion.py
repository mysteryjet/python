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
        # sentencia = cursor.execute("UPDATE asignaturas SET Asignatura = 'Contabilidad 1' WHERE idAsignatura = 6")
        sentencia = cursor.execute("DELETE FROM asignaturas WHERE idAsignatura = 6")
        cursor.execute(sentencia)
        conexion.commit()  # confirma la acción que se esta ejecutando
        print("Registro eliminado con éxito.")
except Error as ex:
    print("Error durante la conexión: ", ex)
finally:
    if conexion.is_connected():
        conexion.close()  # se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

