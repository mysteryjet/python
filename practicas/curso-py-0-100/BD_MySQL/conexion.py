import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'Comadreja234!',
        db = 'administracioncursos'
    )
    if conexion.is_connected():
        print("Conexión exitosa.")
        info_server = conexion.get_server_info()
        print("Información del servidor: ", info_server)
except Error as ex:
    print("Error durante la conexión: ", ex)
finally:
    if conexion.is_connected():
        conexion.close() # se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

